from math import floor
from typing import List
import numpy as np
from CrowdScienceLab import colors, Utils

DEBUG = False
m, n = 0, 0
matrix: List[List[int]] = []
adj_mtx_of_result = []  # n × n adjacent matrix of vote result.


def get_voted_order_by_mid_rule(mtx: List[List[int]]) -> List[int]:
    result = []
    l = len(mtx[0])
    for _ in range(l):
        li = []
        for line in mtx:
            li.append(line[0])
        sorted_li = sorted(li)
        li_len = len(sorted_li)
        k = sorted_li[floor(li_len / 2)]
        result.append(k)
        for line in mtx:
            line.remove(k)
    return result

# x, y < n. x != y.
def __fill_adj(x, y, threshold):
    count = 0
    for i in range(m):
        if matrix[i].index(x) < matrix[i].index(y):
            count += 1
    if count >= threshold:
        adj_mtx_of_result[x][y] = 1


def fill_adj():
    threshold = (m + 1) / 2
    for i in range(n):
        for j in range(n):
            __fill_adj(i, j, threshold)


def check_cycle():
    mtx_power_n = np.matrix(adj_mtx_of_result) ** n
    if DEBUG:
        print(mtx_power_n)
    if np.count_nonzero(mtx_power_n) == 0:
        return False
    else:
        return True


def check_single_peak(li: List[float]) -> bool:
    l = len(li)
    if l <= 2:
        return True
    my_dic: dict[int, int] = {}
    for i in range(l):
        my_dic[li[i]] = i
    mode = 'down' if my_dic[1] < my_dic[0] else 'up'
    FLG = 0
    if mode == 'down':
        for i in range(1, l):
            if my_dic[i] >= my_dic[i - 1]:
                FLG += 1
        return True if FLG == 0 else False
    else:
        downing = False
        for i in range(1, l):
            if not downing:
                if my_dic[i] <= my_dic[i - 1]:
                    downing = True
                    FLG += 1
            else:
                if my_dic[i] >= my_dic[i - 1]:
                    return False
        return True

'''
按照一个特定的属性序，指出哪些投票是不满足单峰性质的，认为它们是“废票”，
剔除后按照中位项定理给出群体排序。
'''
if __name__ == '__main__':
    m = int(input(f"\nPlease enter the{colors.BOLD}{colors.WARNING} m {colors.ENDC} value.\n"))
    n = int(input(f"\nPlease enter the{colors.BOLD}{colors.WARNING} n {colors.ENDC} value.\n"))
    print("Please enter the vote matrix. \nEach line is a person's vote.")
    matrix = [list(map(int, input().split())) for i in range(m)]
    print(matrix)
    adj_mtx_of_result = np.zeros((n, n))
    fill_adj()
    has_cycle = check_cycle()
    if has_cycle:
        print(f"{colors.BOLD}{colors.WARNING}Condorcet paradox happened{colors.ENDC}. \nTrying to remove irrational votes.")
        __matrix = []
        for line in matrix:
            if not check_single_peak(line):
                __matrix.append(line)
        order = get_voted_order_by_mid_rule(__matrix)
        print(f"Vote result: {colors.WARNING}{colors.BOLD}{order}{colors.ENDC}")
    else:
        print(f"{colors.OKGREEN}{colors.BOLD}Vote OK.{colors.ENDC}")
        order = get_voted_order_by_mid_rule(matrix)
        print(f"Vote result: {colors.WARNING}{colors.BOLD}{order}{colors.ENDC}")
        pass
    """
    9 8 7 6 5 4 3 2 1 0
    2 3 1 4 5 6 0 7 8 9
    7 6 5 8 4 3 2 1 0 9
    3 4 2 5 6 1 7 0 8 9
    6 7 5 4 3 2 1 8 0 9
    2 1 3 0 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    3 4 5 2 1 6 7 0 8 9
    3 0 9 7 6 8 1 5 4 2
    9 7 5 8 1 3 2 0 4 6
    3 6 1 7 2 9 8 0 4 5
    2 9 0 6 8 3 1 5 7 4
    8 7 1 2 3 4 9 6 5 0 
    """
