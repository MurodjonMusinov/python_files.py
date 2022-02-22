a = int(input('ko\'paytiriluvchi\nx gacha\n(maksimal 10 ta oladi):'))
for i in range(a-9,a+1):
    if a -9 <0:break
    print()
    for x in range(1,11):
        print(str(i)+"*",str(x),'=',int(i)*int(x))
        