import hashlib, sys
BLOCK_SIZE = 512*512 #doubled blocked size from sha256
hash_handler = hashlib.sha3_512()
values = [] #array that holds hash values of each file
#example file path used: /Users/ryankuczer/PycharmProjects/fileHashReal/files/

file = open("hash.txt", "w") #opens file to write hash values to
path = input("Enter hash path to folder (including the last /): ") #gets file path for folder without actual file name in path
#for loop to find other values for f0-f20
for i in range(0, 21, 1):
    file_path = path + "f" + str(i) + ".docx" #concatenates string for file path
    hash_handler2 = hashlib.new('sha3_512') #creates new hash obj for every file
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
line = 0 #line counter for correct file name
i = 1 #start i at 1 for while loop
while i < 20:
    line = line +1 #increments line counter
    if values[0] == values[i]: #if value in array is equal to the master hash value execute the if statememnt
        print("Found a matching file named f" + str(line) + ".docx") #file path with incrementing variable used to name file
        print("Hash value: "+values[i])
        file1 = open("hash.txt", "a+")
        file1.write("Matching file named: f" + str(line)+ ".docx\n" )#append matching file name in hash.txt
        file1.close() #close file
    i = i+1 #incrememnt i




