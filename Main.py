import preprocessing
import TfIdf
import os

content=[]
data=list(range(30))

allfiles=os.listdir("DATA/")
for filename in os.listdir('DATA/'):
    if filename.endswith('.txt'):
        with open(os.path.join('DATA/', filename),'r', encoding="latin-1") as f:
            content.append(f.read())

def printhasil(text,nilai):
    read=['','',0]
    temp=text.split('\n')
    read[0]=temp[0]
    temp.pop(0)
    read[1]=" ".join(temp)
    read[2]=nilai
    return read

def search():
    phasil={}
    a = 0
    for x in range(len(content)):
        data[x]=preprocessing.preprocess(content[x],queryinp)
    hasil=TfIdf.__init__(data,queryinp)
    for x in range(len(hasil)):
        phasil[x]=printhasil(content[x],hasil[x])
    for key,value in sorted(phasil.items(),key=lambda e: e[1][2],reverse=True):
        if value[2] > 0.002:
            a+=1
            print(value[0]+'\n'+value[1][:100]+'\n'+value[1][100:200]+'\n')
    print('got ' + str(a) + ' document')

queryinp=input("type here...\n")
search()
