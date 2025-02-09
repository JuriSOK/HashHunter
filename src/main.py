import argparse
from hash_cracker import brute_force_wordlist, brute_force_generate
from utils import check_hibp

def main():
    parser = argparse.ArgumentParser(description="HashHunter")
    
    parser.add_argument("-m", "--mode", type=str, choices=["wordlist", "bruteforce", "hibp"], required=True,
                        help="Mode : wordlist (dictionnaire), bruteforce (génération) ou hibp (vérification fuite)")
    parser.add_argument("-H", "--hash", type=str, required=True, help="Le hash à tester/casser")
    parser.add_argument("-a", "--algo", type=str, default="sha256", help="Algorithme (ex: md5, sha256)")
    
    parser.add_argument("-w", "--wordlist", type=str, help="Wordlist (si mode wordlist)")
    parser.add_argument("-l", "--length", type=int, default=4, help="Longueur du mot de passe (si mode bruteforce)")
    
    args = parser.parse_args()

    if args.mode == "wordlist":
        if not args.wordlist:
            print("Erreur : Vous devez spécifier une wordlist avec -w")
            return
        brute_force_wordlist(args.hash, args.wordlist, args.algo)
    
    elif args.mode == "bruteforce":
        brute_force_generate(args.hash, args.algo, args.length)

    elif args.mode == "hibp":
        check_hibp(args.hash)

if __name__ == "__main__":
    main()
