cnt = 0
with open('D:\dump.sql', encoding='utf-8') as myfile:
    while True:
        line = myfile.readline()
        #print(line)
        cnt += 1
        if not line:
            break
    #print("파일 끝에 도달함")
    print("라인수" + str(cnt))
