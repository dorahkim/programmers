# 괄호 변환

def reverse_p(p):
    answer = ''
    for c in p:
        if c == '(':
            answer += ')'
        else:
            answer += '('
    return answer

def solution(p):
    #step1
    if p == '': return ''
    
    #step2
    balanced = -1
    if p[0] == '(':
        balanced = 1
    
    i = 1
    while i < len(p):
        if p[i] == '(': balanced += 1
        else:           balanced -= 1
        if balanced == 0:
            break
        i += 1
        
    right = True
    stack = []
    for elm in p[:i + 1]:
        if elm == '(':
            stack.append(elm)
        elif len(stack) == 0:
            right = False
            break
        else:
            stack.pop()
    
    #step3
    if right:
        return p[:i + 1] + solution(p[i + 1:])
        
    #step4
    else:
        return '(' + solution(p[i + 1:]) + ')' + reverse_p(p[1:i])
