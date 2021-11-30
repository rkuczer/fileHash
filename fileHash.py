import hashlib, sys
BLOCK_SIZE = 512*512 #doubled blocked size from sha256
hash_handler = hashlib.sha3_512()
values = []
#/Users/ryankuczer/PycharmProjects/fileHashReal/files/f0.docx

file = open("hash.txt", "w") #opens file to write hash values to
path = input("Enter hash path to folder (including the last /): ") #gets file path for folder without actual file name in path
#for loop to find other values for f0-f20
for i in range(0, 21, 1):
    file_path = path + "f" + str(i) + ".docx"
    #file_path = "/Users/ryankuczer/PycharmProjects/fileHashReal/files/f" + str(i) + ".docx" #file path with incrementing variable used to open file
    hash_handler2 = hashlib.new('sha3_512')
    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while fb:
            hash_handler2.update(fb)
            fb = f.read(BLOCK_SIZE)
    file_hexhash = hash_handler2.hexdigest()
    file.write(file_hexhash+"\n") #writes hex values to text file
    values.append(file_hexhash) #appends value to array for comparison
    #print(f"{file_path} file hash value: \n{file_hexhash}\n")
file.close()

#open hash.txt and compare f0 to f1-f20

print("Master hash value: " + values[0] +"\n")
line = 0
i = 0
while i < 20:

    if values[0] == values[i]:
        print("Found a matching file named f" + str(line) + ".docx")
        print(values[i])
        file1 = open("hash.txt", "a+")
    i = i+1
    line = line + 1
file1.close()

#while myline:
#    print(myline)
#    if myline == masterHash:
#        print("THIS FILE MATCHES")
#    else:
#        print("No matching file")
#    myline = file1.readline()


