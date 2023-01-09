import re
with open('C:\\Users\\ryanp\\Documents\\Kampus\Matakuliah\\SEMESTER 3\\TBO (teori bahasa dan otomata)\\FinalProjrct\\Final-Project-TBO-bakcup\\verb.txt','r') as f:
    input = f.readlines()
    for key,value in enumerate(input):
        if(value[0]==' '):
            value= value[1:len(value)]
        clean = re.sub('\n','',value)
        input[key] = clean
    print(*input,sep=' | ')