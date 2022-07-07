from typing import List
from CrowdScienceLab import colors
from Utils import drawGraph


NODE_N = 0
matrix: List = []

if __name__ == '__main__':
    NODE_N = int(input(f"\nPlease enter the {colors.BOLD}number of node{colors.ENDC} in the graph.\n"))
    print("Please enter the adjacent matrix")
    matrix = [list(map(int, input().split())) for i in range(NODE_N)]
    drawGraph(matrix)
    # input the starting points
    starts = input('Please enter the starting points ( 0 – %i ) nums, divided by \',\' :\n' % (NODE_N - 1))
    starts = starts.strip()
    starts_str = starts.split(',')
    li = []
    for S in starts_str:
        S = S.strip()
        S = int(S)
        li.append(S)

    users = li
    threshold = float(input('Please enter the threshold. This shall be a float num in [0..1]. \n'))
    # record friend relationship in a dic
    friends_all = {}
    for i in range(NODE_N):
        friends_ind = []
        for j in range(NODE_N):
            edge = matrix[i][j]
            if edge == 1:
                friends_ind.append(j)
        friends_all[i] = friends_ind

    # cascade
    rnd = 0
    print('Beginning user: ', end='')
    print(users)
    while True:
        rnd += 1
        new_users = []
        for i in range(NODE_N):
            if i in users:
                continue
            friends_ind = friends_all[i]
            friends_users = [j for j in friends_ind if j in users]
            influ = len(friends_users) / len(friends_ind)
            if influ >= threshold:
                new_users.append(i)
        users += new_users
        if not new_users:
            print('Finished')
            break
        print(f"New users in the{colors.BOLD}{colors.WARNING} {rnd} th {colors.ENDC}round: ", end='')
        print(new_users)

    '''
    Please enter the number of node in the graph.
    17
    Please enter the adjacent matrix
    0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0
    1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0
    0 0 0 1 0 0 1 1 0 0 0 0 0 0 0 0 0
    0 1 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0
    0 0 0 1 1 0 0 1 1 1 0 0 0 0 0 0 0
    0 0 0 0 1 0 1 0 0 1 0 0 0 1 0 0 0
    0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 0
    0 0 0 0 0 0 1 1 1 0 0 1 0 0 0 0 0
    0 0 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0
    0 0 0 0 0 0 0 0 0 1 1 0 1 0 1 1 0
    0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 1
    0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 1
    0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 1 0
    0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1
    0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 0
    Please enter the starting points ( 0 – 16 ) nums, divided by ',' :
    7, 10, 12
    Please enter the threshold. This shall be a float num in [0..1]. 
    .3
    Beginning user: [7, 10, 12]
    New users in the 1 th round: [4, 11, 13, 14, 16]
    New users in the 2 th round: [3, 6, 9, 15]
    New users in the 3 th round: [5, 8]
    New users in the 4 th round: [1]
    New users in the 5 th round: [0, 2]
    Finished
    
    Process finished with exit code 0
    
    '''