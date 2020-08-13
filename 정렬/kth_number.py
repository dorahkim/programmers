# K번째 수

import random
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new_arr = array[i - 1:j]
        while True:
            if k == 1:
                answer.append(min(new_arr))
                break
            pivot = random.choice(new_arr)
            small = []
            large = []
            same = 0
            for elm in new_arr:
                if elm == pivot:
                    same += 1
                elif elm < pivot:
                    small.append(elm)
                else:
                    large.append(elm)

            if len(small) + same >= k:
                if len(small) > k:
                    new_arr = small
                elif len(small) == k:
                    answer.append(max(small))
                    break
                else:
                    answer.append(pivot)
                    break
            else:
                new_arr = large
                k -= len(small) + same

    return answer
