'''
Created on Apr 22, 2019

@author: Francesca
'''
'''
Created on Apr 9, 2019

@author: s271486
'''
list = []
num = int(input("How many numbers would you like on your list?"))

for n in range(num):
    numbers = int(input("Enter the numbers here:"))
    list.append(numbers)

def findsmallest(numberlist):
    smallest= numberlist[0]
    for value in numberlist:
        if value < smallest:
            smallest = value
    return smallest


print("Your smallest number is:" + str(findsmallest(list)))       
