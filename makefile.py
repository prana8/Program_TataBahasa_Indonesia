import re
with open('C:\\Users\\ryanp\\Documents\\Kampus\Matakuliah\\SEMESTER 3\\TBO (teori bahasa dan otomata)\\FinalProjrct\\Final-Project-TBO-bakcup\\input_test.txt','r') as f:
    listinput = f.readlines()
    for x,value in enumerate(listinput):
        if(value[0]==' '):
            value= value[1:len(value)]
        clean = re.sub('\n','',value)
        listinput[x] = clean
with open('C:\\Users\\ryanp\\Documents\\Kampus\Matakuliah\\SEMESTER 3\\TBO (teori bahasa dan otomata)\\FinalProjrct\\Final-Project-TBO-bakcup\\input_test.txt','w') as f:
    for x in listinput:
        x = x+'\n'
        f.write(x)