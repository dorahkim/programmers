# [1차] 셔틀버스
# 11 points

import collections

def time_to_str(tme):
    return '%02d:%02d' % (int(tme / 60), tme % 60)

def solution(n, t, m, timetable):
    
    first_time = 9 * 60
    last_time = first_time + t * (n - 1)
    shuttle = collections.defaultdict(list)
    
    # arrange crews to shuttle bus
    for i in range(len(timetable)):
        hr, mn = timetable[i].split(':')
        tm = int(hr) * 60 + int(mn)
        if tm <= first_time:
            shuttle[first_time].append(tm)
        elif tm <= last_time:
            shuttle[first_time + (int((tm - 1 - first_time) / t) + 1) * t].append(tm)
    
    # sort crews by their arrival time
    for key in shuttle.keys():
        shuttle[key].sort()
    
    # make a waiting list
    shuttle_time = first_time
    waiting = []
    while True:
        if shuttle_time < last_time:
            if len(shuttle[shuttle_time]) + len(waiting) <= m:
                waiting = []
            else:
                waiting = (waiting + shuttle[shuttle_time])[m:]
        else:
            
            if len(shuttle[shuttle_time]) + len(waiting) < m:
                return time_to_str(last_time)
            else:
                return time_to_str((waiting + shuttle[shuttle_time])[m - 1] - 1)
        
        shuttle_time += t
