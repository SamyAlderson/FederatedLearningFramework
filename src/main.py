"""
Fichier principal du framework de learning fédéré.

Ce fichier est responsable de l'initialisation et de la gestion du framework.
Il importe les modules nécessaires et lance la formation des modèles.

Auteur: [Votre nom]
Date: [Date]
"""

import logging
import yaml
from flask import Flask
from src.models import Models
from src.data import Data
from src.communication import Communication
from src.training import Training
from src.evaluation import Evaluation
from src.main.config import Config

# Configuration du loggeur
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(file_path):
    """
    Charge la configuration du framework à partir d'un fichier YAML.

    Args:
        file_path (str): Chemin du fichier de configuration

    Returns:
        dict: Configuration du framework
    """
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        logger.error(f"Erreur lors du chargement de la configuration : {e}")
        return None

def create_app(config):
    """
    Crée une instance de l'application Flask.

    Args:
        config (dict): Configuration du framework

    Returns:
        Flask: Instance de l'application Flask
    """
    app = Flask(__name__)
    app.config.from_object(config)
    return app

def main():
    """
    Lance la formation des modèles et l'évaluation.
    """
    config = load_config('src/main/config.yaml')
    if config is None:
        return

    app = create_app(config)
    models = Models(config)
    data = Data(config)
    communication = Communication(config)
    training = Training(config, models, data)
    evaluation = Evaluation(config, models, data)

    # Formation des modèles
    training.former()

    # Évaluation des modèles
    evaluation.evaluer()

    # Démarrage de l'application Flask
    app.run(debug=True)

if __name__ == '__main__':
    main()