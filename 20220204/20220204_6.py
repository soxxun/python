def calc(*parameters):
    raise NotImplementedError


try:
    calc(1,2,4,5,6)
except Exception as e:
    print("예외발생")