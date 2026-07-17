"""
Fichier de tests unitaires pour la gestion des données
"""

import unittest
from unittest.mock import Mock
from src.data import DataRepository, DataPartitioner

class TestDataRepository(unittest.TestCase):
    """
    Classe de tests unitaires pour la gestion des données
    """

    def setUp(self):
        """
        Initialisation des objectifs de test
        """
        self.data_repository = DataRepository()

    def test_add_data(self):
        """
        Test de l'ajout de données
        """
        data = {"label": "test", "features": [1, 2, 3]}
        self.data_repository.add_data(data)
        self.assertEqual(len(self.data_repository.data), 1)

    def test_get_data(self):
        """
        Test de la récupération des données
        """
        data = {"label": "test", "features": [1, 2, 3]}
        self.data_repository.add_data(data)
        retrieved_data = self.data_repository.get_data()
        self.assertEqual(len(retrieved_data), 1)
        self.assertEqual(retrieved_data[0], data)

    def test_remove_data(self):
        """
        Test de la suppression des données
        """
        data = {"label": "test", "features": [1, 2, 3]}
        self.data_repository.add_data(data)
        self.data_repository.remove_data(data)
        self.assertEqual(len(self.data_repository.data), 0)

class TestDataPartitioner(unittest.TestCase):
    """
    Classe de tests unitaires pour le partitionnement des données
    """

    def setUp(self):
        """
        Initialisation des objectifs de test
        """
        self.data_partitioner = DataPartitioner()

    def test_partition_data(self):
        """
        Test du partitionnement des données
        """
        data = [{"label": "test1", "features": [1, 2, 3]}, {"label": "test2", "features": [4, 5, 6]}]
        partitioned_data = self.data_partitioner.partition_data(data)
        self.assertEqual(len(partitioned_data), 2)

class TestData(unittest.TestCase):
    """
    Classe de tests unitaires pour la gestion des données
    """

    def test_data_partitioner(self):
        """
        Test du partitionnement des données
        """
        data_partitioner = DataPartitioner()
        data = [{"label": "test1", "features": [1, 2, 3]}, {"label": "test2", "features": [4, 5, 6]}]
        partitioned_data = data_partitioner.partition_data(data)
        self.assertEqual(len(partitioned_data), 2)

    def test_data_repository(self):
        """
        Test de la gestion des données
        """
        data_repository = DataRepository()
        data = {"label": "test", "features": [1, 2, 3]}
        data_repository.add_data(data)
        retrieved_data = data_repository.get_data()
        self.assertEqual(len(retrieved_data), 1)

if __name__ == "__main__":
    unittest.main()
```

```python
# src/data.py
"""
Module de gestion des données
"""

class DataRepository:
    """
    Classe de gestion des données
    """

    def __init__(self):
        """
        Initialisation de la classe
        """
        self.data = []

    def add_data(self, data):
        """
        Ajout de données
        """
        self.data.append(data)

    def get_data(self):
        """
        Récupération des données
        """
        return self.data

    def remove_data(self, data):
        """
        Suppression des données
        """
        self.data.remove(data)

class DataPartitioner:
    """
    Classe de partitionnement des données
    """

    def partition_data(self, data):
        """
        Partitionnement des données
        """
        partitioned_data = []
        for d in data:
            partitioned_data.append(d)
        return partitioned_data