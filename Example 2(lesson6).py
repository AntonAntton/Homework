ba = bytearray(b'hello')
ba[0] = 72
print(ba)
print(type(ba))
immutable_bytes = bytes(ba)
print(immutable_bytes)