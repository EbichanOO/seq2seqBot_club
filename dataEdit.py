import os, re
class DataSet:
    def __init__(self, Path="./datas/nucc/"):
        self.filePath = Path #ファイルのパス
        self.textField = [] #文章のフィールド
        self.sentences = [] #文章

    def MakeDict(self, savePath='./datas/', dictName='dict'):
        dirList = os.listdir(self.filePath)
        textFiles = []
        for dump in dirList:
            if(re.search('.txt',dump)):
                textFiles.append(self.filePath + dump)
        if(len(textFiles)==0):
            print("not Found text files.")
        else:
            import MeCab
            dictWords = []
            print("Found {} text files.".format(len(textFiles)))
            
            tasknum = 0
            for dump in textFiles:
                with open(dump, 'r', encoding='utf-8') as f:
                    temp = f.read().split('\n')
                
                i = 0
                for tmp in temp:
                    if(len(tmp)!=0):
                        if(tmp[0]=="F" or tmp[0]=="M" or tmp[0]=="%"): #1返答1行に分離
                            i += 1
                            sent = []
                            if( len(tmp.split("：")) == 2):
                                _, sent = tmp.split("：")
                            elif(len(tmp.split("：")) == 1):
                                sent = tmp.split("：")[3:]
                            self.sentences.append(sent)
                        elif(tmp[0]!='＠'):
                            self.sentences[i-1] += tmp
                for a_sentence in self.sentences:
                    try:
                        dictWords.append(MeCab.Tagger('-Owakati').parse(a_sentence.strip("\n")).split(" "))
                    except:
                        pass
                tasknum += 1
                print("Do " + str(tasknum)+"/"+str(len(textFiles)) + " mecab process")
                i = 0
            print("read end")
            listWords = list(set(dictWords))
            print(len(listWords))

DD = DataSet()
DD.MakeDict()