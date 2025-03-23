#Print "Hello World!"
h="Hello World!"
for i in h:
    print(i)

#Print numbers from 1 to 10.
for i in range(1,11,1):
    print(i)

#Print even numbers between 1 to 20.
for i in range(2,21,2):
    print(i)

#Print the length of a string.
a=input()
print(len(a))

#Check if a string is empty.
f=input()
if f=="":
    print("Empty")
else:
    print("Not Empty") 

#Convert a string to uppercase.
y=input()   
print(y.upper())

#Convert a string to lowercase.
x=input()
print(x.lower())

#Print the first character of a string.
k=input()
for i in k:
    print(i)
    break

#Print the last charecter of a string.
p=input()
print(p[len(p)-1])

#Count the number of vowels in astring.
g=input()
c=0
for i in g:
    if i in"a,e,i,o,u,A,E,I,O,U":
        c+=1
print(c)





