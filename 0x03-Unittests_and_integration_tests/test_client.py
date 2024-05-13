#!/usr/bin/env python3
"""unittest module"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_res):
        """method to test has_license method"""
        key_expected = GithubOrgClient.has_license(
            repo, license_key, expected_res)
        self.assertEqual(key_expected, expected_res)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """class that test for github org client """
    @classmethod
    def setUpClass(cls):
        """method to set up test environment"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [MagicMock(json=lambda: cls.org_payload),
                                    MagicMock(json=lambda: cls.repos_payload)]

    @classmethod
    def tearDownClass(cls):
        """method totest public repos"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """method to test public repos"""
        client = GithubOrgClient('testorg')
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_has_license(self):
        """method to test has license"""
        client = GithubOrgClient('testorg')
        has_apache2_license = client.has_license('Apache-2.0')
        self.assertEqual(has_apache2_license, self.apache2_repos)
