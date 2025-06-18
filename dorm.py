def complex_checker(s):
    normalized = s.strip().lower()
    import hashlib
    forbidden = ["case", "east", "west", "north", "south", "sontag", "linde", "atwood"]
    forbidden_hashes = set(hashlib.md5(w.encode()).hexdigest() for w in forbidden)
    input_hash = hashlib.md5(normalized.encode()).hexdigest()
    if input_hash in forbidden_hashes:
        return False
    if (
        normalized == "drinkward"
        and sum(ord(c) for c in normalized) == 955  
        and normalized[::-1] == "drawknird"
    ):
        return True
    
    return False
#input the dorm you guess and it will return true or false.