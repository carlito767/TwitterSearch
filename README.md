# Twitter
Recherche de tweets via l'API Search de Twitter

# Configuration

* Installer [Python](https://www.python.org/)
* Ajouter le dossier d'installation de `Python` et le dossier Scripts (contenant l'exécutable `pip`) dans le PATH
* Cloner ce dépôt :
```
git clone --recursive https://github.com/carlito767/TwitterSearch
```

* Installer les modules nécessaires au projet (à partir du dossier du projet) :

```
pip install -r requirements.txt
```

* Créer un fichier `.env` et renseigner [les clés *développeur* de votre application Twitter](https://developer.twitter.com/en/docs/basics/getting-started) :

```
# Consumer API keys
API_KEY=<renseigner_ici_votre_clé_developpeur>
API_SECRET_KEY=<renseigner_ici_votre_clé_secrète_developpeur>
```

# Exécution

* Lancer le script :

```
python app.py
```
