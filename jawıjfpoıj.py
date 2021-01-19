a=1
k=0
f=int(input("Ucgensel sayi olup olmadığını sorgulayacağın sayıyı gir:"))
for i in range(1,f+1):
    k+=i
    if(k==f):
        a=0
        print("Girdiğiniz ",f," sayısı üçgensel sayı olup\n",i,".üçgensel sayıdır",k)
if(a):
    print("Üçgensel Sayı değildir")

