# Projet CBIR (Content-Based Image Retrieval) avec Streamlit

Ce projet implémente un système de recherche d'images basé sur leur contenu (CBIR) à l'aide de descripteurs d'images binaires (BiT) et d'une interface utilisateur interactive créée avec Streamlit. Les utilisateurs peuvent téléverser une image de requête, choisir une mesure de distance de similarité, puis visualiser les images les plus similaires dans une base de données locale.

## Fonctionnalités

- **Interface utilisateur interactive** : L'application utilise Streamlit pour fournir une interface utilisateur interactive où les utilisateurs peuvent téléverser une image de requête et visualiser les images similaires trouvées dans la base de données. (Fichier : `app.py`)

- **Choix de la distance de similarité** : Les utilisateurs peuvent choisir parmi plusieurs mesures de distance (Euclidienne, Canberra, Manhattan, Chebyshev, Minkowsky) pour calculer la similarité entre les images. (Fichier : `distances.py`)

- **Extraction des descripteurs d'images** : Les descripteurs d'images sont extraits à l'aide de l'algorithme BiT (Binary Texture Descriptor). (Fichier : `descriptors.py`)

- **Gestion des chemins d'accès aux images** : Les chemins d'accès aux images sont définis dans le fichier `paths.py`. Pour éviter d'exposer des informations sensibles, utilisez des chemins relatifs ou des variables d'environnement.

- **Téléchargement de l'image de requête** : Les utilisateurs peuvent téléverser une image de requête à l'aide de la fonctionnalité de téléchargement d'image. (Fichier : `upload.py`)

- **Calcul des distances de similarité** : Les distances de similarité entre l'image de requête et les images de la base de données sont calculées en fonction de la mesure de distance sélectionnée. (Fichier : `distances.py`)

- **Affichage des résultats** : Les images similaires sont affichées à l'utilisateur sous forme de vignettes dans l'interface utilisateur. (Fichier : `app.py`)

- **Gestion des dépendances** : Les dépendances du projet sont répertoriées dans le fichier `dependencies.txt` et peuvent être installées à l'aide de la commande `pip install -r dependencies.txt`.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir Python et pip installés.
3. Créez un environnement virtuel (facultatif mais recommandé).
4. Installez les dépendances en exécutant `pip install -r dependencies.txt`.

## Utilisation

1. Exécutez l'application en utilisant la commande `streamlit run app.py`.
2. Téléversez une image de requête.
3. Choisissez une mesure de distance de similarité.
4. Visualisez les images similaires trouvées dans la base de données.

## Gestion des informations sensibles

Le chemin `kth_path` spécifié dans le fichier `paths.py` représente le chemin absolu vers le dossier contenant les images de la base de données. Dans ce projet, il s'agit du dossier KTH-TIPS2-a, qui contient les images utilisées pour la recherche d'images basée sur le contenu (CBIR). Assurez-vous que ce chemin est correctement configuré pour que le projet puisse accéder aux images nécessaires.
Pour éviter de compromettre vos informations personnelles, assurez-vous de ne pas inclure d'informations sensibles dans vos fichiers. Si vos fichiers Python contiennent des chemins personnels, remplacez-les par des chemins relatifs ou utilisez des variables d'environnement.

## Contribution

Les contributions sont les bienvenues. Pour toute modification majeure, veuillez ouvrir d’abord une issue pour discuter de ce que vous aimeriez changer.

## Licence

Ce projet est sous licence MIT. Pour plus d'informations, consultez le fichier `LICENSE`.
