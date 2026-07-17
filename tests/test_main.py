# tests/test_main.py

import unittest
from unittest.mock import patch
from src.main import main
from src.exceptions import FrameworkException

class TestMainFunction(unittest.TestCase):

    @patch('src.main.logger')
    def test_main_calls_main_function(self, mock_logger):
        # Arrange
        mock_logger.info.return_value = None

        # Act
        main()

        # Assert
        mock_logger.info.assert_called_once()

    @patch('src.main.logger')
    def test_main_calls_main_function_with_args(self, mock_logger):
        # Arrange
        mock_logger.info.return_value = None

        # Act
        main(args='-h')

        # Assert
        mock_logger.info.assert_called_once()

    @patch('src.main.logger')
    def test_main_calls_main_function_with_invalid_args(self, mock_logger):
        # Arrange
        mock_logger.error.return_value = None

        # Act
        with self.assertRaises(SystemExit):
            main(args='-i')

        # Assert
        mock_logger.error.assert_called_once()

    def test_main raises_FrameworkException_with_internal_error(self):
        # Act
        with self.assertRaises(FrameworkException):
            main(args='-i')

if __name__ == '__main__':
    unittest.main()
```

```python
# tests/test_main.py (suite)

import unittest
from unittest.mock import patch
from src.main import main
from src.exceptions import FrameworkException

class TestMainFunction(unittest.TestCase):

    @patch('src.main.logger')
    def test_main_calls_main_function_with_invalid_input(self, mock_logger):
        # Arrange
        mock_logger.error.return_value = None

        # Act
        with self.assertRaises(FrameworkException):
            main(args='-i')

        # Assert
        mock_logger.error.assert_called_once()

    def test_main_returns_0_with_valid_input(self):
        # Act
        result = main(args='--help')

        # Assert
        self.assertEqual(result, 0)

    def test_main_returns_nonzero_with_invalid_input(self):
        # Act
        result = main(args='-i')

        # Assert
        self.assertNotEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
```

```python
# src/main.py (modifié pour inclure les tests)

import argparse
import logging
from src.exceptions import FrameworkException

def main(args=None):
    parser = argparse.ArgumentParser(description='Federated Learning Framework')
    parser.add_argument('-h', '--help', action='help', help='Affiche l\'aide')
    parser.add_argument('-i', '--invalid', action='store_true', help='Argument non valide')
    args = parser.parse_args(args)

    if args.invalid:
        raise FrameworkException('Argument non valide')

    logging.info('Fichier principal appelé')
    logging.info('Argument : %s', args)

if __name__ == '__main__':
    main()
```

```python
# src/exceptions.py (nouveau fichier)

class FrameworkException(Exception):
    pass