import hashlib
import os


hashDic = {}

def HashGenerationFunc() :
    filePath = input("Hash값을 알고자하는 파일 경로를 입력하세요 : ")
    with open(filePath, mode='rb') as file:
       data=file.read()
       print("MD5 : " + hashlib.md5(data).hexdigest())
       print("SHA-1 : " + hashlib.sha1(data).hexdigest())
       print("SHA-256 : " + hashlib.sha256(data).hexdigest())

def makingDictonary(searchPath) :
    for path, direct, files in os.walk(searchPath) :
        for file in files:
            filePath = os.path.join(path,file)
            with open(filePath,mode='rb') as file :
                data = file.read()
                hashDic[filePath]=[hashlib.md5(data).hexdigest(),hashlib.sha1(data).hexdigest(),hashlib.sha256(data).hexdigest()]

def findSearchHash(Hashvalue):
    for key, value in hashDic.items():
        if Hashvalue == value :
            return key
    return "There is no such file"

def HashSearchFunc() :
    searchPath = input("검색하고자 하는 파일의 경로를 입력하세요(입력한 경로부터 모든 하위 디렉토리를 검색합니다.) : ")
    searchHash = input("찾고자 하는 파일의 해쉬값을 입력하세요(MD5,SHA1,SHA256 순서로 입력/띄어쓰기로 구분) : ").split()
    for i in range(0,3):
       searchHash[i] = searchHash[i].lower()

    print(searchHash)
    makingDictonary(searchPath)
    print(findSearchHash(searchHash))


if __name__ == '__main__':
    opt = int(input("어떤 기능을 이용하겠습니까?(해쉬값생성 : 0, 해쉬셋 검색 : 1)"))
    if opt == 0:
        HashGenerationFunc()
    elif opt == 1:
        HashSearchFunc()

