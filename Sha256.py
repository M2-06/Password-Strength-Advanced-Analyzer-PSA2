import hashlib

def txtToSHA256(passtxt):

#encode() converts the string into bytes to be accepted by the hash function.

    result = hashlib.sha256(passtxt.encode())

#hexidigest() returns the encoded data in hexadecimal format

    return result.hexdigest()
