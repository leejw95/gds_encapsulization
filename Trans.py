import hashlib


class Transfer:

    def change(self,key:str):
        sha = hashlib.new('sha256')
        sha.update(key.encode())
        hash_str = sha.hexdigest()
        if hash_str[0].isdigit():
            hash_str = '_' + hash_str
        return hash_str
