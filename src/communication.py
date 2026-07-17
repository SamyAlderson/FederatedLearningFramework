"""
Protocole de communication entre les participants du framework de learning fédéré.

Ce module définit les fonctions de communication qui permettent aux participants
de s'interconnecter et d'échanger des données.
"""

import logging
import socket
import select
import pickle

from typing import Dict, List

# Configuration du logging
logging.basicConfig(level=logging.INFO)

class Participant:
    """Représentation d'un participant du framework de learning fédéré."""

    def __init__(self, name: str, ip: str, port: int):
        """
        Crée un nouveau participant.

        :param name: Nom du participant
        :param ip: Adresse IP du participant
        :param port: Numéro de port du participant
        """
        self.name = name
        self.ip = ip
        self.port = port

class Message:
    """Représentation d'un message entre les participants."""

    def __init__(self, type: str, data: Dict):
        """
        Crée un nouveau message.

        :param type: Type du message (e.g. 'model', 'data')
        :param data: Données associées au message
        """
        self.type = type
        self.data = data

def connect_to_participant(participant: Participant) -> socket.socket:
    """
    Établit une connexion avec un participant.

    :param participant: Participant à contacter
    :return: Socket de connexion
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((participant.ip, participant.port))
        return sock
    except socket.error as e:
        logging.error(f"Erreur de connexion avec {participant.name}: {e}")
        return None

def send_message(sock: socket.socket, message: Message) -> None:
    """
    Envoie un message à un participant via une connexion.

    :param sock: Socket de connexion
    :param message: Message à envoyer
    """
    try:
        data = pickle.dumps(message)
        sock.sendall(data)
    except socket.error as e:
        logging.error(f"Erreur d'envoi de message: {e}")

def receive_message(sock: socket.socket) -> Message:
    """
    Reçoit un message d'un participant via une connexion.

    :param sock: Socket de connexion
    :return: Message reçu
    """
    try:
        data = sock.recv(1024)
        message = pickle.loads(data)
        return message
    except socket.error as e:
        logging.error(f"Erreur de réception de message: {e}")
        return None

def communicate(participants: List[Participant], message: Message) -> None:
    """
    Envoie un message à tous les participants et reçoit leurs réponses.

    :param participants: Liste des participants
    :param message: Message à envoyer
    """
    for participant in participants:
        sock = connect_to_participant(participant)
        if sock:
            send_message(sock, message)
            response = receive_message(sock)
            if response:
                logging.info(f"Réponse de {participant.name}: {response}")
            sock.close()

# Exemple d'utilisation
if __name__ == "__main__":
    participants = [
        Participant("Participant 1", "127.0.0.1", 8080),
        Participant("Participant 2", "127.0.0.1", 8081)
    ]

    message = Message("model", {"weights": [1.0, 2.0, 3.0]})
    communicate(participants, message)