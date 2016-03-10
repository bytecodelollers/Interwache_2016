#xoring with the counter gets the flag.

flag = "IVyN5U3X)ZUMYCs"
answer =""
count=0
for x in flag:
    answer+=chr(ord(x) ^count)
    count+=1
print answer
