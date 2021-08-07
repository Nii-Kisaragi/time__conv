n=0.0
i=0.0
j=0.0
print("選択してください\n\nmin→h:1, s→h:2\n\n")
n=input()
N=int(n)

if N==1:
    print("換算したい数値[min]を入力してください。\n\n")
    i=input()
    I=float(i)
    j=I/60
    print(str(I)+"minは"+str(j)+"hです。\n\n")
    N=0;i=0;I=0;j=0

elif N==2:
    print("換算したい数値[s]を入力してください。\n\n")
    i=input()
    I=float(i)
    j=I/60/60
    print(str(I)+"sは"+str(j)+"hです。\n\n")
    N=0;i=0;I=0;j=0;
    
else:
    print("入力した数値が不正です。\n\n")