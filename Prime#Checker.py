number = int(input("Enter A Number: "))
flag = False
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            flag = True
            break
    if flag:
     print(number, "Not a prime Number")
     print(i,"times",number//i,"is",number)
    else:
     print(number, "Prime Number")