import random

L=['Hero','villan','comedian','heroine','director','writer','sidecharacters']
B=['1','2','3','4','5','6','7','8','9','0']
A=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k']
M=['A','D','R','H','X','Z','L']
S=['!','@','-']
K=[B,A,M,S]
P=[]
for i in range(0,5):
    for j in K:
        P.append(random.choice(j))
        i=i+1
    i=i-3
random.shuffle(P)
newpass = ""
for i in P:
    newpass +=i

print(newpass)
num=[]
for z in range(0,len(B)):
    num += random.choice(B)
num1=""
for q in num:
    num1 += q
print(num1)