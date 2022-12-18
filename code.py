from hashlib import sha256
import uuid 

print(sha256(hex(uuid.getnode()).encode('utf-8')).hexdigest())
