import openai
import json
import os
from dotenv import load_dotenv
from semantic_kernel import SemanticKernel
load_dotenv() 
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
 def call_openai_api(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci",   
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Erro ao chamar a API do OpenAI: {e}")
        return None
 nio
def semantic_kernel_example():
    kernel = SemanticKernel()
    task = kernel.create_task("Gerar uma lista de 3 coisas para fazer amanhã.")
    
    print("Resultado do Semantic Kernel:")
    print(task)
 def main():
    print("Bem-vindo ao exemplo de integração com o Azure OpenAI e Semantic Kernel!")
  
    prompt = "Escreva um breve parágrafo sobre a importância da IA no futuro."
    print("Chamando a API do OpenAI...")
    result = call_openai_api(prompt)
    print(f"Resposta da API do OpenAI: {result}\n")

    # Exemplo de uso do Semantic Kernel
    print("Usando o Semantic Kernel...")
    semantic_kernel_example()

if __name__ == "__main__":
    main()
