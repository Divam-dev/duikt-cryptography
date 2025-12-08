import hashlib  

def compute_md5(message):  
    # Перетворюємо рядок у байти та обчислюємо MD5  
    md5_hash = hashlib.md5(message.encode('utf-8')).hexdigest()  
    return md5_hash  

# Приклад використання  
text = "Hello World"  
hash_value = compute_md5(text)  
print(f"Хеш MD5 для '{text}': {hash_value}")  
