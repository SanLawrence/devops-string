from unidecode import unidecode

def standardize(text):
    return unidecode(text)

nome = "Saint Lawrence Sevalho Gonçalves Dias"
std_nome = standardize(nome)
print(f"Seu nome é: {nome}\nSeu nome sem acento é: {std_nome}")