#---coding:utf-8---
import jieba

def main1():#while input
    while True:
        print(a:=input("say:"))
        if a == "break":
            print("good bey")
            break

def main2():#list,jieba,for
    s = "你好世界"
    ss = jieba.lcut(s)
    for a in ss:
        print(a)
    print(ss)
    print("ss[1]=",ss[1])

def main3():#list:append,
    ls1 = ["hh",11,1.2,True]
    ls2 = range(10,30)
    for s in ls2:
        ls1.append(s)
        print(ls1)
    ls2.index(44)

    
    print(ls2.index(19))
    # if (a:=type((xx:=ls1.index(138))))==int:
    #     print(xx)
    #     # ls1.pop(xx)
    # else:
    #     print(ls1)
    

if __name__ == "__main__":
    main3()