import unittest
from src import models

class TestModel(unittest.TestCase):
    def test_neural_network(self):
        """Test le modèle de réseau de neurones"""
        # Création d'un réseau de neurones
        model = models.NeuralNetwork(input_dim=10, output_dim=5)
        # Vérification de la structure du réseau
        self.assertEqual(model.layers[0].output_shape, (10,))
        self.assertEqual(model.layers[-1].output_shape, (5,))

    def test_support_vector_machine(self):
        """Test le modèle de machine à support vector"""
        # Création d'une machine à support vector
        model = models.SupportVectorMachine(kernel='linear')
        # Vérification de la forme du modèle
        self.assertEqual(model.coef_.shape, (5,))

    def test_kmeans(self):
        """Test le modèle de K-Means"""
        # Création d'un modèle de K-Means
        model = models.KMeans(n_clusters=5)
        # Vérification de la forme du modèle
        self.assertEqual(model.cluster_centers_.shape, (5, 5))

class TestModelTraining(unittest.TestCase):
    def test_neural_network_training(self):
        """Test la formation du réseau de neurones"""
        # Création d'un réseau de neurones
        model = models.NeuralNetwork(input_dim=10, output_dim=5)
        # Formation du réseau
        model.train(data=[1, 2, 3, 4, 5])
        # Vérification de la forme du réseau après formation
        self.assertEqual(model.layers[0].output_shape, (10,))
        self.assertEqual(model.layers[-1].output_shape, (5,))

    def test_support_vector_machine_training(self):
        """Test la formation de la machine à support vector"""
        # Création d'une machine à support vector
        model = models.SupportVectorMachine(kernel='linear')
        # Formation de la machine
        model.train(data=[1, 2, 3, 4, 5])
        # Vérification de la forme de la machine après formation
        self.assertEqual(model.coef_.shape, (5,))

    def test_kmeans_training(self):
        """Test la formation du modèle de K-Means"""
        # Création d'un modèle de K-Means
        model = models.KMeans(n_clusters=5)
        # Formation du modèle
        model.train(data=[1, 2, 3, 4, 5])
        # Vérification de la forme du modèle après formation
        self.assertEqual(model.cluster_centers_.shape, (5, 5))

if __name__ == '__main__':
    unittest.main()