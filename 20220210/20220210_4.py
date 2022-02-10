# 성적처리 프로그램
# 1. 학생이름입력하고
# 2. 점수를 공백을 기준으로 순서대로(국영수) 입력한다. 100 100 100
# 3. 학생들의 평균과 총점을 구하고 석차도 구한다
# 4. 입력받는 학생수는 제한이 없음..(입력하는 사람 마음)

class Students:
    def __init__(self):  # 생성자
        self.name = ""
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.rank = 0
        self.total=0
        self.avg = 0.0

    def inputData(self):  # 데이터 입력
        self.inputdata = input("이름과 국영수를 공백을 기준으로 입력 : ").split()
        self.processScore()

    def processScore(self):
        self.name = self.inputdata[0]
        self.kor = self.inputdata[1]
        self.eng = self.inputdata[2]
        self.math = self.inputdata[3]
        for i in self.inputdata:
            try:
                self.total += int(i)
            except Exception as e:
                print(e)
        self.avg = self.total / 3

    def __str__(self):
        return f"name:{self.name}  kor:{self.kor} eng:{self.eng} math:{self.math} total:{self.total}  avg:{self.avg}"

class StudentsMsg:
    def __init__(self, studentsList):  # 학생객체 리스트를 갖는다
        self.slist = studentsList
    def setRank(self):  # 학생들 석차 기록 ( 공동 등수가 있는 경우도 고려)
        pass
    def displayRank(self):  # 성적순으로 학생 정보 출력
        pass

s = Students()
s.inputData()
print(s)

# a = StudentsMsg()
# a.inputData()
# StudentsMsg().inputData()