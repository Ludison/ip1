


ipsd=[]
for i in range(10):
    a=input('请输入%g个ip' % (10-i))
    ipsd.append(a)

for i in range(10):
    ip=ipsd[i].split('.')
    if int(ip[0])==10:
        print(ipsd[i])
    elif (int(ip[0])==172) and (int(ip[1])<=31) and (int(ip[1])>=16):
        print(ipsd[i])
    elif (int(ip[0])==192) and (int(ip[1])==168):
        print(ipsd[i])
    else:
        continue


'''
ip=['1.1.1.1']
a=ip[0].split('.')
for i in range(len(a)):
    print(a[i])

a=input('')
ips=[]
ips.append(a)
b=ips[0].split('.',)
for i in range(len(b)):
    print(b[i])
'''