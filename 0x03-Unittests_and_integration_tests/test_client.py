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
    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license"),
    ])
    def test_has_license(self):
