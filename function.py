list1=[34,56,78,32]
list2=[87,76,90,11]

def calculate_total(exp):
    total=0
    for i in exp:
        total=total+i
    return total

calculate1=calculate_total(list1)
calculate2=calculate_total(list2)



def calculate_triangle_Area(base,hight):
    return 1/2*(base* hight)
