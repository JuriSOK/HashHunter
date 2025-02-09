import itertools
import multiprocessing
from tqdm import tqdm
from utils import hash_password, check_password

def brute_force_wordlist(hash_target, wordlist, algo="sha256"):
    """ Attaque basée sur une wordlist """
    with open(wordlist, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file]

    with multiprocessing.Pool(processes=4) as pool:
        results = list(tqdm(pool.imap(lambda word: check_password(word, hash_target, algo), words), total=len(words)))

    if any(results):
        print(f" Mot de passe trouvé : {words[results.index(True)]}")
    else:
        print("Mot de passe non trouvé.")


def brute_force_generate(hash_target, algo="sha256", max_length=4):
    """ Attaque brute force (génère tous les mots possibles) """
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    for length in range(1, max_length + 1):
        for word in tqdm(itertools.product(chars, repeat=length), total=len(chars)**length):
            word = "".join(word)
            if hash_password(word, algo) == hash_target:
                print(f" Mot de passe trouvé : {word}")
                return
    
    print("Mot de passe non trouvé.")
