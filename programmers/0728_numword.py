def solution(s):
    num_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 
                'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0', }
    
    for num_key in num_dict.keys():
        if num_key in s:
            s = s.replace(num_key, num_dict.get(num_key))
        
    answer = int(s)
    return answer