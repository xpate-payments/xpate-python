import unittest

from xpate_sdk import Xpate
from xpate_sdk.api_client import ApiClient


class XpateTest(unittest.TestCase):
    def test_it_creates_a_client(self) -> None:
        self.assertIsInstance(
            Xpate.create_client('https://www.example.com', 'abc123'),
            ApiClient
        )
