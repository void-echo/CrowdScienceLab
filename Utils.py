from typing import List
import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt
from CrowdScienceLab import colors

def drawGraph(matrix: List[List[float]]):
    matrix = pd.DataFrame(data=matrix)
    G = nx.DiGraph(matrix)

    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == '__main__':
    NODE_N = int(input(f"\nPlease enter the {colors.BOLD}number of node{colors.ENDC} in the graph.\n"))
    print("Please enter the adjacent matrix")
    matrix = [list(map(int, input().split())) for i in range(NODE_N)]
    drawGraph(matrix)