import unittest
from unittest.mock import patch
from client import GithubOrgClient
from client import get_json
from parameterized import parameterized
""" The module for testing client.py"""


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ('google', ),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mocked):
        mocked.return_value = 'done'
        client = GithubOrgClient(input)
        
        output = f'https://api.github.com/orgs/{input}'
        self.assertEqual(client.ORG_URL, output)
        