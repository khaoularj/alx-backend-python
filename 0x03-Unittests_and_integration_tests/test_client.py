#!/usr/bin/env python3
"""unittest"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class that test cases for GithubOrgClien"""
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
        url = 'https://api.github.com/orgs/{}'.format(name)
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, {'name': name})

    def test_public_repos_url(self):
        """method to unit-test GithubOrgClient._public_repos_url"""
        url_payload = {
            'repos_url': 'https://api.github.com/orgs/testorg/repos'
        }
        with patch.object(
            GithubOrgClient, 'org', new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = url_payload
            client = GithubOrgClient('testorg')
            result = client._public_repos_url
            url_1 = 'https://api.github.com/orgs/testorg/repos'
            self.assertEqual(result, url_1)