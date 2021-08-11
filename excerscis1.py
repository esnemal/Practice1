

f=open("C:\\Python\\Code\\ex-1.txt","r+")
f1=open("C:\\Python\\Code\\ex-out.txt","w")
print(type(f))
print(type(f1))
for line in f:
    list=line.split(",")
    total=0
    for number in list:
        number=int(number)
        total=total+number
    f1.write(("sum:" + str(total)+"|")+line)
    print("sum:",total,"|", line)




def CountNum(a):
    count = 0
    for line in f:
        token1 = line.split(',')

        for number in token1:
            number=int(number)
            if number == a:
                count = count + 1

            else:
                count = count + 0

    return count

