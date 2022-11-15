import os
import re
def pathread(filepath):
    patha= {}
    i=0
    for root, dirs, files in os.walk(filepath):
        patha[i]=root
        i=i+1
    return patha
def work(files):
    File_Name = {}
    i=0
    for files in os.listdir(files):
        File_Name[i]=files
        i=i+1
    return File_Name
def dealwith(path,ext):
    filedict={}
    a = pathread(path)
    s = 0
    for i in range(0, len(a)):
        for j in range(0, len(work(a[i]))):
            if ((os.path.splitext(str(work(a[i])[j]))[-1]) == ext):
                s = s + 1
                filedict[s] = a[i] + '/' + str(work(a[i])[j])
    return filedict
def findapi(file):
    f1 = open(file, 'r', encoding='utf-8')
    text = f1.read()
    f1.close()
    regex = r"[ ]*(@RequestMapping|@GetMapping)[(](\s*value\W*|[\"/]*)[^\"]*\"[)}]"
    matches = re.finditer(regex, text, re.MULTILINE)
    strs=''
    for matchNum, match in enumerate(matches, start=1):
        match = [x.strip('\n') for x in match.group()]
        strs = ''.join(match)
        strs=strs+'\n'
    return strs
if __name__ == '__main__':
    print("在path处填入java项目路径")
    path=""
    # path=sys.argv[1]
    for i,j in dealwith(path,".java").items():
        findapi(j)
        f = open(r"./apiout.txt", 'a')
        f.write()
        f.write(findapi(j))
        f.close()