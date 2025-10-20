import json  # Usaremos json.dumps para formatar o payload

import requests

print("--- Tutorial: Enviando Dados para API (POST) ---")
print("------------------------------------------------\\n")
# Endpoint da API para criar um novo post
# Para JSONPlaceholder, este endpoint simula a criação de um post.
posts_api_url = "https://jsonplaceholder.typicode.com/posts"
# Dados (payload) que queremos enviar para criar o novo post.
# Este é um dicionário Python que será convertido para JSON.
new_post_payload = {
    "title": "Título do Meu Novo Artigo de ML via API",
    "body": "Este é o conteúdo detalhado do artigo, demonstrando como é possível criar novos dados em um sistema externo usando requisições POST em Python. Isso é útil para alimentar bases de dados, criar tickets, etc.",
    "userId": 5,  # ID de um usuário existente (de 1 a 10 no JSONPlaceholder)
}

print(f"1. Tentando criar um novo post no endpoint: {posts_api_url}")
print(f" Dados a serem enviados (payload): {new_post_payload}")

try:
    # Definir os cabeçalhos HTTP.
    # 'Content-Type: application/json' informa ao servidor que o corpo da requisição é um JSON.
    headers = {"Content-type": "application/json; charset=UTF-8"}
    # A função requests.post() envia uma requisição HTTP POST.
    # POST é usado para enviar dados ao servidor para criar um novo recurso.
    # O parâmetro 'data' espera uma string. json.dumps() converte o dicionário Python para uma string JSON.
    # Alternativamente, você pode usar 'json=new_post_payload' e requests cuidará dos headers e da serialização.
    response_post = requests.post(
        posts_api_url, data=json.dumps(new_post_payload), headers=headers
    )
    # Ou de forma mais simples:
    # response_post = requests.post(posts_api_url, json=new_post_payload)

    # Verificar o status da resposta HTTP
    # Um status_code de 201 (Created) é o esperado para uma criação bem-sucedida.

    if response_post.status_code == 201:
        print(" Requisição POST bem-sucedida! Status Code: 201 Created")

        # A API geralmente retorna os dados do recurso recém-criado, incluindo um ID.

        created_post_data = response_post.json()
        print("\\n 2. Dados do post criado (resposta da API):")
        # json.dumps com indent=2 para uma visualização formatada.
        print(json.dumps(created_post_data, indent=2))
        print(f" O ID atribuído ao novo post é: {created_post_data.get('id')}")

        print(
            "\\n (Observação importante: O JSONPlaceholder simula a criação, mas não persiste o item em seu banco de dados real. Ele apenas retorna o objeto como se tivesse sido criado.)"
        )
        # Tratar outros códigos de status HTTP
    else:
        print(f" Erro na requisição POST. Status Code: {response_post.status_code}")

        print(f" Detalhes da resposta: {response_post.text}")

        # Capturar e tratar exceções de conexão
except requests.exceptions.RequestException as e:
    print(f" Ocorreu um erro ao realizar a requisição POST: {e}")
    print("\\n" + "-" * 70 + "\\n")
