"""
Module d'évaluation des modèles

Ce module contient les fonctions nécessaires pour évaluer la performance des modèles
appris par le framework de learning fédéré.
"""

import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense

def evaluate_model(model: Model, X_test: np.ndarray, y_test: np.ndarray) -> dict:
    """
    Évalue la performance d'un modèle sur un ensemble de données de test.

    Args:
    - model (Model): Le modèle à évaluer
    - X_test (np.ndarray): Les données d'entrée de test
    - y_test (np.ndarray): Les étiquettes de sortie de test

    Returns:
    - Une dictionnaire contenant les résultats de l'évaluation
    """
    # Prédit les résultats sur les données de test
    y_pred = model.predict(X_test)

    # Convertit les résultats en étiquettes de sortie
    y_pred_class = np.argmax(y_pred, axis=1)
    y_test_class = np.argmax(y_test, axis=1)

    # Calcule les scores de performance
    accuracy = accuracy_score(y_test_class, y_pred_class)
    report = classification_report(y_test_class, y_pred_class)
    matrix = confusion_matrix(y_test_class, y_pred_class)

    # Renvoie les résultats de l'évaluation
    return {
        "accuracy": accuracy,
        "classification_report": report,
        "confusion_matrix": matrix
    }

def evaluate_model_on_dataset(model: Model, dataset: dict) -> dict:
    """
    Évalue la performance d'un modèle sur un ensemble de données divisées en lots.

    Args:
    - model (Model): Le modèle à évaluer
    - dataset (dict): Un dictionnaire contenant les données divisées en lots

    Returns:
    - Une dictionnaire contenant les résultats de l'évaluation
    """
    results = {}

    # Évalue le modèle sur chaque lot de données
    for i, (X_test, y_test) in enumerate(dataset.values()):
        results[f"lot_{i}"] = evaluate_model(model, X_test, y_test)

    return results

def plot_confusion_matrix(matrix: np.ndarray) -> None:
    """
    Affiche une matrice de confusion sous forme de graphique.

    Args:
    - matrix (np.ndarray): La matrice de confusion
    """
    import matplotlib.pyplot as plt
    plt.imshow(matrix, interpolation="nearest")
    plt.title("Matrice de confusion")
    plt.colorbar()
    plt.show()

def plot_roc_curve(fpr: np.ndarray, tpr: np.ndarray) -> None:
    """
    Affiche la courbe de la fonction réception-opérationnel (ROC) sous forme de graphique.

    Args:
    - fpr (np.ndarray): Les valeurs de fausse positivité
    - tpr (np.ndarray): Les valeurs de vraie positivité
    """
    import matplotlib.pyplot as plt
    plt.plot(fpr, tpr)
    plt.title("Courbe de ROC")
    plt.xlabel("Fausse positivité")
    plt.ylabel("Vraie positivité")
    plt.show()