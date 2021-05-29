from binascii import unhexlify

hx = open('task.hex', 'rb').read().split(b'\n')
plain = b''
for h in hx:
    plain += unhexlify(h[1:])

open('plain', 'wb').write(plain)

