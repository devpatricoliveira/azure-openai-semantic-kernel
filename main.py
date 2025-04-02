import os
from openai import AzureOpenAI

# Certifique-se de que as variáveis de ambiente estão configuradas corretamente
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)

# Função para gerar imagem com DALL-E 3
def gerar_imagem_pokemon():
    prompt = "Um Pokémon misturado entre Bulbasaur e Charmander, com a chama de Charmander e as folhas de Bulbasaur"
    
    response = client.images.generate(
        model="dall-e-3",  # Nome do modelo de geração de imagens
        prompt=prompt,     # Descrição do que queremos gerar
        n=1,               # Número de imagens a serem geradas
        size="1024x1024"   # Tamanho da imagem gerada
    )

    # Exibe a URL da imagem gerada
    if response and 'data' in response and len(response['data']) > 0:
        image_url = response['data'][0]["url"]
        print(f"Imagem gerada: {image_url}")
    else:
        print("Erro ao gerar a imagem!")

# Chama a função para gerar a imagem
if __name__ == "__main__":
    gerar_imagem_pokemon()
