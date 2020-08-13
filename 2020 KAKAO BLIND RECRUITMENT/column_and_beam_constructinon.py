# 기둥과 보 설치
# 11points

def solution(n, build_frame):
    column = {}
    row = {}
    
    def validColumn(x, y):
        #바닥 위
        if y == 0:
            return True
        #다른 기둥 위에 있을 때
        elif (x, y - 1) in column:
            return True
        #보의 한쪽 끝 위에 있을 때1
        elif (x, y) in row:
            return True
        #보의 한쪽 끝 위에 있을 때2
        elif (x - 1, y) in row:
            return True
        return False
    
    def validRow(x, y):
        #한쪽 끝이 기둥 위에 있을 때1
        if (x, y - 1) in column:
            return True
        #한쪽 끝이 기둥 위에 있을 때2
        elif (x + 1, y - 1) in column:
            return True
        #양쪽 끝이 보일 때
        elif (x - 1, y) in row and (x + 1, y) in row:
            return True
        return False
    
    for x, y, a, b in build_frame:        
        if x < 0 or y < 0:
            continue
            
        #build
        if b == 1:
            #column
            if a == 0:
                if y >= n:
                    continue
                if validColumn(x, y):
                    column[(x, y)] = 1
            #row
            else:
                if x >= n or y == 0:
                    continue
                if validRow(x, y):
                    row[(x, y)] = 1                
        #remove
        else:
            #column
            if a == 0:
                if not (x, y) in column:
                    continue
                del column[(x, y)]
                #지지하고 있는 기둥이 있을 때
                if (x, y + 1) in column and not validColumn(x, y + 1):
                    column[(x, y)] = 1
                    continue
                #지지하고 있는 보가 있을 때1
                if (x, y + 1) in row and not validRow(x, y + 1):
                    column[(x, y)] = 1
                    continue
                #지지하고 있는 보가 있을 때2
                if (x - 1, y + 1) in row and not validRow(x - 1, y + 1):
                    column[(x, y)] = 1
                    continue
            #row
            else:
                if not (x, y) in row:
                    continue
                del row[(x, y)]
                #지지하고 있는 기둥이 있을 때1
                if (x, y) in column and not validColumn(x, y):
                    row[(x, y)] = 1
                    continue
                #지지하고 있는 기둥이 있을 때2
                if (x + 1, y) in column and not validColumn(x + 1, y):
                    row[(x, y)] = 1
                    continue
                #양 옆이 보일 때1
                if (x - 1, y) in row and not validRow(x - 1, y):
                    row[(x, y)] = 1
                    continue                    
                #양 옆이 보일 때2    
                if (x + 1, y) in row and not validRow(x + 1, y):
                    row[(x, y)] = 1
                    continue             
                
    answer = []
    for key in column.keys():
        answer.append([key[0], key[1], 0])
    for key in row.keys():
        answer.append([key[0], key[1], 1])
    return sorted(answer, key=lambda x:(x[0] * (n + 1) + x[1], x[2]))
