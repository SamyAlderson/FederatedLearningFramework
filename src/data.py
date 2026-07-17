"""
Module src/data.py pour la gestion des données distribuées.

Cette classe gère les données distribuées entre les participants du framework de l'apprentissage fédéré.
Elle utilise un système de partitionnement pour gérer les données et prend en compte la variabilité des données.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple

class Data:
    """
    Classe Data pour la gestion des données distribuées.
    """

    def __init__(self, data: List[Dict], partitionnement: Dict):
        """
        Initialise la classe Data avec les paramètres suivants :

        Args:
            data (List[Dict]): Liste de données à stocker.
            partitionnement (Dict): Dictionnaire de partitionnement pour les données.

        Raises:
            ValueError: Si les données ne sont pas de type List[Dict].
            ValueError: Si le partitionnement n'est pas de type Dict.
        """
        if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
            raise ValueError("Les données doivent être de type List[Dict].")
        if not isinstance(partitionnement, dict):
            raise ValueError("Le partitionnement doit être de type Dict.")

        self.data = data
        self.partitionnement = partitionnement

    def get_partition(self, participant: str) -> Dict:
        """
        Récupère la partition de données pour un participant spécifique.

        Args:
            participant (str): Nom du participant.

        Returns:
            Dict: Partition de données pour le participant.

        Raises:
            KeyError: Si le participant n'est pas trouvé dans le partitionnement.
        """
        if participant not in self.partitionnement:
            raise KeyError(f"Participant '{participant}' non trouvé dans le partitionnement.")

        return self.partitionnement[participant]

    def get_partition_size(self, participant: str) -> int:
        """
        Récupère la taille de la partition de données pour un participant spécifique.

        Args:
            participant (str): Nom du participant.

        Returns:
            int: Taille de la partition de données pour le participant.

        Raises:
            KeyError: Si le participant n'est pas trouvé dans le partitionnement.
        """
        partition = self.get_partition(participant)
        return len(partition)

    def get_data(self, participant: str) -> List[Dict]:
        """
        Récupère les données pour un participant spécifique.

        Args:
            participant (str): Nom du participant.

        Returns:
            List[Dict]: Données pour le participant.

        Raises:
            KeyError: Si le participant n'est pas trouvé dans le partitionnement.
        """
        return [d for d in self.data if d['participant'] == participant]

    def get_total_data(self) -> List[Dict]:
        """
        Récupère toutes les données.

        Returns:
            List[Dict]: Toutes les données.
        """
        return self.data

    def update_partition(self, participant: str, partition: Dict):
        """
        Met à jour la partition de données pour un participant spécifique.

        Args:
            participant (str): Nom du participant.
            partition (Dict): Nouvelle partition de données pour le participant.

        Raises:
            KeyError: Si le participant n'est pas trouvé dans le partitionnement.
        """
        self.partitionnement[participant] = partition

    def add_data(self, data: Dict):
        """
        Ajoute de nouvelles données à la gestion.

        Args:
            data (Dict): Nouvelles données à ajouter.

        Raises:
            ValueError: Si les données ne sont pas de type Dict.
        """
        if not isinstance(data, dict):
            raise ValueError("Les données doivent être de type Dict.")

        self.data.append(data)

# Exemple d'utilisation
if __name__ == "__main__":
    data = [
        {'participant': 'participant1', 'features': [1, 2, 3], 'label': 0},
        {'participant': 'participant2', 'features': [4, 5, 6], 'label': 1},
        {'participant': 'participant1', 'features': [7, 8, 9], 'label': 0},
    ]

    partitionnement = {
        'participant1': [0, 2],
        'participant2': [1]
    }

    data_manager = Data(data, partitionnement)
    print(data_manager.get_partition('participant1'))
    print(data_manager.get_data('participant1'))
    print(data_manager.get_total_data())
    data_manager.update_partition('participant1', [0, 1])
    print(data_manager.get_partition('participant1'))
    data_manager.add_data({'participant': 'participant3', 'features': [10, 11, 12], 'label': 1})
    print(data_manager.get_total_data())