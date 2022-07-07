from typing import List

from CrowdScienceLab import colors
from Utils import drawGraph

DEBUG = False
NODE_N: int = 0


# 求单个节点的聚集系数
# 聚集系数 = 等于所有与它相连的顶点之间所连的边的数量，
# 除以这些顶点之间可以连出的最大边数
def cluster(matrix, index) -> float:
    edges_to_neightbor = set()
    for i in range(0, NODE_N):
        if i != index:
            if matrix[i][index] == 1:
                edges_to_neightbor.add(i)
            if matrix[index][i] == 1:
                edges_to_neightbor.add(i)
    neighbor_n = len(edges_to_neightbor)  # 有多少个邻居
    if neighbor_n <= 1:
        return 0
    max_n = 2 * (neighbor_n * (neighbor_n - 1) / 2.0)  # 有向图，所以乘以 2
    edges_between_neighbors_n = 0
    for i in edges_to_neightbor:
        for j in edges_to_neightbor:
            if i != j and matrix[i][j] == 1 and i != index and j != index:
                edges_between_neighbors_n += 1
    return edges_between_neighbors_n * 1.0 / max_n


def cluster_list(matrix) -> List[float]:
    li = []
    for i in range(0, NODE_N):
        li.append(cluster(matrix, i))
    if DEBUG:
        print(li)
    return li


# 邻里重叠度 = 与A、B均为邻居的节点数 / 与节点A、B中至少一个为邻居的节点数
def overlap(matrix, i, j) -> float:
    if i == j:
        return 1.0
    wide = set()  # 与节点A、B中至少一个为邻居的节点数
    narrow = set()  # 与A、B均为邻居的节点数
    for k in range(0, NODE_N):
        times = 0
        if k != i:
            if matrix[i][k] == 1 or matrix[k][i] == 1:
                wide.add(k)
                times += 1
        if k != j:
            if matrix[j][k] == 1 or matrix[k][j] == 1:
                wide.add(k)
                times += 1
        if times >= 2:
            narrow.add(k)

    if wide == 0:
        return 0  # 如果两个节点都没有邻居，返回 0
    return len(narrow) * 1.0 / len(wide)


def print_overlaps(matrix):
    for i in range(0, NODE_N):
        for j in range(0, NODE_N):
            print(f"overlap of node {i} and {j} : {colors.BOLD}{overlap(matrix, i, j)}{colors.ENDC}")


if __name__ == '__main__':
    NODE_N = int(input(f"\nPlease enter the {colors.BOLD}number of node{colors.ENDC} in the graph.\n"))
    print("Please enter the adjacent matrix")
    matrix = [list(map(int, input().split())) for i in range(NODE_N)]
    drawGraph(matrix)
    li = cluster_list(matrix)
    for index, num in enumerate(li):
        print(f"cluster val of node {colors.BOLD}{index}{colors.ENDC} :%.2f" % num)
    print("*" * 20)
    print_overlaps(matrix)
    '''
    Result:
    
    Please enter the number of node in the graph.
    4
    Please enter the adjacent matrix
    0 1 1 0
    1 0 0 1
    1 1 0 1
    0 1 1 0
    cluster val of node 0 :0.50
    cluster val of node 1 :0.67
    cluster val of node 2 :0.67
    cluster val of node 3 :0.50
    ********************
    overlap of node 0 and 0 : 1.0
    overlap of node 0 and 1 : 0.25
    overlap of node 0 and 2 : 0.25
    overlap of node 0 and 3 : 1.0
    overlap of node 1 and 0 : 0.25
    overlap of node 1 and 1 : 1.0
    overlap of node 1 and 2 : 0.5
    overlap of node 1 and 3 : 0.25
    overlap of node 2 and 0 : 0.25
    overlap of node 2 and 1 : 0.5
    overlap of node 2 and 2 : 1.0
    overlap of node 2 and 3 : 0.25
    overlap of node 3 and 0 : 1.0
    overlap of node 3 and 1 : 0.25
    overlap of node 3 and 2 : 0.25
    overlap of node 3 and 3 : 1.0
    
    Process finished with exit code 0
    '''
