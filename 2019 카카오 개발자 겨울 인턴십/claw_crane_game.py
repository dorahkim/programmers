# 크레인 인형뽑기 게임

def solution(board, moves):
    
    top = []
    for c in range(len(board[0])):
        for r in range(len(board)):
            if board[r][c] > 0:
                top.append(r)
                break
                
    q = []
    rtn = 0
    for move in moves:
        if top[move - 1] == len(board):
            continue
        q.append(board[top[move - 1]][move - 1])
        if len(q) > 1:
            if q[-1] == q[-2]:
                rtn += 1
                q = q[:-2]
    
        top[move - 1] += 1
    
    return rtn * 2
