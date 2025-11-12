# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Definição da função para gerar dados fictícios de vendas
def gera_dados(num_registros = 500):
    
    # Mensagem inicial indicando a quantidade de registros a serem gerados
    # Dados de linhas a serem gerados serão preenchidos no momento da chamada da função
    print(f"\nIniciando a geração de {num_registros} registros...")

    # Dicionário com produtos, suas categorias e preços
    produtos = {
        'Notebook Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Notebook': {'categoria': 'Eletrônicos', 'preco': 4500.00},
        'Mouse sem fio': {'categoria': 'Acessórios', 'preco': 250.00},
        'Mouse com fio': {'categoria': 'Acessórios', 'preco': 99.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 350.00},
        'Teclado Membrana': {'categoria': 'Acessórios', 'preco': 150.00},
        'Monitor 24"': {'categoria': 'Eletrônicos', 'preco': 900.00},
        'Monitor 27"': {'categoria': 'Eletrônicos', 'preco': 1300.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},   
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Cadeira Escritório': {'categoria': 'Móveis', 'preco': 800.00},
        'Mesa Gamer': {'categoria': 'Móveis', 'preco': 950.00},
        'Mesa Escritório': {'categoria': 'Móveis', 'preco': 600.00},
        'Headset Stereo': {'categoria': 'Acessórios', 'preco':  400.00},
        'Fone de Ouvido': {'categoria': 'Acessórios', 'preco': 49.00},
        'Fone Bluetooth': {'categoria': 'Acessórios', 'preco': 150.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo GTX0000': {'categoria': 'Hardware', 'preco': 4500.00},
        'Placa de Vídeo RTX0000': {'categoria': 'Hardware', 'preco': 7000.00},
        'Processador X5': {'categoria': 'Hardware', 'preco': 120.00},
        'Processador X7': {'categoria': 'Hardware', 'preco': 350.00},
        'Memória RAM 8GB': {'categoria': 'Hardware', 'preco': 300.00},
        'Memória RAM 16GB': {'categoria': 'Hardware', 'preco': 550.00},
        'SSD 512GB': {'categoria': 'Hardware', 'preco': 350.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    # Cria uma lista apenas com os nomes dos produtos
    lista_produtos = list(produtos.keys())

    # Dicionário com cidades e seus respectivos estados
    cidades_estados = {
        'São Paulo': 'SP', 'Campinas': 'SP', 
        'Rio de Janeiro': 'RJ', 'Niteróio': 'RJ', 'Belo Horizonte': 'MG', 'Brasília': 'DF',
        'Porto Alegre': 'RS', 'Gramado': 'RS', 'Gravataí': 'RS',
        'Vitória': 'ES', 'Salvador': 'BA', 'Fortaleza': 'CE', 'Recife': 'PE', 'Olinda': 'PE',
        'Manaus': 'AM', 'Belém': 'PA', 'Goiânia': 'GO', 'Anápolis': 'GO',
        'Curitiba': 'PR', 'Londrina': 'PR', 'Maringá': 'PR', 'Florianópolis': 'SC', 'Joinville': 'SC',
        'Cuiabá': 'MT', 'Campo Grande': 'MS', 'São Luís': 'MA', 'Teresina': 'PI',
        'João Pessoa': 'PB', 'Campina Grande': 'PB', 'Aracaju': 'SE', 'Maceió': 'AL',
        'Natal': 'RN', 'Macapá': 'AP', 'Rio Branco': 'AC', 'Palmas': 'TO', 'Boa Vista': 'RR'
    }

    # Cria uma lista apenas com os nomes das cidades
    lista_cidades = list(cidades_estados.keys())

    # Lista para armazenar os registros de vendas
    dados_vendas = []

    # Define a data inicial dos pedidos
    data_inicial = datetime(2025, 1, 1)

    # Loop para gerar os registros de vendas
    for i in range(num_registros):
        
        # Seleciona aleatoriamente um produto
        produto_nome = random.choice(lista_produtos)

        # Seleciona aleatoriamente uma cidade
        cidade = random.choice(lista_cidades)

        # Gera uma quantidade de produtos vendida entre 1 e 7
        quantidade = np.random.randint(1, 8)

        # Calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))

        # Aplicar regra de desconto para alguns produtos
        # Desconto sazonal, aplica desconto aleatório de até 10%
        if produto_nome in ['Mouse sem fio', 'Teclado Mecânico', 'Cadeira Gamer', 'Headset 7.1'] and (data_pedido >= datetime(2025, 2, 1) and data_pedido < datetime(2025, 4, 1)):
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        # Adiciona um registro de venda à lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })
    
    # Mensagem final indicando que a geração terminou
    print("Geração de dados concluída.\n")

    # Retorna os dados no formato de DataFrame
    return pd.DataFrame(dados_vendas)