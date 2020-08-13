# 키패드 누르기

def solution(numbers, hand):
    left = [3, 0]
    right = [3, 2]
    answer = ''
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = [int((n - 1) / 3), 0]
        elif n in [3, 6, 9]:
            answer += 'R'
            right = [int((n - 3) / 3), 2]
        else:
            button = [int((n - 2) / 3), 1]
            if n == 0:
                button = [3, 1]
            llen = abs(button[0] - left[0]) + abs(button[1] - left[1])
            rlen = abs(button[0] - right[0]) + abs(button[1] - right[1])
            if llen < rlen:
                answer += 'L'
                left = button
            elif llen > rlen:
                answer += 'R'
                right = button
            elif hand == 'left':
                answer += 'L'
                left = button
            else:
                answer += 'R'
                right = button
    return answer
