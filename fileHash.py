import hashlib
BLOCK_SIZE = 262144
hash_handler = hashlib.sha3_512()
file = open("hash.txt", "w")

#master hash value
file_path = "/Users/ryankuczer/PycharmProjects/fileHashReal/files/f0.docx" #file path with incrementing variable used to open file
with open(file_path, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while fb:
        hash_handler.update(fb)
        fb = f.read(BLOCK_SIZE)
masterHash = hash_handler.hexdigest()
print(f"{file_path} file hash value: \n{masterHash}\n")

#other folder values
for i in range(1, 21, 1):
    file_path = "/Users/ryankuczer/PycharmProjects/fileHashReal/files/f" + str(i) + ".docx" #file path with incrementing variable used to open file
    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while fb:
            hash_handler.update(fb)
            fb = f.read(BLOCK_SIZE)
    file_hexhash = hash_handler.hexdigest()
    file.write(file_hexhash+"\n")
    print(f"{file_path} file hash value: \n{file_hexhash}\n")
file.close()

file1=open("hash.txt", "r")

Num = 0

for line in file1:
    if line == masterHash:
        print("File matches original")
    else:
        print("File Number: " + str(Num) + ": Not matching")
        Num = Num+1