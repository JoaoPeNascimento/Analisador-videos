import os
import sys
import time
import pytubefix
from google import genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("Erro: Chave de API não encontrada.")
    print("Crie um arquivo chamado '.env' na mesma pasta com o conteúdo:")
    print("GOOGLE_API_KEY=SuaChaveAqui")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)

def download_audio_native(url, filename="audio_temp.m4a"):
    print(f"Baixando áudio do YouTube...")
    try:
        yt = pytubefix.YouTube(url)
        print(f"   Título: {yt.title}")
        
        audio_stream = yt.streams.get_audio_only()
        if not audio_stream:
            raise Exception("Nenhum stream de áudio encontrado.")

        audio_stream.download(filename=filename)
        print("Download concluído.")
        return filename
    except Exception as e:
        print(f"❌ Erro no download: {e}")
        return None

def processar_video(audio_path):
    print("Enviando áudio para o Google Gemini...")
    
    try:
        file_obj = client.files.upload(file=audio_path)
        print(f"   Arquivo enviado. Processando...")

        while file_obj.state.name == "PROCESSING":
            time.sleep(2)
            file_obj = client.files.get(name=file_obj.name)
            
        if file_obj.state.name == "FAILED":
            raise ValueError("O processamento do arquivo falhou no Google.")

        print("Gerando resumo...")
        
        prompt = (
            "Você é um assistente de estudo. Ouça o áudio deste vídeo com atenção. "
            "Crie um resumo detalhado em Markdown (PT-BR). "
            "Inclua: Título Principal, Pontos Chave (bullet points) e uma Conclusão Prática."
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[file_obj, prompt]
        )
        
        return response.text

    except Exception as e:
        print(f"Erro na IA: {e}")
        return None
    finally:
        try:
            if 'file_obj' in locals():
                client.files.delete(name=file_obj.name)
        except:
            pass

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <URL_DO_YOUTUBE>")
        sys.exit(1)

    url = sys.argv[1]
    audio_filename = "temp_audio.m4a"

    if download_audio_native(url, audio_filename):
        resumo = processar_video(audio_filename)
        
        if resumo:
            print("\n" + "="*40)
            print(resumo)
            print("="*40 + "\n")
            
            with open("resumo.md", "w", encoding="utf-8") as f:
                f.write(resumo)
            print("Salvo em 'resumo.md'")

        if os.path.exists(audio_filename):
            os.remove(audio_filename)

if __name__ == "__main__":
    main()