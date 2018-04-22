def fs(n):
    try:
        a=int(n)
    except ValueError as  e:
        print("您输入的数字有误，请再次输入")

    else:
        if  a==1:
            return 1
        elif a==2:
            return 1
        elif a>2:
            return fs(a-1)+fs(a-2)

if __name__=='__main__':
    b=input('请输入一个大于0的整数')
    print(fs(b))
