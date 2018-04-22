import  datetime

def day(date):
    try:
        dd=datetime.datetime.strptime(date,"%Y-%m-%d")
    except ValueError as e:
        print("您输入的格式有误，请重新输入")
    else:
        d=dd.timetuple().tm_yday
        print(d)

if __name__=='__main__':
    date = input("请输入一个日期，格式为 YYYY-MM-DD:")
    day(date)


