import sys
import numpy as np
from typing import List
from CrowdScienceLab import colors

NODE_N = 0
matrix: List = []       # use matrix as static var.
mat2: List = []

def containsOdd(G, n):
    # -1: undefined
    # 0: RED
    # 1: GREEN
    colorArr = [-1] * n
    colorArr[0] = 1
    Q = [0]
    while Q:
        u = Q.pop(0)
        for v in range(n):
            if G[u][v] and colorArr[v] == -1:
                colorArr[v] = 1 - colorArr[u]
                Q.append(v)
            elif G[u][v] and colorArr[v] == colorArr[u]:
                return True
    return False

"""
use recursion to designate a group, 
in which all nodes have an edge of "1" inbetween
"""
def cluster(i, group):
    group.append(i)
    for j in range(len(matrix[i])):
        if j not in group:
            if matrix[i][j] == 1:
                cluster(j, group)
    return group


"""
该程序不仅可以判断是否含有负向边圈，
还可以判断一个图是否是平衡的。
"""
if __name__ == '__main__':
    NODE_N = int(input(f"\nPlease enter the {colors.BOLD}number of node{colors.ENDC} in the graph.\n"))
    print("Please enter the adjacent matrix")
    matrix = [list(map(int, input().split())) for i in range(NODE_N)]
    groups = []

    # 填充：以正边组成的连通分量
    t, begin = 0, 0
    li = [i for i in range(NODE_N)]
    while True:
        groups.append([])
        groups[t] = cluster(begin, groups[t])
        for j in groups[t]:
            li.remove(j)
        if not li:
            break
        begin = li[0]
        t += 1
    has_neg_edge = False
    for group in groups:
        for a in range(len(group)):
            i = group[a]
            if not has_neg_edge:
                for j in group[a + 1:]:
                    if matrix[i][j] == -1:
                        has_neg_edge = True
                        break
    if has_neg_edge:
        print(f"{colors.WARNING} 以正边组成的连通分量中，含有负边。因此该网络不是平衡的。 {colors.ENDC}")
        sys.exit(0)

    # 降维（实际上只是进行了缩点），并且将 -1 的边改成 1.
    mat2 = np.zeros((t+1, t+1))
    for i in range(len(groups)):
        group = groups[i]
        for j in range(i + 1, len(groups)):
            nxt = groups[j]
            edgeExist = False
            for node1 in group:
                if edgeExist:
                    break
                for node2 in nxt:
                    if matrix[node1][node2] == -1:
                        mat2[j][i], mat2[i][j] = 1, 1
                        edgeExist = True
                        break

    if not containsOdd(mat2, t):
        print("This Graph does not contain a odd nagtive circle.\nGraph is balanced.")
    else:
        print(f"This Graph does {colors.WARNING}contain{colors.ENDC} a odd nagtive circle.\nGraph is not balanced.")

    '''
    Result:
    
    Example 1:
    Please enter the number of node in the graph.
    15
    Please enter the adjacent matrix
    0  1  1  0  0  0  0  0  0  0  0  0  0  0  0
    1  0  1 -1  1  0  0  0  0  0  0  0  0  0  0
    1  1  0  0  0 -1  0  0  0  0  0  0  0  0  0
    0 -1  0  0  0  0 -1  0 -1  0  0  0  0  0  0
    0  1  0  0  0 -1  0  0  0  0  0  0  0  0  0
    0  0 -1  0 -1  0  0  1  0  0 -1  0  0  0  0
    0  0  0 -1  0  0  0  0  0  0  0  1  0  0  0
    0  0  0  0  0  1  0  0  0  0 -1  0  0  0  0
    0  0  0 -1  0  0  0  0  0  0  0  1  0  0  0
    0  0  0  0  0  0  0  0  0  0  1  1  0  0  0
    0  0  0  0  0 -1  0 -1  0  1  0  0  1 -1  0
    0  0  0  0  0  0  1  0  1  1  0  0  1  0  0
    0  0  0  0  0  0  0  0  0  0  1  1  0  0  1
    0  0  0  0  0  0  0  0  0  0 -1  0  0  0 -1
    0  0  0  0  0  0  0  0  0  0  0  0  1 -1  0
    This Graph does not contain a odd nagtive circle.
    
    
    Example 2:
    Please enter the number of node in the graph.
    15
    Please enter the adjacent matrix
    0  1  1  0  0  0  0  0  0  0  0  0  0  0  0
    1  0  1 -1  1  0  0  0  0  0  0  0  0  0  0
    1  1  0  0  0 -1  0  0  0  0  0  0  0  0  0
    0 -1  0  0  0  0 -1  0 -1  0  0  0  0  0  0
    0  1  0  0  0 -1  0  0  0  0  0  0  0  0  0
    0  0 -1  0 -1  0  0  1  0  0 -1  0  0  0  0
    0  0  0 -1  0  0  0  0  0  0  0  1  0  0  0
    0  0  0  0  0  1  0  0  0  0 -1  0  0  0  0
    0  0  0 -1  0  0  0  0  0  0  0  1  0  0  0
    0  0  0  0  0  0  0  0  0  0 -1  1  0  0  0
    0  0  0  0  0 -1  0 -1  0 -1  0  0 -1 -1  0
    0  0  0  0  0  0  1  0  1  1  0  0  1  0  0
    0  0  0  0  0  0  0  0  0  0 -1  1  0  0 -1
    0  0  0  0  0  0  0  0  0  0 -1  0  0  0 -1
    0  0  0  0  0  0  0  0  0  0  0  0 -1 -1  0
    This Graph does contain a odd nagtive circle.
    Graph is not balanced.
    
    Process finished with exit code 0
    '''