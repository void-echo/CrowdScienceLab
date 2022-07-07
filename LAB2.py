from typing import List
from CrowdScienceLab import colors
from Utils import drawGraph


NODE_N = 0
matrix = None       # use matrix as static var.

# return list, list[i] = k means node i has k friends.
def friend_num() -> List[int]:
    li = []
    for i in range(0, NODE_N):
        k = 0
        for j in range(0, NODE_N):
            if i != j and matrix[i][j] == 1:
                k += 1
        li.append(k)
    return li

# This experiment studies the content of friendship paradox. 
# For moral considerations, one-side friends are not considered, 
# so undirected simple graph is adopted.

if __name__ == '__main__':
    NODE_N = int(input(f"\nPlease enter the {colors.BOLD}number of node{colors.ENDC} in the graph.\n"))
    print("Please enter the adjacent matrix")
    matrix = [list(map(int, input().split())) for i in range(NODE_N)]
    drawGraph(matrix)
    li = friend_num()
    up = 0
    for i in range(0, NODE_N):
        yes = 0
        aver = 0
        for j in range(0, NODE_N):
            if matrix[i][j] == 1 and i != j:
                aver += li[j]
                yes += 1
        aver /= yes
        if li[i] < aver:
            up += 1

    for i in range(0, NODE_N):
        print(f"Node\t{colors.BOLD}{i}{colors.ENDC}\thas\t{colors.BOLD}{li[i]}{colors.ENDC}\tfriends.")
    print(f"ratio that match the friendship paradox: {colors.BOLD}%.2f{colors.BOLD}" % (up / NODE_N))

    '''
    Result:
    
    Please enter the number of node in the graph.
    4
    Please enter the adjacent matrix
    0 1 1 0
    1 0 0 1
    1 1 0 1
    0 1 1 0
    Node	0	has	2	friends.
    Node	1	has	2	friends.
    Node	2	has	3	friends.
    Node	3	has	2	friends.
    ratio that match the friendship paradox: 0.50
    
    Process finished with exit code 0
    '''