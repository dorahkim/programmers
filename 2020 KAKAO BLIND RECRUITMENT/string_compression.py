# 문자열 압축

def solution(s):
    lns = len(s)
    answer = [lns]
    
    for i in range(1, lns):
        prev = None
        j = 0
        cnt = 0
        lst = []
        while j + i <= lns:
            if prev != s[j:j + i]:
                lst.append(cnt)
                prev = s[j:j + i]
                cnt = 1
            else:
                cnt += 1
            j += i
        lst.append(cnt)
        
        ln = lns - j + i * (len(lst) - 1)
        for j in lst:
            if j > 1:
                ln += len(str(j))
        
        answer.append(ln)
        
    return min(answer)
