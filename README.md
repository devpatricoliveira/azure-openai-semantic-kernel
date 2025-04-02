# 🚀 Explorando IA com Azure OpenAI & Semantic Kernel

## 📌 Sobre o Projeto
Fala, galera! Tô aqui pra contar o que aprendi com o material do Pablo Lopes, que é Cloud Advocate na Microsoft (o cara é brabo, segue ele no Insta e TikTok: @techdevpablo). O objetivo desse conteúdo é meter a mão na massa com a API do Azure OpenAI e dar uma pincelada no Semantic Kernel, que é tipo um middleware pra IA. A ideia é aprender a fazer apps maneiras usando IA, sacando como chamar APIs e criar agentes de IA que automatizam umas paradas. 🧠

## 🎯 O que vamos fazer?
- Explorar a API do Azure OpenAI e suas funcionalidades.
- Entender o que é o Semantic Kernel e como ele pode ser útil.
- Configurar o ambiente pra rodar os testes.
- Criar exemplos práticos de uso da API.

## 📂 Estrutura do Projeto
```
/azure-openai-project
│-- .env               # Variáveis de ambiente (não compartilhe!)
│-- .gitignore         # Ignora arquivos desnecessários no Git
│-- README.md          # Documentação do projeto
│-- config.json        # Configurações da API e integração
│-- main.py            # Código principal
│-- requirements.txt   # Dependências do projeto
```

## 🔧 Como configurar
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/azure-openai-project.git
cd azure-openai-project
```

### 2️⃣ Criar e ativar um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar as variáveis de ambiente
Crie um arquivo `.env` e adicione essas informações:
```plaintext
AZURE_OPENAI_ENDPOINT= "cole_o_endpoint_aqui"
AZURE_OPENAI_API_KEY= "cole_sua_chave_aqui"
AZURE_OPENAI_API_VERSION= "cole_a_versão_da_API_aqui"
```

## 🧠 O que dá pra fazer com Azure OpenAI?
A API do Azure OpenAI é tipo um canivete suíço da IA: dá pra fazer um monte de coisa! Ela suporta vários modos:
- **Chat**: Pra criar conversas (tipo um bot no WhatsApp). 🗨️
- **Completar (Completions)**: Gera texto a partir de um prompt (ex.: "me conta uma piada de manga"). ✍️
- **Imagens**: Gera imagens do zero (usando o DALL-E 3). 🖼️
- **Áudio**: Faz transcrição ou geração de voz. 🎙️

## 🎭 Exemplos de Uso
### 🔹 Criando um Chatbot
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

messages = [{"role": "user", "content": "E aí, beleza?"}]

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    messages=messages,
    temperature=0.7
)

print(response["choices"][0]["message"]["content"])
```

### 🔹 Gerando um Texto
```python
response = client.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    prompt="Me conta uma piada de manga",
    max_tokens=32,
    temperature=1.0,
    n=1
)

print(response["choices"][0]["text"].strip())
```

### 🔹 Criando uma Imagem com DALL-E 3
```python
response = client.images.generate(
    model="dall-e-3",
    prompt="Uma cidade futurista no pôr do sol",
    n=1,
    size="1024x1024"
)

print(response["data"][0]["url"])
```

## 🏆 O que é o Semantic Kernel?
O **Semantic Kernel** é tipo um "faz-tudo" pra IA. Ele ajuda a:
- Adicionar funcionalidades inteligentes nas aplicações.
- Criar agentes de IA que automatizam tarefas.
- Gerenciar memória e funções personalizadas para que a IA lembre de contextos anteriores.

### 🔹 Exemplo de Integração com Semantic Kernel
```python
from semantic_kernel import Kernel

kernel = Kernel()

@kernel.function("dizer_ola")
def dizer_ola():
    return "Olá, tudo bem?"

print(kernel.invoke("dizer_ola"))
```

## 📚 Recursos e Referências
- 🔗 [Documentação oficial do Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
- 🔗 [Introdução ao Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview)
- 📄 **Slides de Apoio:** *Apresentação sobre API e Semantic Kernel.pptx*

## 🚀 AFechando com Chave de Ouro
O Azure OpenAI é brabo pra criar apps com IA: dá pra fazer chat, gerar texto, imagens e até trabalhar com áudio. O Semantic Kernel entra pra deixar tudo mais top, com agentes de IA e funções automáticas. Com isso, tu consegue criar umas aplicações maneiras e ainda impressionar o prof na entrega do trabalho. Agora estou pronto para meter a mão na massa agora! 😎 🤖🔥

