import hashlib
BLOCK_SIZE = 262144
hash_handler = hashlib.sha3_512()
file = open("hash.txt", "w")

for i in range(0, 21, 1):
    file_path = "/Users/ryankuczer/PycharmProjects/fileHashReal/files/f" + str(i) + ".docx" #file path with incrementing variable used to open file

    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while fb:
            hash_handler.update(fb)
            fb = f.read(BLOCK_SIZE)
    file_hexhash = hash_handler.hexdigest()
    file.write(file_hexhash+"\n")
    print(f"{file_path} file hash value: \n{file_hexhash}")
file.close()
file=open("hash.txt", "r")
line1 = file.readline()
Num = 0
for line in file:
    if line == line1:
        print("File matches original")
    else:
        print("File Number: " + str(Num) + ": Not matching")
        Num = Num+1