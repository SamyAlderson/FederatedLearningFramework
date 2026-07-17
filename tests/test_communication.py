# tests/test_communication.py

import unittest
import json
from src.data import Data
from src.communication import Communication
from src.models import Model

class TestCommunication(unittest.TestCase):

    def setUp(self):
        self.data = Data()
        self.communication = Communication()
        self.model = Model()

    def test_send_message(self):
        # Test si la méthode send_message envoyer un message correctement
        message = {'type': 'test', 'data': 'hello'}
        response = self.communication.send_message(message)
        self.assertEqual(response, {'status': 'ok'})

    def test_receive_message(self):
        # Test si la méthode receive_message recevoir un message correctement
        message = {'type': 'test', 'data': 'hello'}
        self.communication.send_message(message)
        response = self.communication.receive_message()
        self.assertEqual(response, message)

    def test_register_model(self):
        # Test si la méthode register_model s'enregistrer un modèle correctement
        model = self.model
        self.communication.register_model(model)
        self.assertIn(model, self.communication.models)

    def test_send_model_update(self):
        # Test si la méthode send_model_update envoyer une mise à jour de modèle correctement
        model = self.model
        update = {'weights': [1, 2, 3]}
        response = self.communication.send_model_update(model, update)
        self.assertEqual(response, {'status': 'ok'})

    def test_receive_model_update(self):
        # Test si la méthode receive_model_update recevoir une mise à jour de modèle correctement
        model = self.model
        update = {'weights': [1, 2, 3]}
        self.communication.send_model_update(model, update)
        response = self.communication.receive_model_update(model)
        self.assertEqual(response, update)

if __name__ == '__main__':
    unittest.main()
```

```python
# tests/test_communication.py (suite)

import unittest
from src.communication import Communication

class TestCommunicationError(unittest.TestCase):

    def setUp(self):
        self.communication = Communication()

    def test_send_message_invalid_message(self):
        # Test si la méthode send_message lever une erreur avec un message invalide
        message = {}
        with self.assertRaises(ValueError):
            self.communication.send_message(message)

    def test_receive_message_no_message(self):
        # Test si la méthode receive_message lever une erreur sans message
        with self.assertRaises(ValueError):
            self.communication.receive_message()

    def test_register_model_invalid_model(self):
        # Test si la méthode register_model lever une erreur avec un modèle invalide
        model = None
        with self.assertRaises(TypeError):
            self.communication.register_model(model)

    def test_send_model_update_invalid_update(self):
        # Test si la méthode send_model_update lever une erreur avec une mise à jour invalide
        model = self.model
        update = None
        with self.assertRaises(ValueError):
            self.communication.send_model_update(model, update)

    def test_receive_model_update_no_update(self):
        # Test si la méthode receive_model_update lever une erreur sans mise à jour
        model = self.model
        with self.assertRaises(ValueError):
            self.communication.receive_model_update(model)

if __name__ == '__main__':
    unittest.main()