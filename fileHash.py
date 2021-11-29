import hashlib
BLOCK_SIZE = 512*512 #doubled blocked size from sha256
hash_handler = hashlib.sha3_512()
file = open("hash.txt", "w")

#master hash value used to compare to examples in hash.txt
file_path = "/Users/ryankuczer/PycharmProjects/fileHashReal/files/f0.docx" #file path with incrementing variable used to open file
with open(file_path, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while fb:
        hash_handler.update(fb)
        fb = f.read(BLOCK_SIZE)
masterHash = hash_handler.hexdigest()
#print(f"Master hash is{file_path} file hash value: \n{masterHash}\n")

#for loop to find other values for f1-f20
for i in range(1, 21, 1):
    file_path = "/Users/ryankuczer/PycharmProjects/fileHashReal/files/f" + str(i) + ".docx" #file path with incrementing variable used to open file
    hash_handler2 = hashlib.new('sha3_512')
    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while fb:
            hash_handler2.update(fb)
            fb = f.read(BLOCK_SIZE)
    file_hexhash = hash_handler2.hexdigest()
    file.write(file_hexhash+"\n")
    #print(f"{file_path} file hash value: \n{file_hexhash}\n")
file.close()

#open hash.txt and compare f0 to f1-f20
file1=open("hash.txt", "rb")
myline = file1.readline()
print("Master hash: " + masterHash +"\n")
while myline:
    print(myline)
    if myline == masterHash:
        print("THIS FILE MATCHES")
    else:
        print("No matching file")
    myline = file1.readline()
file1.close()
