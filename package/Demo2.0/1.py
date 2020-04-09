import random




import tkinter.messagebox
#我是注释

Random=random.randint(1,100)
A=tkinter.messagebox.askokcancel("","IDE测试：输出随机数"+str(Random))
A=tkinter.messagebox.askokcancel("自定义标题","IDE测试：输出随机数2"+str(random.randint(-10,20)))
A=tkinter.messagebox.askokcancel("自定义标题","IDE测试：输出随机数3"+str(Random))
A=tkinter.messagebox.askokcancel("Helloworld!","你好世界！")
#我是注释,预告：下面是分支程序
if A == True :
    A=tkinter.messagebox.askokcancel("","听说你按下了确定哦")
if A == False :
    A=tkinter.messagebox.askokcancel("","听说你按下了取消哦")
B=int(input("现在输一个数字吧"))
C=random.randint(1,1000)
if B>C :
    A=tkinter.messagebox.askokcancel("","你比我猜的大,我的数字："+str(C))
if B<C :
    A=tkinter.messagebox.askokcancel("","你比我猜的小")
if B == C :
    A=tkinter.messagebox.askokcancel("","你和我一样")
