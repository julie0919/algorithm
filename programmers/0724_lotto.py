def solution(lottos, win_nums):
    count = 0
    count_zero = 0
    max_rank = 0
    min_rank = 0

    for num in lottos:
        if num == 0:
            count_zero += 1

        for win_num in win_nums:
            if num == win_num:
                count += 1
        
    total_count = count + count_zero    

    if total_count == 2 or total_count == 1:
        max_rank = 5
    elif total_count == 0:
        max_rank = 6
    else:
        max_rank = 7 - total_count
    
    if count == 2 or count == 1:
        min_rank = 5
    elif count == 0:
        min_rank = 6
    else:
        min_rank = 7 - total_count

    answer = [max_rank, min_rank]
    return answer