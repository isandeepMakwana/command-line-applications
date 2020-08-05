a=input()
d=int(a)
m=input()
c=[]
B=[]
c.append(m)
letter=list(c[0])

    q=ord(letter[i])
    if (q<97):
        B.append(chr(155-q))
        m=1
    else:
        B.append(chr(219-q))
        m=1
if(m==1):
    print("".join(B),end="")
else:
    print("Invalid")

