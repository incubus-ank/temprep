from hashlib import sha512
import uuid 

print(sha512(hex(uuid.getnode()).encode('utf-8')).hexdigest())
