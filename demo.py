englishcorpus =["is","a","boy"]
frenchcorpus =["est","une","garçon"]
spanishcorpus =["es","un", "niño"]
def findenglish(sentences):
    getrandomsplit = sentences.split()
    print(getrandomsplit)
    for i in getrandomsplit:
        if i in englishcorpus:
            t = 0
            break
        else:
            t=1
    if(t ==1):
        return 0;
    else:
        return 1
def findfrench(sentences):
    getrandomsplit = sentences.split()
    print(getrandomsplit)
    for i in getrandomsplit:
        if i in frenchcorpus:
            t = 0
            break
        else:
            t=1
    if(t ==1):
        return 0;
    else:
        return 1
def findspanish(sentences):
    getrandomsplit = sentences.split()
    print(getrandomsplit)
    for i in getrandomsplit:
        if i in spanishcorpus:
            t = 0
            break
        else:
            t=1
    if(t ==1):
        return 0;
    else:
        return 1
sentence ="Suraj is a boy"
if findenglish(sentence) ==1:
    print("english")
if findfrench(sentence)==1:
    print("french")
if findspanish(sentence)==1:
    print("spanish")
