import os
import time
from multiprocessing import Pool

def xor_crypt(data, key=8):
    return bytes(a ^ key for a in data)


if __name__ == '__main__':
    t1 = time.time()
    max_thrs = os.cpu_count()
    block_size = 1000000
    filename = input('Enter file name: ')
    with open(filename, 'rb') as f:
        in_bytes = f.read()
    p = Pool(max_thrs)
    result = p.map(xor_crypt, [in_bytes[i:i + block_size] for i in range(0, len(in_bytes), block_size)])
    p.close()
    p.join()
    with open(filename, 'wb') as f:
        f.write(b''.join([k for k in result]))
    print(f'File {filename} crypted with XOR in {round(time.time() - t1, 2)}s.')