# Analisador de Vídeos com IA

Este projeto é uma ferramenta de automação em Python que extrai o áudio de vídeos do YouTube e utiliza o modelo **Google Gemini** para gerar resumos detalhados e práticos.

## 📋 Funcionalidades

- **Download de Áudio:** Extrai automaticamente a faixa de áudio de vídeos do YouTube utilizando a biblioteca pytubefix.

- **Processamento com IA:** Envia o áudio para a API do Google GenAI para processamento multimodal.

- **Geração de Resumos:** Cria um resumo em formato Markdown contendo título, pontos-chave (bullet points) e uma conclusão prática.

- **Limpeza Automática:** Remove ficheiros de áudio temporários após o processamento.

- **Exportação:** Guarda o resultado final num ficheiro local chamado resumo.md.

## 🛠️ Pré-requisitos

- Python 3.x instalado.

- Uma chave de API do Google AI Studio (Google Gemini).

## 🚀 Instalação

1- **Clone o repositório**:

```Bash
git clone https://github.com/joaopenascimento/analisador-videos.git
cd analisador-videos
```

2- **Crie um ambiente virtual (recomendado)**:

```Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3- \***\*Instale as dependências**: Com base nas importações do código, instale as bibliotecas necessárias:

```Bash
pip install pytubefix google-genai python-dotenv
```

## ⚙️ Configuração

O projeto utiliza variáveis de ambiente para gerir credenciais de segurança.

1- Crie um ficheiro .env na raiz do projeto (pode usar o .env.sample como base).

1- Adicione a sua chave de API do Google:

```Ini, TOML
GOOGLE_API_KEY=SuaChaveAqui
```

## 💻 Como Utilizar

Execute o script `main.py` passando o URL do vídeo do YouTube que deseja resumir como argumento:

```Bash
python main.py "URL_DO_VIDEO"
```

**Exemplo**:

```Bash
python main.py "https://www.youtube.com/watch?v=Exemplo123"
```

**O que acontece durante a execução:**
1- O script faz o download do áudio (temp_audio.m4a).

2- Faz o upload para o Google Gemini e aguarda o processamento.

3- Exibe o resumo no terminal.

4- Cria um ficheiro resumo.md com o conteúdo gerado.

## 🤖 Modelo Utilizado

O script está configurado para utilizar o modelo `gemini-2.5-flash` para garantir rapidez e eficiência na análise de janelas de contexto longas (áudio).
