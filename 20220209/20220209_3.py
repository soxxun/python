# 성적처리 프로그램
# 1. 학생이름입력하고
# 2. 점수를 공백을 기준으로 순서대로(국영수) 입력한다. 100 100 100
# 3. 학생들의 평균과 총점을 구하고 석차도 구한다
# 4. 입력받는 학생수는 제한이 없음..(입력하는 사람 마음)

class Students:
    def __init__(self,name,kor,eng,math):  # 생성자
        self.total = 0
        self.avg = 0.0
        self.rank = 0
        pass
    def inputData(self):    # 데이터 입력
        inputdata = input("이름과 국영수를 공백을 기준으로 입력 : ")
        pass
    def processScore(self):
        pass    

class StudentsMsg:
    def __init__(self,studentsList):  # 학생객체 리스트를 갖는다
        self.slist = studentsList
    def setRank(self):  # 학생들 석차 기록 ( 공동 등수가 있는 경우도 고려)
        pass
    def displayRank(self):  # 성적순으로 학생 정보 출력
        pass
    
# a = StudentsMsg()
# a.inputData()
StudentsMsg().inputData()