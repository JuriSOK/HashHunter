import hashlib
import requests

def hash_password(password, algo="sha256"):
    """ Hache un mot de passe avec l'algorithme donné """
    return hashlib.new(algo, password.encode()).hexdigest()

def check_password(word, hash_target, algo="sha256"):
    """ Vérifie si un mot de passe haché correspond au hash cible """
    return hash_password(word, algo) == hash_target

def check_hibp(hash_value):
    """ Vérifie si un hash est dans la base Have I Been Pwned """
    prefix = hash_value[:5].upper()
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    response = requests.get(url)
    if response.status_code != 200:
        print("Erreur lors de la requête à HIBP")
        return

    hashes = response.text.splitlines()
    for line in hashes:
        h, count = line.split(":")
        if hash_value[5:].upper() == h:
            print(f"Le hash a fuité {count} fois !")
            return
    
    print("Aucun résultat trouvé sur HIBP.")
