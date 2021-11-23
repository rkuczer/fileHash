import hashlib
file_path = "/Users/ryankuczer/PycharmProjects/fileHashReal/files/f0.docx"
order=ord(file_path[54])
char=chr(order)
for i in range(0, 21, 1):
    print(order)
    char+=1
    char = char(order)
    print(type(order))

BLOCK_SIZE = 262144
hash_handler = hashlib.sha512()
file = open("hash.txt", "w")
#for loop here for everything else
with open(file_path, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while fb:
        hash_handler.update(fb)
        fb = f.read(BLOCK_SIZE)
file_hexhash = hash_handler.hexdigest()
file.write(file_hexhash)
file.close()
print(f"{file_path} file hash value: \n{file_hexhash}")
