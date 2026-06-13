import random
import string
print("\033[92m PASSWORD GENERATOR\033[0m")

while True:
    try:

        size = int(input("Tamanho da senha: "))
        break
    except:
        print("Digite so numeros!")

chars = string.ascii_letters + string.digits + "!@#$%"
password = ""
for i in range(size):
    password += random.choice(chars)


print(f"Sua senha: {password}")

if size >= 12:
    print("Sua senha: {password}")
else:
    print("Senha  fraca, use 12+ caracteres")
