# word_list = input().split()
# req = 'UCPC'

# for i in range(len(word_list)):
#     if word_list[i][0] in req:
#         req = req.replace(word_list[i][0], '', 1)
# if req:
#     print('I hate UCPC')
# else:
#     print('I love UCPC')

# word = input()
# isucpc = ''
# for i in range(len(word)):
#     if word[i].isupper():
#         isucpc += word[i]

# if 'UCPC' in isucpc:
#     print('I love UCPC')
# else:
#     print('I hate UCPC')

word = input()
alp = ['U', 'C', 'P', 'C']
i = 0

for a in alp:
    if a in word:
        i += 1
        word = word[word.index(a) + 1:]
    else:
        print('I hate UCPC')
        break
if i == 4:
    print('I love UCPC')