import os
key = "USERNAME"
value = os.getenv(key)
while True:
    os.system(f"python3 like.py {value}")
