import unittest
from client import GithubOrgClient
""" The module for testing client.py"""


class TestGithubOrgClient(unittest.TestCase):
    def test_org(self):
        client = GithubOrgClient("parker")
        output = 'https://api.github.com/orgs/parker'
        self.assertEqual(client.ORG_URL, output)