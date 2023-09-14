import unittest

from mle.main import prompt_executor


class Tests(unittest.TestCase):
    def test_prompt_response_expected_is_instance(self):
        # Arrange
        prompt = "Como começar a investir?"
        # Act
        response = prompt_executor(prompt)
        # Assert
        self.assertIsInstance(response, str)

    def test_prompt_response_expected_true(self):
        # Arrange
        prompt = "Sobre o que podemos falar?"
        # Act
        response = prompt_executor(prompt)
        # Assert
        self.assertTrue(response.strip())  # Verifique se não está em branco
