import re
def preprocess(dok,query):
    qi = query.split()
    qi = ' '.join(sorted(set(qi), key=qi.index))
    qi=qi.split()

    #tokenisasi & casefolding
    dok=re.sub(r'[\W\d]', ' ', dok)
    dok=dok.lower()
    dok=dok.split()

    #stopword
    tf=[]
    frekuen=[0]*len(qi)
    for x in range(len(dok)):
        for y in range(len(qi)):
            if dok[x] == qi[y]:
                tf.append(dok[x])
                frekuen[y]+=1
    return frekuen