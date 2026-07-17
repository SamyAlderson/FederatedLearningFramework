"""
Modèles utilisés pour l'apprentissage

Ce module définit les modèles utilisés pour l'apprentissage dans le framework de learning fédéré.
Il inclut des modèles de réseaux de neurones, SVM, K-Means, ainsi que des fonctions de formation et d'évaluation.
"""

from typing import Dict, List
from abc import ABC, abstractmethod
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from sklearn.svm import SVC
from sklearn.cluster import KMeans

class ModelBase(ABC):
    """
    Base class pour les modèles d'apprentissage
    """

    @abstractmethod
    def train(self, X: List[List[float]], y: List[float]) -> None:
        """
        Formation du modèle

        Args:
            X (List[List[float]]): Données d'entraînement
            y (List[float]): Étiquettes des données d'entraînement
        """
        pass

    @abstractmethod
    def predict(self, X: List[List[float]]) -> List[float]:
        """
        Prédiction avec le modèle

        Args:
            X (List[List[float]]): Données à prédire

        Returns:
            List[float]: Prédiction du modèle
        """
        pass

class NeuralNetworkModel(ModelBase):
    """
    Modèle de réseau de neurones
    """

    def __init__(self, num_inputs: int, num_outputs: int) -> None:
        """
        Construction du modèle

        Args:
            num_inputs (int): Nombre d'entrées du réseau
            num_outputs (int): Nombre de sorties du réseau
        """
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.model = self._create_model()

    def _create_model(self) -> Model:
        """
        Création du modèle de réseau de neurones

        Returns:
            Model: Modèle de réseau de neurones
        """
        inputs = Input(shape=(self.num_inputs,))
        x = Dense(64, activation='relu')(inputs)
        x = Dropout(0.2)(x)
        outputs = Dense(self.num_outputs)(x)
        model = Model(inputs=inputs, outputs=outputs)
        return model

    def train(self, X: List[List[float]], y: List[float]) -> None:
        """
        Formation du modèle

        Args:
            X (List[List[float]]): Données d'entraînement
            y (List[float]): Étiquettes des données d'entraînement
        """
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.model.fit(X, y, epochs=10)

    def predict(self, X: List[List[float]]) -> List[float]:
        """
        Prédiction avec le modèle

        Args:
            X (List[List[float]]): Données à prédire

        Returns:
            List[float]: Prédiction du modèle
        """
        return self.model.predict(X)

class SVMMODEL(ModelBase):
    """
    Modèle de SVM
    """

    def __init__(self) -> None:
        """
        Construction du modèle
        """
        self.model = SVC(kernel='rbf', C=1)

    def train(self, X: List[List[float]], y: List[float]) -> None:
        """
        Formation du modèle

        Args:
            X (List[List[float]]): Données d'entraînement
            y (List[float]): Étiquettes des données d'entraînement
        """
        self.model.fit(X, y)

    def predict(self, X: List[List[float]]) -> List[float]:
        """
        Prédiction avec le modèle

        Args:
            X (List[List[float]]): Données à prédire

        Returns:
            List[float]: Prédiction du modèle
        """
        return self.model.predict(X)

class KMeansModel(ModelBase):
    """
    Modèle de K-Means
    """

    def __init__(self, n_clusters: int) -> None:
        """
        Construction du modèle

        Args:
            n_clusters (int): Nombre de clusters
        """
        self.model = KMeans(n_clusters=n_clusters)

    def train(self, X: List[List[float]]) -> None:
        """
        Formation du modèle

        Args:
            X (List[List[float]]): Données d'entraînement
        """
        self.model.fit(X)

    def predict(self, X: List[List[float]]) -> List[int]:
        """
        Prédiction avec le modèle

        Args:
            X (List[List[float]]): Données à prédire

        Returns:
            List[int]: Prédiction du modèle (indice du cluster)
        """
        return self.model.predict(X)