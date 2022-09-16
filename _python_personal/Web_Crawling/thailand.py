
class ThailandPackage:
    def detail(self):
        print(f'[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만 원')

# 모듈 직접 실행
# - 실제로 모듈이나 패키지를 생성할 때에는 잘 동작하는지 test를 해 보아야 함

if __name__ == "__main__":
    print('thailand 모듈을 직접 실행')
    print('(이 문장은 모듈을 직접 실행할 때만 실행됨)')
    trip_to = ThailandPackage()
    trip_to.detail()
else: # 메인이 아닌 경우
    print('thailand 외부에서 모듈 호출')