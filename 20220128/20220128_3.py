# 재귀함수  - 실무에서는 잘 안씀...... why 가독성 떨어지고.. 속도가 떨어진다.
def fa(n):
    if n == 1:
        return 1
    return n * fa(n-1)


print("재귀함수 호출")
print(fa(5))
print("재귀함수 호출끝")

