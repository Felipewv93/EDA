import matplotlib.pyplot as plt
import seaborn as sns


class Graficos():

    def gerar_histograma(df):

        sns.histplot(df["latency_ms"], kde=True)
        plt.title("Distribuição da Latência")
        plt.xlabel("Latência (ms)")
        plt.ylabel("Quantidade")
        plt.savefig("assets/histograma_latencia.png")
        plt.close()


    def gerar_boxplot(df):

        sns.boxplot(data=df, x="metric_type", y="cpu_usage_pct")
        plt.title("Uso de CPU por Tipo de Serviço")
        plt.xlabel("Tipo de serviço")
        plt.ylabel("Uso de CPU (%)")
        plt.savefig("assets/boxplot_cpu.png")
        plt.close()
        
        sns.boxplot(data=df, x="metric_type", y="memory_usage_gb")
        plt.title("Uso de Memória por Tipo de Serviço")
        plt.xlabel("Tipo de serviço")
        plt.ylabel("Uso de memória (GB)")
        plt.savefig("assets/boxplot_memoria.png")
        plt.close()


    def gerar_heatmap(df):

        correlacao = df[["cpu_usage_pct", "latency_ms"]].corr()
        
        sns.heatmap(correlacao, annot=True)
        plt.title("Correlação entre CPU e Latência")
        plt.savefig("assets/heatmap_correlacao.png")
        plt.close()


def gerar_graficos(df):

    print(f'\nGerando gráficos...')
    try:
        Graficos.gerar_histograma(df)
        Graficos.gerar_boxplot(df)
        Graficos.gerar_heatmap(df)
        print("Gráficos salvos nas pasta assets.")

    except Exception as e:
        print("Erro na geração de gráficos: ", e)
