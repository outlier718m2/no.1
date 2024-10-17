with open('D:\dump.sql', encoding='utf-8') as myfile:
    while True:
        txt = myfile.readline()
        #print(line)
        if 'CREATE TABLE' in txt:
            print(txt)
    #print("파일 끝에 도달함")
    print(txt)