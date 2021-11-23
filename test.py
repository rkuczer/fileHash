import hashlib  # hashlib module
#algorithms_guaranteed property shows all available hash algorithms.
print(hashlib.algorithms_guaranteed)

# make a hash object
h = hashlib.sha3_256()
h.update(b'ABCDE')  # Update the hash object with byte object
h_digest = h.digest()   # Return the digest of the data passed to the update() method so far
h_hexDigest = h.hexdigest() # containing only hexadecimal digits
h_digestSize = h.digest_size    #The size of the resulting hash in bytes

print(f'h hash value: {h_digest}')
print(f'h hash hex value: {h_hexDigest}')
print(f'h hash size in bytes: {h_digestSize}')

h.update(b'abcde')  # Repeated calls are equivalent to a single call with the concatenation of all the arguments
h_digest = h.digest()
h_hexDigest = h.hexdigest()
h_digestSize = h.digest_size

print(f'h hash value: {h_digest}')
print(f'h hash hex value: {h_hexDigest}')
print(f'h hash size in bytes: {h_digestSize}')

# make a hash object
h1 = hashlib.sha3_256()
h1.update(b'ABCDEabcde')  # Update the hash object with byte object
h1_digest = h1.digest()   # Return the digest of the data passed to the update() method so far
h1_hexDigest = h1.hexdigest() # containing only hexadecimal digits
h1_digestSize = h1.digest_size    #The size of the resulting hash in bytes

print(f'h1 hash value: {h1_digest}')
print(f'h1 hash hex value: {h1_hexDigest}')
print(f'h1 hash size in bytes: {h1_digestSize}')

