#!/usr/bin/env python3
"""unittest module"""
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

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """method totest public repos"""
        sam = {"name": "sam", "grade": {"key": "a"}}
        jack = {"name": "jack", "grade": {"key": "c"}}
        alex = {"name": "alex", "grade": {"key": "d"}}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [sam, jack, alex]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as k:
            v = GithubOrgClient("v")
            self.assertEqual(v.public_repos(), ['sam', 'jack', 'alex'])
            self.assertEqual(v.public_repos("a"), ['sam'])
            self.assertEqual(v.public_repos("e"), [])
            self.assertEqual(v.public_repos("30"), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            k.assert_called_once_with()
