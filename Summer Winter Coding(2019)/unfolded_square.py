# 멀쩡한 사각형
# 10 points

def solution(w,h):
    
    # caluculate common factor of two numbers
    def common_factor(w, h):
        if h % w == 0 or w % h == 0:
            return min(h, w)
        
        div = 1
        while pow(div, 2) <= w and pow(div, 2) <= h:
            if w % div == 0 and h % div == 0:
                rtn = div
            div += 1
        return rtn
    
    # calculate folded area of w * h rectangle
    def folded(w, h):
        #common factor
        c_factor = common_factor(w, h)
        if c_factor == 1:
            return w + h - 1
        else:
            return c_factor * folded(int(w / c_factor), int(h / c_factor))
    
    return w * h - folded(w, h)
