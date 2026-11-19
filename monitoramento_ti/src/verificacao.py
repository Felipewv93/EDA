def verificar_dados(df):

    print(f'\nIniciando verificação dos dados...')

    try:
        print("\nValores nulos:")
        print(df.isnull().sum())

        print("\nDuplicados:")
        print(df.duplicated().sum())

        print("\nTipos de serviço:")
        print(list(df["metric_type"].unique()))

        print("\nTipos de dados:")
        print(df.dtypes)

    except Exception as e:
        print("Erro na verificação dos dados: ", e)