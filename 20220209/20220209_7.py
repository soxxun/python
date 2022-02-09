# class
# 만들기
# 사용하기(객체)
#   생성자
#   자동호출되는 내부 함수 __이름__()
#       __init__()
#       __str__()
#       __eq__()  비교연산자(객체끼리)

# 사용자 데이터를 처리하는 클래스
# 데이터 입력받기  파일명

# filename = input("file name : ")  # 함수
#
# with open(filename,"r") as f:  # 함수
#     lines = f.readlines()
#     for line in lines:
#         print(line)
#////////////////////////////////////////////////////
# 읽어들일 파일이 없으면 경고를 발생시키고 다시 입력 받기
# try ~ except.... while
class FileMg:
    def getFileName(self):
        return input("file name: ")

    def readFile(self,filename, encoding = 'utf-8'):
        with open(filename, 'r',encoding=encoding)as f:
            lines = f.readlines()
            for line in lines:
                print(line,end="")
#/////////////////////////////// 사용
# 5번시도하고 그래도 실패하면 프로그램 종료하기
MAXTRYCOUNT = 5
for i in range(MAXTRYCOUNT+1):
    try:
        f = FileMg()
        name = f.getFileName()
        # f.readFile(name,encoding='utf-8')
        f.readFile(name)
    except FileNotFoundError as e:
        print(f"{name} 파일이 없습니다.{i+1}번 시도했습니다.{MAXTRYCOUNT}번초과하면 종료됩니다.")
    except Exception as ec:
        print(ec)
        break
    else:
        break