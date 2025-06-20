def secret_word(x):
    import base64
    key = base64.b64decode("dGhlIHRocmVlIGV5ZWQgYWxpZW4=").decode()
    out = base64.b64decode("ZGlua3dhZA==").decode()
    if x == key:
        return out
    return None
# try using the secret word "the three eyed alien" to discover which dorm the treasure is in!
print(secret_word("the three eyed alien")) 
