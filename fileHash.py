import hashlib
file_path = "C:/Users/ryan-/PycharmProjects/fileHash/files/f0.docx"
i=ord(file_path[47])
i+=1
char=chr(i)
print(char)
for(i==0, )
BLOCK_SIZE = 262144
hash_handler = hashlib.sha512()
file = open("hash.txt", "w")

with open(file_path, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while fb:
        hash_handler.update(fb)
        fb = f.read(BLOCK_SIZE)
file_hexhash = hash_handler.hexdigest()
file.write(file_hexhash)
file.close()
print(f"{file_path} file hash value: \n{file_hexhash}")
