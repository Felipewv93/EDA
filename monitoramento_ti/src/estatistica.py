def calcular_estatisticas(df):

    print(f'\nIniciando análise dos dados...')

    try:
        print("\nLATÊNCIA")
        print("Média:", df["latency_ms"].mean().round(2))
        print("Mediana:", df["latency_ms"].median().round(2))
        print("Desvio padrão:", df["latency_ms"].std().round(2))
        print("Mínimo:", df["latency_ms"].min().round(2))
        print("Máximo:", df["latency_ms"].max(),round(2))

        print("\nCPU")
        print("Média:", df["cpu_usage_pct"].mean().round(2))
        print("Mediana:", df["cpu_usage_pct"].median().round(2))
        print("Desvio padrão:", df["cpu_usage_pct"].std().round(2))
        print("Mínimo:", df["cpu_usage_pct"].min().round(2))
        print("Máximo:", df["cpu_usage_pct"].max().round(2))

        print("\nMEMÓRIA")
        print("Média:", df["memory_usage_gb"].mean().round(2))
        print("Mediana:", df["memory_usage_gb"].median().round(2))
        print("Desvio padrão:", df["memory_usage_gb"].std().round(2))
        print("Mínimo:", df["memory_usage_gb"].min().round(2))
        print("Máximo:", df["memory_usage_gb"].max().round(2))

    except Exception as e:
        print("Erro ao analisar dados: ", e)
