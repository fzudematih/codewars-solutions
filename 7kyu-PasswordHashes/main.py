def pass_hash(str):
    import hashlib
    result = hashlib.md5(str.encode()) 
    return result.hexdigest()
