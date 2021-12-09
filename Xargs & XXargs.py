#Xargs
'''
def student(*details) :
    print(details[0])

student(101,"Khalekuzzaman")
student(102,"Khalekuzzaman",3.50)
'''

'''
def add(*numbers) :       #
    sum = 0
    for number in numbers :
        sum = sum + number
        print(sum)


add(10,40)
add(10,40,80)
add(10,40,30,60)

'''
#XXargs
def student(**details) :    #dictionary moto kaj korbe
    print(details["name"])

student(id = 101,name = "kaochar")