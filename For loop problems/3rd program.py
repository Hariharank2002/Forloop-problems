num = int(input())
count=0
for i in range(1,num+1):
    if i%2 == 1 :
        count=count+i
    else:
        count=count-i
print(count)