import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do cliente Azure OpenAI com variáveis de ambiente
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

# Função para interagir com a IA no modo de chat
def conversar_com_ia():
    # Mensagens enviadas para a IA
    mensagens = [{"role": "user", "content": "Me conta sobre o Charmander"}]

    # Requisição para obter resposta da IA
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=mensagens,
        temperature=0.7
    )

    # Exibindo a resposta da IA
    print("Resposta da IA sobre Charmander:")
    print(response["choices"][0]["message"]["content"])

# Função para gerar texto sobre um Pokémon
def gerar_texto_sobre_pokemon():
    # Exemplo de prompt para gerar texto sobre Bulbasaur
    prompt = "Me conta sobre o Pokémon Bulbasaur"

    # Requisição para obter uma resposta de texto
    response = client.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        prompt=prompt,
        max_tokens=150,
        temperature=1.0,
        n=1
    )

    # Exibindo a resposta gerada
    print("Texto gerado sobre o Bulbasaur:")
    print(response["choices"][0]["text"].strip())

# Função para gerar uma imagem de um Pokémon misturado
def gerar_imagem_pokemon():
    # Prompt para criar uma imagem de um Pokémon híbrido (Bulbasaur + Charmander)
    prompt = "Um Pokémon misturado entre Bulbasaur e Charmander, com a chama de Charmander e as folhas de Bulbasaur"

    # Requisição para gerar a imagem
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    # Exibindo o URL da imagem gerada
    print("Imagem gerada do Pokémon híbrido:")
    print(response["data"][0]["url"])

# Função principal para escolher o que fazer
def main():
    print("Escolha uma opção:")
    print("1. Conversar sobre o Charmander")
    print("2. Gerar texto sobre o Pokémon Bulbasaur")
    print("3. Criar uma imagem de um Pokémon misturado")

    escolha = input("Digite o número da opção: ")

    if escolha == "1":
        conversar_com_ia()
    elif escolha == "2":
        gerar_texto_sobre_pokemon()
    elif escolha == "3":
        gerar_imagem_pokemon()
    else:
        print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
