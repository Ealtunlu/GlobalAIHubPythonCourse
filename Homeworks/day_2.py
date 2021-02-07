#Create a list and swap the second half of the list with the first half of the list and print the list on the screen.
list = [1,2,3,4,5,6,7,8,9,10]
e = len(list)
if e%2 == 0:
    e = e//2
    swapped_list = list[e:] + list[:e]
    print(swapped_list)
elif e%2 == 1:
    print("Odd Number Of Elements In List")
else:
    print("Wrong Usage")
#Ask the user to input a single digit integer to a variable 'n', then print out all of the even numbers from 0 to 'n'(including 'n')
n = int(input("Input single digit integer : " ))
if n%2==1:
     for i in range(0,n,2):
         print(i,end=" ")
print(n)
if n%2==0:
    print("Please input a single digit integer!")
