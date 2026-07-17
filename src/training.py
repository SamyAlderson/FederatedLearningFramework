"""
Module de formation des modèles.

Ce module fournit des fonctions pour la formation des modèles de l'apprentissage fédéré.
"""

import logging
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

logger = logging.getLogger(__name__)

def formater_donnees(data, target):
    """
    Formate les données pour la formation des modèles.

    Args:
        data (numpy.ndarray): Données d'entrée.
        target (numpy.ndarray): Cibles.

    Returns:
        tuple: Données formattées et cibles.
    """
    logger.info("Formattage des données...")
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def creer_modele(input_shape, output_shape):
    """
    Crée un modèle de réseau de neurones.

    Args:
        input_shape (int): Nombre de dimensions d'entrée.
        output_shape (int): Nombre de dimensions de sortie.

    Returns:
        tensorflow.keras.Model: Modèle de réseau de neurones.
    """
    logger.info("Création du modèle...")
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(input_shape,)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(output_shape, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def entrainer_modele(model, X_train, y_train, epochs, batch_size):
    """
    Entraîne le modèle.

    Args:
        model (tensorflow.keras.Model): Modèle à entraîner.
        X_train (numpy.ndarray): Données d'entrée pour l'entraînement.
        y_train (numpy.ndarray): Cibles pour l'entraînement.
        epochs (int): Nombre d'époques.
        batch_size (int): Taille du lot.

    Returns:
        tuple: Historique de l'entraînement et modèle entraîné.
    """
    logger.info("Entraînement du modèle...")
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, min_delta=0.001)
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, callbacks=[early_stopping])
    return history, model

def evaluer_modele(model, X_test, y_test):
    """
    Évalue le modèle.

    Args:
        model (tensorflow.keras.Model): Modèle à évaluer.
        X_test (numpy.ndarray): Données d'entrée pour l'évaluation.
        y_test (numpy.ndarray): Cibles pour l'évaluation.

    Returns:
        tuple: Prédiction et exactitude du modèle.
    """
    logger.info("Évaluation du modèle...")
    prediction = model.predict(X_test)
    accuracy = model.evaluate(X_test, y_test)
    return prediction, accuracy