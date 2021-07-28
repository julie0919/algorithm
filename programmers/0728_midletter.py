def solution(s):
    answer = ''
    mid_index = len(s) // 2
    if len(s) % 2:
        answer = s[mid_index]
    else:
        answer = s[mid_index-1:mid_index+1]

    return answer