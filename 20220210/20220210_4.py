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
        return self

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
        # return [self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank]

    def __str__(self):
        return f"name:{self.name}  kor:{self.kor} eng:{self.eng} math:{self.math} total:{self.total}  avg:{self.avg} rank:{self.rank}"

class StudentsMsg:
    def __init__(self, studentsList):  # 학생객체 리스트를 갖는다
        self.slist = studentsList
    def setRank(self):  # 학생들 석차 기록 ( 공동 등수가 있는 경우도 고려)
        pass
    def displayRank(self):  # 성적순으로 학생 정보 출력
        pass

# 학생객체를 저장
students = []
for i in range(2):
    students.append(Students().inputData())

#학생객체를 저장하고 있는 리스트중에 학생의 totla값을 기준으로 정렬
students.sort(key=lambda obj:obj.total, reverse=True)
# 객체의 맴버변수들의 값을 확인
# for i in students:
#     print(i)

#석차 셋팅
totalList = [i.total for i in students]
for idx,value in enumerate(totalList):
    students[idx].rank =  totalList.index(value)+1

# 학생객체의 정보를 다 출력해서 rank가 제대로 셋팅되었는지 확인
# rank순으로 정렬
students.sort(key =lambda obj : obj.rank)
for i in students:
    print(i)

# 숙제
# 1등학생의  이름은?


# #
# import random as rd
# scores = [58, 90, 76, 72, 60, 60, 41, 63, 96, 83, 47, 64, 82, 75, 45, 78, 79, 82, 48, 97] #rd.sample(range(40,100+1),20)
# print(scores)
# scores.sort(reverse=True)
# print(scores)
# rank = []
# for i in scores:
#     rank.append(scores.index(i)+1)
# print(rank)
#
#
# temp = [
#     ['a',70,20,30],
#     ['b',20,30,40],
#     ['c',50,10,30]
# ]
# from operator import itemgetter
# temp.sort(key=itemgetter(1))
# print(temp)
#
# temp2 = [
#     {'name':'a','kor':70, 'eng':20, 'math':30},
#     {'name':'b','kor':20, 'eng':30, 'math':40},
#     {'name':'c','kor':20, 'eng':10, 'math':30}
# ]
# temp2.sort(key=lambda a : (a['kor'], a['eng'] ) )
# print(temp2)