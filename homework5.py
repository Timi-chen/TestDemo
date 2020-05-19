import random
x=eval(input(""))
y=random.randint[0,30]
i=0
while(x!=y):
    if(x<y):
        print("遗憾！太小了")
        i+=1
        x=eval(input(""))
    else:
        print("遗憾！太大了")
        i+=1
        x=eval(input(""))
else:
    print("预测{}次，你猜中了！".format(i))
