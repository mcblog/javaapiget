import os
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
    with open(file, 'r') as rd_file:
        fs = open(file, "r")
        liness = fs.readline()
        liine = liness[:-1]
        print(liine)
        for line in rd_file.readlines():

            if "@RequestMapping("in line:
                f = open(r"./apiout.txt", 'a')
                f.write(line)
                f.close()
            if "@GetMapping("in line:
                f = open(r"./apiout.txt", 'a')
                f.write(line)
                f.close()
        rd_file.close()
    return line
if __name__ == '__main__':
    print("在代码中给path输入参数")
    path=""
    #path=sys.argv[1]
    for i,j in dealwith(path,".java").items():
    #print(i)
        print()
        findapi(j)
        f = open(r"./apiout.txt", 'a')
        f.write(findapi(j))
        f.close()


