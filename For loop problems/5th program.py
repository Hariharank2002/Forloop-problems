for num in range(2,10):
    value=False

    for i in range(2,num):
        if num%i ==0:
            value=True
            break
    if not value:
        print(num)