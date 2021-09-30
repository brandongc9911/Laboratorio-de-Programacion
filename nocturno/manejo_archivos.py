with open('nocturno/archivo1.txt','r', encoding="utf-8")as data:
    d = data.readlines()
    
    for i in range(len(d)):
        print(d[i])