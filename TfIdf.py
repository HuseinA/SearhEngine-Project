import math

def __init__(datalatih,qinp):
    data = datalatih
    idf=[0]*len(data[1])
    hasil = [0] * len(data)
    tfweight(data)
    WtdIdf(data,idf)
    norm(data)
    inp = querymath(qinp)
    eksinp(inp,idf)
    hasil=cossim(data, inp,hasil)
    return hasil


def tfweight(data):
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y]==0:
                data[x][y]=0
            else:
                data[x][y]=1+math.log10(data[x][y])
    return data

def WtdIdf(data,idf):
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y]!=0:
                idf[y]+=1

    for x in range(len(idf)):
        idf[x]=(math.log10(len(data)/idf[x]))

    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y]*=idf[y]
    return data

def norm(data):
    sigma = [0]*len(data)
    for x in range(len(data)):
        for y in range(len(data[x])):
            sigma[x]=sigma[x]+pow(data[x][y],2)
        for y in range(len(data[x])):
            if data[x][y]==0:
                data[x][y]=0
            else:
                data[x][y]=data[x][y]/math.sqrt(sigma[x])
    return data

#menghitung frekuensi input
def querymath(qinp):
    temp={}
    indata=qinp.split()
    for x in indata:
        for y in temp:
            if x == y:
                temp[y] += 1
                break
        else:
            temp[x]=(1)
    temp2=[]
    for x in temp:
        temp2.append(temp[x])
    return temp2

def eksinp(inp,idf):
    sigma=0
    for x in range(len(inp)):
        inp[x]=(1+math.log10(inp[x]))*idf[x]
    for x in range(len(inp)):
        sigma += pow(inp[x], 2)
    for x in range(len(inp)):
        inp[x] = inp[x]/ math.sqrt(sigma)
    return inp


def cossim(data,inp,hasil):
    for x in range(len(data)):
        for y in range(len(data[x])):
            hasil[x] += data[x][y]*inp[y]
    return hasil