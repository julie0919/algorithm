# 시간초과
# word = input().upper()

# word_dict = {}

# for letter in word:
#     word_dict[letter] = word.count(letter)

# if list(word_dict.values()).count(max(word_dict.values())) > 1:
#     print('?')
# else:
#     print(max(word_dict, key=word_dict.get))


s = input().upper()
compress_s = list(set(s))

count_list = [s.count(i) for i in compress_s]

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(compress_s[count_list.index(max(count_list))])