
class VietnamPackage:
    def detail(self):
        print(f'[베트남 패키지 3박 5일] 다낭 효도 여행 60만 원')

# 여기에서도 외부 호출이 되는 것임
# 즉 패키지 내에서의 직접 호출이 아니라
# 패키지 내 if문을 작성한 해당 파일에서 실행해야만 직접 호출인 것

from travel import thailand
trip_to = thailand.ThailandPackage()
trip_to.detail()