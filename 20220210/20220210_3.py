class TV:
    serial = 0
    def __init__(self):
        TV.serial += 1
        self.serial = TV.serial

list_a = []
for i in range(10):
    list_a.append(TV())

for i in list_a:
    print(i.serial)