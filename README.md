# wtf-api

L'api WTF-API vous donne accès à un large choix de films et de serie ainsi que toutes les informations rattachées à ces entités.

# Utilisation - Setup
 - Avant tout, assurez-vous d'avoir la variable DEBUG à True pour le developpement

```python
# settings.py
DEBUG = False
```
- Pour mettre à jour votre environement virtuel > ce mettre au niveau de ce fichier dans le terminal
```bash
pip install -r requirements.txt
```

- Si vous avez rajouté des modules à l'application faites systèmatiquement au niveau du fichier *requirements.txt* la commande suivante:
```bash
pip freeze > requirements.txt
```

- Lancer votre serveur, ENJOY!
```bash
python manage.py runserver
```


# Api ROUTES

**Section utilisateur**

*Inscription*
- **PUT** /api/profil/<user_id>
```json
{
    "email": "",
    "nom": "",
    "prenom": "",
    "date_naissance": null,
    "genre": "",
    "telephone": ""
}
```

*Connexion - JWT TOKEN*
- **POST** /api/api-token-auth
```json
{
    "email": "",
    "password": ""
}
```

*Rafraichir le token*
- **POST** /api/api-token-refresh/
```json
{
    "token": ""
}
```

*Inscription*
- **POST** /api/inscription
```json
{
    "email": "",
    "password": "",
    "nom": "",
    "prenom": "",
    "date_naissance": null,
    "genre": "",
    "telephone": "",
    "pays": ""
}
```

**Section Films**

- **GET** /api/films
```json
{
    "id_video": 12,
    "titre": "Le Monde de Nemo",
    "date_sortie": "2003-05-30",
    "poster": "/8zR2vXoXfdlknEYjfHvCbb1rJbI.jpg",
    "plot": "Dans les eaux tropicales de la Grande Barrière de corail, un poisson-clown du nom de Marin mène une existence paisible avec son fils unique, Nemo. Redoutant l'océan et ses risques imprévisibles, il fait de son mieux pour protéger son fils. Comme tous les petits poissons de son âge, celui-ci rêve pourtant d'explorer les mystérieux récifs. Lorsque Nemo disparaît, Marin devient malgré lui le héros d'une quête unique et palpitante. Le pauvre papa ignore que son rejeton à écailles a été emmené jusque dans l'aquarium d'un dentiste. Marin ne s'engagera pas seul dans l'aventure : la jolie Dory, un poisson-chirurgien bleu à la mémoire défaillante et au grand cœur, va se révéler d'une aide précieuse. Les deux poissons vont affronter d'innombrables dangers, mais l'optimisme de Dory va pousser Marin à surmonter toutes ses peurs.",
    "vo": "en",
    "scores": [],
    "duree": "101",
    "categories": [
    ],
    "productions": [
    ],
    "acteurs": []
},
{
    "id_video": 3,
    "titre": "Ombres au paradis",
    "date_sortie": "1986-10-17",
    "poster": "/nj01hspawPof0mJmlgfjuLyJuRN.jpg",
    "plot": "L'histoire d'amour d'un conducteur de camion a ordures, Nikander, et d'une caissiere de supermarche, Ilona. Un des rares films du nouveau cinema finlandais enfin sur nos ecrans.",
    "vo": "fi",
    "scores": [],
    "duree": "73",
    "categories": [
    ],
    "productions": [
    ],
    "acteurs": []
  }
```


- **GET** /api/films/<int:id_film>
```json
{
    "id_video": 12,
    "titre": "Le Monde de Nemo",
    "date_sortie": "2003-05-30",
    "poster": "/8zR2vXoXfdlknEYjfHvCbb1rJbI.jpg",
    "plot": "Dans les eaux tropicales de la Grande Barrière de corail, un poisson-clown du nom de Marin mène une existence paisible avec son fils unique, Nemo. Redoutant l'océan et ses risques imprévisibles, il fait de son mieux pour protéger son fils. Comme tous les petits poissons de son âge, celui-ci rêve pourtant d'explorer les mystérieux récifs. Lorsque Nemo disparaît, Marin devient malgré lui le héros d'une quête unique et palpitante. Le pauvre papa ignore que son rejeton à écailles a été emmené jusque dans l'aquarium d'un dentiste. Marin ne s'engagera pas seul dans l'aventure : la jolie Dory, un poisson-chirurgien bleu à la mémoire défaillante et au grand cœur, va se révéler d'une aide précieuse. Les deux poissons vont affronter d'innombrables dangers, mais l'optimisme de Dory va pousser Marin à surmonter toutes ses peurs.",
    "vo": "en",
    "scores": [],
    "duree": "101",
    "categories": [
    ],
    "productions": [
    ],
    "acteurs": []
}
```

**POST** /api/films/rating
```
"film": id_video,
"note": [1-5]
```

**PUT** /api/films/rating/<int:pk>
- /!\ Si un utilisateur autre que celui qui a voter essaye de voter il y a un accès refusé. /!\
```
"film": id_video,
"note": [1-5]
```
