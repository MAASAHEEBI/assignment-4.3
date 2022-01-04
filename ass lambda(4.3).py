'''Write a Python program to square the elements of a list using map() function.

Sample List: [4, 5, 2, 9]
Square the elements of the list:

[16, 25, 4, 81]'''

n=int(input('how many numbers are there in a list: '))
l=[]
for i in range(n):
    m=int(input('enter number to be squared : '))
    l.append(m)
print('Given elements of the list:',l)
print('after squaring: ',end='')
print(list(map((lambda x:x**2),l)))
