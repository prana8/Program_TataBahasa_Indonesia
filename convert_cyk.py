from rule_cnf import get_set_of_production
import re

T_Segitiga = {}
g = None
previousNode = None

def is_accepted(inputString):
    global T_Segitiga
    T_Segitiga.clear()
    prodRules = get_set_of_production()
    inputString = inputString.lower().split(" ")
    for i in range(1,len(inputString)+1):
        for j in range(i, len(inputString)+1):
            T_Segitiga[(i,j)] = []
    for i in range(len(inputString),0,-1):
        for j in range(1, i+1):
            if (j == j + len(inputString) - i):
                tempList = []
                for key, value in prodRules.items():
                    for val in value:
                        if (val == inputString[j-1] and key not in tempList):
                            tempList.append(key)
                T_Segitiga[(j, j + len(inputString) - i)] = tempList
            else:
                tempList = []
                resultList = []
                for k in range(len(inputString) - i):
                    first = T_Segitiga[(j,j+k)]
                    second = T_Segitiga[(j+k+1,j+len(inputString) - i)]
                    for fi in first:
                        for se in second:
                            if (fi + " " + se not in tempList):
                                tempList.append(fi + " " + se)
                for key, value in prodRules.items():
                    for val in value:
                        if (val in tempList and key not in resultList):
                            resultList.append(key)
                T_Segitiga[(j,j+len(inputString) - i)] = resultList
    for key,(value,inside) in enumerate(T_Segitiga.items()):
        print(value,inside)
    if "K" in T_Segitiga[(1, len(inputString))]:
        return 1
    else:
        return 0