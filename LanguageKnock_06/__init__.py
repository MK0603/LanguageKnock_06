class NClass():
    '''
    classdocs
    '''


    def __init__(self, ):
        '''
        Constructor
        '''

    #クラス内のメソッドのインデント:__init__と同じ段。一つ下げていた時にはAttributeErrorというエラーが出ていた

    #ブレークポイント用メソッド
    def printer(self,):
        print("b")
    def nGram(self,targetString ,n):
        nGramArray=[]
        for i in range(len(targetString)):
            nGramArray.append(targetString[i:i+n])
        return nGramArray

    def nGramWord(self,targetString,n):
        nGramWordArray=[]
        modify=targetString.split()
        for i in range(len(modify)):
            result=[]
            for j in range(i,min(i+n,len(modify))):
                result.append(modify[j])
            str=" ".join(result)
            nGramWordArray.append(str)
        return nGramWordArray


target_1="paraparaparadise"
target_2="paragraph"

SUM=[]
PROD=[]
DIFF=[]

NGramInst = NClass()
target_1nGram=NGramInst.nGram(target_1,2)
target_2nGram=NGramInst.nGram(target_2,2)

#和集合を出す
for i in range(len(target_1nGram)):
    for j in range(len(target_2nGram)):
        #target1の中から、和集合に追加
        if not target_1nGram[i] in SUM:
            SUM.append(target_1nGram[i])
        #target2の中から、和集合に追加
        if not target_2nGram[j] in SUM:
            SUM.append(target_2nGram[j])

#積集合を出す
for i in range(len(target_1nGram)):
    for j in range(len(target_2nGram)):
        if target_1nGram[i] in target_2nGram:
            #積集合なので、targetの1,2のどちらでも構わない
            if not target_1nGram[i] in PROD:
                PROD.append(target_1nGram[i])

#差集合を出す
for i in range(len(target_1nGram)):
    for j in range(len(target_2nGram)):
        if not target_1nGram[i] in target_2nGram:
            #積集合なので、targetの1,2のどちらでも構わない
            if not target_1nGram[i] in DIFF:
                DIFF.append(target_1nGram[i])

print(target_1+"にseが含まれるかどうか : ",end="")
print("se" in target_1nGram)
print(target_2+"にseが含まれるかどうか : ",end="")
print("se" in target_2nGram)
