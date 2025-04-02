import os
from openai import AzureOpenAI
import json

# Carrega as configurações do arquivo config.json
with open('config.json') as config_file:
    config = json.load(config_file)

client = AzureOpenAI(
    azure_endpoint=config['api_endpoint'],
    api_key=config['api_key'],
    api_version=config['api_version']
)

def obter_informacao_pokemon(pokemon):
    messages = [{"role": "user", "content": f"Me conta sobre o {pokemon}"}]

    response = client.chat.completions.create(
        model=config['deployment_name'],
        messages=messages,
        temperature=0.7
    )
    
    return response["choices"][0]["message"]["content"]

# Exemplo de uso
pokemon = "Charmander"
info = obter_informacao_pokemon(pokemon)
print(info)
