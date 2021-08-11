head = list(input().split('_'))
title = ''
for i in head:
    title += i.upper() + '_'

print(title[:-1])