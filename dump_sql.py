N = 53
with open('D:\dump.sql', encoding='utf-8') as myfile:
    head = [next(myfile) for x in range(N)]
print(len(head))
for l in head:
    print(l)



