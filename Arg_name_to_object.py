import hashlib

libname = ['Tie_Cell', 'NMOSWithDummy', 'PMOSWithDummy', 'SupplyRails']
num = []

def hashing(key:str):
    sha = hashlib.new('sha256')
    sha.update(key.encode())
    hash_str = sha.hexdigest()
    if hash_str[0].isdigit():
        hash_str = '_' + hash_str
    return hash_str

for i in libname :
    a = hashing(i)
    num.append(a)