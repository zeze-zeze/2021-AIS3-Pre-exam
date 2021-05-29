import secrets


def splitmix64(x: int) -> int:
    U64_MASK = 0xFFFFFFFFFFFFFFFF
    x = (x + 0x9E3779B97F4A7C15) & U64_MASK
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & U64_MASK
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & U64_MASK
    return x ^ (x >> 31)


class Hash:

    def __init__(self):
        self.secret = secrets.randbits(64)


    def pad(self, message: bytes) -> bytes:
        c = -len(message) % 8
        return message + b'\x00' * c


    def digest(self, message: bytes) -> bytes:
        message = self.pad(message)

        blocks = [int.from_bytes(message[i:i+8], 'big')
                  for i in range(0, len(message), 8)]

        def f(a: int, b: int) -> int:
            for i in range(16):
                a, b = b, a ^ splitmix64(b)
            return b

        state = self.secret
        for block in blocks:
            state = f(state, block)

        return state.to_bytes(8, 'big')


    def hexdigest(self, message: bytes) -> str:
        return self.digest(message).hex()
