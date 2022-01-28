a = 100
def f(v):
    v = -500

def gf(v):
    global a
    a = -1500

f(a)
print(f"f(v) = {a}")

gf(a)
print(f"gf(v) = {a}")


list_a = [1,2,3]
def listF(li):
    li[0] = 100

listF(list_a)
print(f"list_a = {list_a}")
