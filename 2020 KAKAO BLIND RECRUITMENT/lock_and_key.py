# 자물쇠와 열쇠
# 14 points

def solution(key, lock):
    
    rows = set([])
    cols = set([])
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 0:
                rows.add(i)
                cols.add(j)
    
    #Test 2, 4, 12: No 0 in lock
    if len(rows) == 0:
        return True
    
    #crop the lock
    lock = lock[min(rows):max(rows) + 1]
    for r in range(len(lock)):
        lock[r] = lock[r][min(cols):max(cols) + 1]
    
    for n in range(4):
        #find the match
        if len(key) >= len(lock) and len(key[0]) >= len(lock[0]):
            for i in range(len(key) + 1 - len(lock)):
                for j in range(len(key[0]) + 1 - len(lock[0])):
                    match = True
                    for k in range(len(lock)):
                        for l in range(len(lock[0])):
                            if key[i + k][j + l] == lock[k][l]:
                                match = False
                                break
                        if not match:
                            break
                    if match:
                        return True
        
        #rotation
        newkey = [[0 for i in range(len(key))] for j in range(len(key[0]))]
        for r in range(len(key)):
            for c in range(len(key[0])):
                if key[r][c] == 1:
                    newkey[c][len(key) - 1 - r] = 1
        key = newkey
    
    return False
