# 🚀 Explorando IA com Azure OpenAI & Semantic Kernel no Mundo Pokémon

## 📌 Sobre o Projeto
Fala, galera! Tô aqui pra compartilhar o que aprendi com o material do Pablo Lopes, que é Cloud Advocate na Microsoft (o cara é brabo, segue ele no Insta e TikTok: @techdevpablo). O objetivo desse conteúdo é meter a mão na massa com a API do Azure OpenAI e dar uma pincelada no Semantic Kernel, que é tipo um middleware pra IA. A ideia é aprender a fazer apps maneiras usando IA, sacando como chamar APIs e criar agentes de IA que automatizam umas paradas. 🧠

Mas espera… Ao invés de só criar um chatbot genérico, vamos usar essa tecnologia para criar uma aplicação sobre o universo Pokémon! Que é algo que gosto e deixa o projeto com minha personalidade. Vamos interagir com os Pokémons clássicos como Bulbasaur, Charmander e Squirtle, e a IA vai fornecer informações e até curiosidades sobre eles! 🚀🔥

## 🎯 O que vamos fazer?
Explorar a API do Azure OpenAI e suas funcionalidades.

Entender o que é o Semantic Kernel e como ele pode ser útil.

Configurar o ambiente pra rodar os testes.

Criar exemplos práticos de uso da API para consultar Pokémons clássicos.

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
git clone https://github.com/seu-usuario/azure-openai-semantic-kernel.git
azure-openai-semantic-kernel
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

Chat: Pra criar conversas (tipo um bot sobre Pokémons). 🗨️

Completar (Completions): Gera texto a partir de um prompt (ex.: "Me conta sobre o Charmander"). ✍️

Imagens: Gera imagens do zero (usando o DALL-E 3, tipo criando um Pokémon do zero). 🖼️

Áudio: Faz transcrição ou geração de voz (poderia ser a IA narrando o universo Pokémon). 🎙️

🎭 Exemplos de Uso
🔹 Criando um Chatbot Pokémon
Vamos criar um chatbot que conversa sobre Pokémons! Quando o usuário escolher um Pokémon, a IA retorna as informações sobre ele.

```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

messages = [{"role": "user", "content": "Me conta sobre o Charmander"}]

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    messages=messages,
    temperature=0.7
)

print(response["choices"][0]["message"]["content"])


```

### 🔹 Gerando um Texto Sobre Pokémons
Imagine que você quer saber mais sobre Bulbasaur? A IA pode gerar uma resposta com as informações do Pokémon baseado no que você pedir!

```python
response = client.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    prompt="Me conta sobre o Pokémon Bulbasaur",
    max_tokens=150,
    temperature=1.0,
    n=1
)

print(response["choices"][0]["text"].strip())


```

### 🔹 Criando uma Imagem com DALL-E 3
Quem não ama ver uma boa imagem de Pokémon, né? Vamos criar imagens de Pokémons usando DALL-E 3.

```python
response = client.images.generate(
    model="dall-e-3",
    prompt="Um Pokémon misturado entre Bulbasaur e Charmander, com a chama de Charmander e as folhas de Bulbasaur",
    n=1,
    size="1024x1024"
)

print(response["data"][0]["url"])

```

🏆 O que é o Semantic Kernel?
O Semantic Kernel é como se fosse um middleware para IA, ajudando a:

Adicionar funcionalidades inteligentes nas aplicações.

Criar agentes de IA que automatizam tarefas.

Gerenciar memória e funções personalizadas para que a IA lembre de contextos anteriores.

Com isso, podemos usar o Semantic Kernel para criar agentes de IA Pokémon que automatizam tarefas, como responder perguntas ou recomendar Pokémons.

🔹 Exemplo de Integração com Semantic Kernel
Aqui, vamos criar um agente de IA que lembra do Pokémon que você escolheu e dá informações sobre ele:

```python
from semantic_kernel import Kernel

class SemanticKernel:
    def __init__(self):
        self.pokemon_info = {
            "Bulbasaur": "Bulbasaur é um Pokémon de tipo Grama/Venenoso. Ele evolui para Ivysaur e depois para Venusaur.",
            "Charmander": "Charmander é um Pokémon de tipo Fogo. Ele evolui para Charmeleon e depois para Charizard.",
            "Squirtle": "Squirtle é um Pokémon de tipo Água. Ele evolui para Wartortle e depois para Blastoise."
        }
        self.kernel = Kernel()

    @self.kernel.function("informacao_pokemon")
    def informacao_pokemon(self, pokemon):
        return self.pokemon_info.get(pokemon, "Pokémon não encontrado. Escolha entre Bulbasaur, Charmander ou Squirtle.")

# Usando o Kernel para buscar a info
semantic_kernel = SemanticKernel()

print(semantic_kernel.kernel.invoke("informacao_pokemon", "Bulbasaur"))

```

## 📚 Recursos e Referências
- 🔗 [Documentação oficial do Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
- 🔗 [Introdução ao Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview)
- 📄 **Slides de Apoio:** *Apresentação sobre API e Semantic Kernel.pptx*

## 🚀 Fechando com Chave de Ouro
O Azure OpenAI é brabo pra criar apps com IA: dá pra fazer chat, gerar texto, imagens e até trabalhar com áudio. O Semantic Kernel entra pra deixar tudo mais top, com agentes de IA e funções automáticas. Com isso, tu consegue criar umas aplicações maneiras sobre o universo Pokémon, e ainda impressionar o prof na entrega do trabalho. Agora estou pronto para meter a mão na massa agora! 😎 🤖🔥

