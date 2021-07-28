def solution(n, lost, reserve):
    avail_student = n - len(lost)
    
    for lost_num in lost:
        front_lost = lost_num - 1
        back_lost = lost_num + 1
        
        if lost_num in reserve:
            avail_student += 1
            reserve.remove(lost_num)
        elif front_lost in reserve: 
            avail_student += 1
            reserve.remove(front_lost) 
        elif back_lost in reserve:
            avail_student += 1
            reserve.remove(back_lost)

    answer = avail_student
    return answer