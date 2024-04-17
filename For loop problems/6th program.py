# n =[1,2,3,4,5,6]
# s=sum(n)
# print(s)
# s1 = sum(n,13)
# print(s1)

n = [234]
x = 4
n_str = str(n[0])

output = []

for i in n_str:
    output.append(int(i))
print(output)

O=sum(output)
print(O*x)
