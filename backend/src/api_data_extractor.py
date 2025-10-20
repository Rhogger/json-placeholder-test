import pandas as pd
import requests

print("--- Tutorial: Obtendo Dados de API (GET) e Pandas ---")
print("--------------------------------------------------\\n")

# Endpoint da API para obter a lista de usuários
# JSONPlaceholder simula um servidor REST com dados de exemplo.
users_api_url = "https://jsonplaceholder.typicode.com/users"
print(f"1. Tentando obter dados de usuários do endpoint: {users_api_url}")

try:
    # A função requests.get() envia uma requisição HTTP GET para a URL.
    # GET é usado para recuperar informações do servidor.
    response_get = requests.get(users_api_url)
    # Verificar o status da resposta HTTP
    # Um status_code de 200 significa que a requisição foi bem-sucedida.
    if response_get.status_code == 200:
        print(" Requisição GET bem-sucedida! Status Code: 200 OK")
        # response.json() converte a resposta JSON da API em um objeto Python.
        # Neste caso, será uma lista de dicionários, onde cada dicionário é um usuário.aaaaa

        users_data = response_get.json()
        print(f" Total de {len(users_data)} usuários recebidos.")
        # Criar um DataFrame Pandas a partir da lista de dicionários.

        # Cada dicionário se torna uma linha, e as chaves dos dicionários se tornam as colunas.

        df_users = pd.DataFrame(users_data)
        print("\\n 2. DataFrame Pandas criado com sucesso:")
        print(df_users.head())  # Exibe as 5 primeiras linhas do DataFrame para inspeção.

        print(f"\\n Colunas no DataFrame: {df_users.columns.tolist()}")
        print(f" Formato do DataFrame (linhas, colunas): {df_users.shape}")

        # Exemplo de Manipulação de Dados com Pandas: Extrair a cidade do endereço.

        # O campo 'address' é um dicionário dentro do JSON de cada usuário.

        # Usamos .apply() para aplicar uma função lambda que extrai a chave 'city'.

        df_users["city"] = df_users["address"].apply(lambda x: x["city"])

        print("\\n 3. Coluna 'city' adicionada ao DataFrame, extraída do endereço:")

        print(df_users[["name", "city", "address"]].head())
        # Você pode salvar esses dados para uso posterior em ML, por exemplo:

        # df_users.to_csv('usuarios.csv', index=False)
        # print("\\n Dados salvos em 'usuarios.csv'")
        # Tratar outros códigos de status HTTP comuns
    elif response_get.status_code == 404:
        print(f" Erro 404: Recurso não encontrado. Verifique a URL: {users_api_url}")
    else:
        print(f" Erro na requisição GET. Status Code: {response_get.status_code}")
        print(f" Detalhes da resposta: {response_get.text}")
        # Capturar e tratar exceções relacionadas à conexão (e.g., sem internet, URL inválida)
except requests.exceptions.RequestException as e:
    print(f" Ocorreu um erro ao realizar a requisição GET: {e}")

    print("\\n" + "-" * 70 + "\\n")
