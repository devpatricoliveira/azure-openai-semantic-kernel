import openai
import os
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Carregar configurações
with open("config.json") as config_file:
    config = json.load(config_file)

# Configurar a chave de API e o endpoint
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
api_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# Função para gerar uma resposta da IA
def obter_resposta(prompt):
    response = openai.Completion.create(
        engine=config["model"],
        prompt=prompt,
        temperature=config["temperature"],
        max_tokens=config["max_tokens"]
    )
    return response.choices[0].text.strip()

# Função principal
def main():
    prompt = "Qual Pokémon você escolhe? Bulbasaur, Charmander ou Squirtle?"
    print("Interagindo com a IA...\n")
    resposta = obter_resposta(prompt)
    print(f"IA diz: {resposta}\n")

if __name__ == "__main__":
    main()
