from graph import carregar_grafo, encontrar_rota, desenhar_grafo
from clustering import carregar_entregas, aplicar_kmeans, plotar_clusters

def main():
    print("=== OTIMIZAÇÃO DE ROTAS COM IA ===")

    # Parte 1: Grafo e A*
    G = carregar_grafo("./data/mapa.csv")
    origem, destino = "Restaurante", "E"
    caminho, custo = encontrar_rota(G, origem, destino)
    print(f"Melhor rota de {origem} até {destino}: {caminho} (custo: {custo})")
    desenhar_grafo(G, caminho, salvar_em="./docs/grafo.png")

    # Parte 2: Clustering com K-Means
    df = carregar_entregas("./data/entregas.csv")
    df, kmeans = aplicar_kmeans(df, n_clusters=3)
    print("\nEntregas agrupadas por clusters:")
    print(df)
    plotar_clusters(df, kmeans, salvar_em="./docs/clusters.png")

if __name__ == "__main__":
    main()