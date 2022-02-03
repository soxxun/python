# pyton I/O
# file handler
file = open('basic.txt', "w")  # overwrite
file.write("hello")
file.close()


file = open('basic.txt', "a")  # append
file.write("\npython")
file.close()

file = open('basic.txt', "r")  # read
print(file.read())
file.close()
print("--------------------------------")
# with 절로 변경
with open('basic.txt', "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(f"line = {line}",end="")

