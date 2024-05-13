#!/usr/bin/env python3
"""unittest"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class that test cases for GithubOrgClient"""
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, name, mock_get_json):
        """method to test that
        GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = {'name': name}
        client = GithubOrgClient(name)
        result = client.org
        url = f'https://api.github.com/orgs/{org_name}'
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, {'name': name})
