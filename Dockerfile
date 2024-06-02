# Utiliser une image de base Python
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt et installer les dépendances
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu de votre projet dans le répertoire de travail
COPY . .

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Spécifier la commande par défaut à exécuter lorsque le conteneur démarre
CMD ["streamlit", "run", "app/Scouting_Assistant.py"]
