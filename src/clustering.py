import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def carregar_entregas(arquivo_csv):
    return pd.read_csv(arquivo_csv)

def aplicar_kmeans(df, n_clusters=3):
    X = df[["x", "y"]]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X)
    return df, kmeans

def plotar_clusters(df, kmeans, salvar_em=None):
    plt.figure(figsize=(6,6))
    plt.scatter(df["x"], df["y"], c=df["Cluster"], cmap="viridis", s=100)
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
                c="red", marker="X", s=200, label="Centroides")
    for i, cliente in enumerate(df["Cliente"]):
        plt.text(df["x"][i]+0.1, df["y"][i]+0.1, cliente)
    plt.legend()
    plt.title("Agrupamento de Entregas (K-Means)")
    if salvar_em:
        plt.savefig(salvar_em)
    plt.show()