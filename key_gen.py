import random
import string

def generate_secret_key():
    # Генерируем случайную строку из символов ascii_letters и digits
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(50))

# Выводим сгенерированный ключ
print(generate_secret_key())
