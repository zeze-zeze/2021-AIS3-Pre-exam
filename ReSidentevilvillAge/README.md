# CRYPTO - ReSident eval villAge
## 原始碼

```
import socketserver
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from binascii import unhexlify

class Task(socketserver.BaseRequestHandler):

	def recv(self):
		return self.request.recv(1024).strip()

	def send(self, msg):
		self.request.sendall(msg + b'\n')

	def handle(self):
		privkey = RSA.generate(1024)

		n = privkey.n
		e = privkey.e

		self.send(b'Welcome to ReSident evil villAge, sign the name "Ethan Winters" to get the flag.')
		self.send(b'n = ' + str(n).encode())
		self.send(b'e = ' + str(e).encode())

		while True:
			self.request.sendall(b'1) sign\n2) verify\n3) exit\n')
			option = self.recv()

			if option == b'1':
				self.request.sendall(b'Name (in hex): ')
				msg = unhexlify(self.recv())
				if msg == b'Ethan Winters' or bytes_to_long(msg) >= n:  # msg+k*n not allowed
					self.send(b'Nice try!')
				else:
					sig = pow(bytes_to_long(msg), privkey.d, n)     # TODO: Apply hashing first to prevent forgery
					self.send(b'Signature: ' + str(sig).encode())

			elif option == b'2':
				self.request.sendall(b'Signature: ')
				sig = int(self.recv())
				verified = (pow(sig, e, n) == bytes_to_long(b'Ethan Winters'))
				if verified:
					self.send(b'AIS3{THIS_IS_A_FAKE_FLAG}')
				else:
					self.send(b'Well done!')

			else:
				break

class ForkingServer(socketserver.ForkingTCPServer, socketserver.TCPServer):
	pass

if __name__ == "__main__":
	HOST, PORT = '0.0.0.0', 42069
	print(HOST, PORT)
	server = ForkingServer((HOST, PORT), Task)
	server.allow_reuse_address = True
	server.serve_forever()
```

## 題目理解
server 會把輸入的訊息用 RSA 簽名，只是輸入不能是 Ethan Winters。
server 也能把輸入解密看內容是不是 Ethan Winters，是的話就給 flag

## 漏洞
可以輸入 `\x00` 在 Ethan Winters 前面，這樣在簽名的時候可以繞過 `msg == b'Ethan Winters'` 的限制，又可以在解密的時候符合 `pow(sig, e, n) == bytes_to_long(b'Ethan Winters')` 的條件

## 解法
Welcome to ReSident evil villAge, sign the name "Ethan Winters" to get the flag.
n = 169036189258654061464491505945481373671908570812562154179746471112852619445493081405970719366717316414678171936274011854808776240313808314564776557610170453456244730397286144259972646108628404930755236055081156320060654295241376084227234369517622139839024633866721413400899145330637910201514715361377348422173
e = 65537
1) sign
2) verify
3) exit
1
Name (in hex): 00457468616e2057696e74657273
Signature: 60503940742789570198010780133825271110918084408862949839801463101461432944423351243289166272624071100706830965931761199935534026863746373973404592907356972686880315475976226738594540162078146315613674237977175795976188561654641255408725820076848828459709932564848359757316459833335026206102821951149183481532
1) sign
2) verify
3) exit
2
Signature: 60503940742789570198010780133825271110918084408862949839801463101461432944423351243289166272624071100706830965931761199935534026863746373973404592907356972686880315475976226738594540162078146315613674237977175795976188561654641255408725820076848828459709932564848359757316459833335026206102821951149183481532
AIS3{R3M383R_70_HAsh_7h3_M3Ssa93_83F0r3_S19N1N9}
