# 리스트를 복사할때는 copy() 메소드(함수)를 사용한다
list_a = [1,2,3,4,5]  # 원본
list_b = list_a.copy()
#  두 리스트를 출력
# list_b의 값을 변경해서 두 리스트를 출력

# 값을 복사한게 아니라... 두개를 동일하게 만든것..
list_aa = [1,2,3,4,5]      # 원본 
list_bb = list_aa
#  두 리스트를 출력
# list_bb의 값을 변경해서 두 리스트를 출력


# 값을 복사해서 같은건지... 주소(메모리 또느 참조)값을 같게 해서 같은건지 
# 어떻게 확인가능?
if (list_a == list_b) and (list_a is list_b):
    print(""" 
    두 리스트는 값이 같지만 
    list_a 와 list_b는 같은 값을 참조하고 
    있어서 한쪽인 변경되면 같이변경
          """)
elif (list_a == list_b) and (list_a is not list_b):
    print("""
        두 리스는 값만 같기때문에 한쪽이 변경되도 
        다른쪽은 변경되지 않는다
    """)
if list_a == list_b:
    if list_a is list_b:
        print(""" 
            두 리스트는 값이 같지만 
            list_a 와 list_b는 같은 값을 참조하고 
            있어서 한쪽인 변경되면 같이변경
                  """)
    else:
        print("""
                두 리스는 값만 같기때문에 한쪽이 변경되도 
                다른쪽은 변경되지 않는다
            """)



# 개선.......
# if 조건:
#    if 조건:
#        ..
#    else:


