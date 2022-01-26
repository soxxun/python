# list comprehension



print( [i for i in range(10)] )

list_a = [1,5,8,7,9,8,6,4,8,7]

over10_list_a = [i for i in list_a if i > 3]
print(over10_list_a)

dic_a = {
    1: 10, 2: 20, 3: 30, 4: 40
}
dic_a_key = [key for key,value in dic_a.items()]
dic_a_value = [value for key, value in dic_a.items()]

custom = [('a', 1, 100), ('b', 2, 300), ('c', 3, 500), ('d', 4, 600)]
custom2 = [['a', 1, 100], ['b', 2, 300], ['c', 3, 500], ['d', 4, 600]]

# for i, j, k in custom2:
#     print(f"custom i = {i} j = {j}  k={k}")

# list comprehension
[print(f"custom i = {i} j = {j}  k={k}") for i, j, k in custom2]

print([i for i, j, k in custom2])

print((i for i, j, k in custom2))
print(reversed([1,2,3,4,5]))

print( [i for i in (i for i, j, k in custom2)] )

print( [i for i in (i for i, j, k in custom2)] )

print( [ [i,j] for i,j,k in custom2 ] )

print( [ j*k for i,j,k in custom2 ] )

