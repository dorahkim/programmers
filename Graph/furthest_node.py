# 가장 먼 노드
# 11 points

import collections
def solution(n, edge):
    dic = collections.defaultdict(list)
    for s, e in edge:
        dic[s - 1].append(e - 1)
        dic[e - 1].append(s - 1)
    
    been = [False for i in range(n)]
    q = [0]
    cnt = 0
    while len(q) > 0:
        newq = set()
        for node in q:
            been[node] = True
            for nxt in dic[node]:
                if not been[nxt]:
                    newq.add(nxt)
        q = [node for node in list(newq) if not been[node]]
        if len(q) == 0:
            break
        cnt = len(q)
    return cnt
