# Login-and-Mdp-BruteForcer
# Brute Force Tool

Ce programme est un outil de bruteforce développé en Python pour tester des combinaisons de noms d'utilisateur et de mots de passe sur une page de connexion donnée.

## Fonctionnalités

- **Bruteforce des noms d'utilisateur et des mots de passe :** Le programme lit les noms d'utilisateur à partir d'un fichier `userlist.txt` et les mots de passe à partir d'un fichier `passlist.txt`, puis essaie chaque combinaison sur une page de connexion spécifiée.
- **Gestion des cookies :** Le programme permet de spécifier une valeur de cookie à inclure dans la requête HTTP.

## Configuration

Assurez-vous de configurer les paramètres :

- `url` : URL de la page de connexion.
- `password_file` : Chemin vers le fichier contenant la liste des mots de passe.
- `userfile` : Chemin vers le fichier contenant la liste des noms d'utilisateur.
- `login_failed_string` : Chaîne de caractères indiquant qu'une tentative de connexion avec un nom d'utilisateur invalide a échoué.
- `password_failed_string` : Chaîne de caractères indiquant qu'une tentative de connexion avec un mot de passe invalide a échoué.
- `cookie_value` : Valeur du cookie à inclure dans la requête HTTP.

## Utilisation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Exécutez le programme en exécutant `python3 brute.py` dans votre terminal.

## Avertissement

Ce programme est développé dans un but éducatif et éthique. Assurez-vous d'avoir l'autorisation appropriée avant de l'utiliser sur un système ou un service tiers. L'utilisation abusive de cet outil peut avoir des conséquences légales.

## Auteur

Ce programme a été développé par [Ardcord].

Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter.


