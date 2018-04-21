
'''

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



def get_private_ip(ip_address):

    a=ip_address.split('.')
    first=a[0]
    second=a[1]
    third=a[2]
    fourth=a[3]

    try:
        first=int(first)
        second=int(second)
        third=int(third)
        fourth=int(fourth)
    except:
        print('您输入的第%g个ip有误，请确认输入正确的ip'% (i+1) )

    if (first==10 and 0<=second<=255 and 0<=third<=255 and 0<=fourth<=255):
        print('第%g个ip为第一类私有ip' % (i+1))
    elif (first==172 and 16<=second<=31 and 0<=third<=255 and 0<=fourth<=255):
        print('第%g个ip为第二类私有ip' % (i+1))
    elif (first==192 and second==168 and 0<=third<=255 and 0<=fourth<=255):
        print('第%g个ip为第三类私有ip' % (i+1))

if __name__=='__main__':

    row = input('请用空格为间隔输入ip地址')

    ip=[n for n in row.split()]
    for i in range(len(ip)):
        get_private_ip(ip[i])


