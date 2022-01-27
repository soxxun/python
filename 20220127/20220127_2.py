def test():
    a, b = 10, 20
    return a, b

def test2():
    a, b = 10, 20
    return [a, b]


returnv1, returnv2 = test()
print(f"{returnv1}  {returnv2}")

returnv3 = test2()
for i in returnv3:
    print(i)
