# 모의고사

def solution(answers):
    answer = [0, 0, 0]
    #1: 12345
    one = [1,2,3,4,5] * 8
    #2: 21232425
    two = [2,1,2,3,2,4,2,5] * 5
    #3: 3311224455
    thr = [3,3,1,1,2,2,4,4,5,5] * 4
    for i in range(len(answers)):
        if answers[i] == one[i % 40]:
            answer[0] += 1
        if answers[i] == two[i % 40]:
            answer[1] += 1
        if answers[i] == thr[i % 40]:
            answer[2] += 1
            
    mx = max(answer)
    rtn = []
    for i in range(len(answer)):
        if answer[i] == mx:
            rtn.append(i + 1)
    return rtn
