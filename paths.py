from typing import List
from os import listdir
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer la valeur de KTH_PATH depuis les variables d'environnement
kth_path = os.getenv("KTH_PATH")

if kth_path is None:
    raise ValueError("KTH_PATH n'est pas défini dans les variables d'environnement")

kth_dir: List[str] = listdir(kth_path)
#print(kth_dir)
