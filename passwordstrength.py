import string
str=input('Enter your password')
l=0
u=0
n=0
s=0
c=0
for i in range(len(str)):
    if str[i].islower()==True:
        l+=1
    elif str[i].isupper()==True:
        u+=1
    elif str[i].isnumeric()==True:
        n+=1
    else:
        s+=1
if l>0 and u>0 and n>0 and s>0 and len(str)>=8:
    print('Your password is strong')
elif l>0 and u>0 and s>0 and len(str)>=6:
    print('Your password is moderate')
    print('Add one digit to it')
    str1=input()
    str=str+str1
    print('Your password now is:',str)
    if len(str)<8:
        print('u need to add some characters')
        c=8-len(str)
        print("Add %d more characters to your password"%c)
        for i in range(c):
            ch=input()
            str=str+ch
        print('Your password now is:',str)
else:
    print('Your password is weak')
    if l==0:
        print('Add at least 1 lowercase character in your password')
        ch=input()
        str+=ch
    if u==0:
        print('Add at least 1 uppercase character in your password')
        ch=input()
        str+=ch
    if n==0:
        print('Add at least 1 digit character in your password')
        ch=input()
        str+=ch
    if s==0:
        print('Add at least 1 special character in your password')
        ch=input()
        str+=ch
    if len(str)<8:
        c=8-len(str)
        print("Add %d more characters to your password"%c)
        for i in range(c):
            ch=input()
            str=str+ch
        print('Your password now is:',str)
    
input()
