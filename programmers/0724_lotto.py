def solution(lottos, win_nums):
    count = 0
    count_zero = lottos.count(0)
    
    for num in lottos:
        for win_num in win_nums:
            if num != 0 and num == win_num:
                count += 1

    if count_zero == 6:
        return [1, 6]
    elif count_zero == 0 and count == 0:
        return [6, 6]
        
    min_count = count
    max_count = count + count_zero

    max_rank = 7 - max_count
    
    if min_count > 0:
        min_rank = 7 - min_count
    else:
        min_rank = 6

    answer = [max_rank, min_rank]
    return answer