import pandas as pd

def carregar_dados():

    print(f'\nCarregando dados...')

    try:
        df = pd.read_csv("data/monitoramento_ti_infra.csv")
        print("Dados carregados com sucesso!")
        return df

    except Exception as e:
        print("Erro ao carregar dados", e)
