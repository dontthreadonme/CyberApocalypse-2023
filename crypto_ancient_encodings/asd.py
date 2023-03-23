from Crypto.Util.number import bytes_to_long, long_to_bytes
from base64 import b64decode

flag = open("output.txt", "r").readline()

print(b64decode(long_to_bytes(int(flag, 16))))
