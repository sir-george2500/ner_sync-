import unittest
from ner_client import NameEntityClient


class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string(self):
        ner = NameEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)
