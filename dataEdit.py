import os, re
class DataSet:
    def __init__(self, Path="./datas/nucc/"):
        self.filePath = Path

    def MakeDict(self, savePath='./datas/', dictName='Adict'):
        dirList = os.listdir(self.filePath)
        textFiles = []
        for dump in dirList:
            if(re.search('.txt',dump)):
                textFiles.append(self.filePath + dump)
        if(len(textFiles)==0):
            print("not Found text files.")
        else:
            import MeCab
            LT = MeCab.Tagger('-Owakati')
            dictWords = []
            print("Found {} text files.".format(len(textFiles)))
            
            for dump in textFiles:
                with open(dump, 'r', encoding='utf-8') as f:
                    temp = f.read().split('\n')
                    i = 0
                    for tmp in temp:
                        if(tmp[0]=='F' or tmp[0]=='M'):
                            i += 1
                            dictWords.append(tmp)
                        elif(tmp[0]!='＠'):
                            dictWords[i-1] += tmp
                    print(len(temp))
                    #if len(dictWords)==0:
                        #dictWords=LT.parse(temp)

DD = DataSet()
DD.MakeDict()