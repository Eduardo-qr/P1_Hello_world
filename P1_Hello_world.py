from datetime import datetime

nome = input("Diga seu nome: ")
idade = int(input("Diga a sua idade: "))

anos = 100 - idade
anos100 = datetime.now().year + anos

print(f"Olá {nome}!\nNo ano {anos100} você terá 100 anos.")

