import time
t1 = time.time()
filename = input('Enter file name: ')
with open(filename, 'rb') as f:
    in_bytes = f.read()


def xor_crypt(data, key=8):
    return bytes(a ^ key for a in data)


with open(filename, 'wb') as f:
    f.write(xor_crypt(in_bytes))
print(f'File {filename} crypted with XOR in {round(time.time() - t1, 2)}s.')