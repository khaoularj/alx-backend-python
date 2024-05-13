#!/usr/bin/env python3
"""unittest"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, result):
        """method to test that the method returns what it is supposed to"""
        output = access_nested_map(map, path)
        self.assertEqual(output, result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, unexpected_output):
        """method that test exception raising"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(unexpected_output, e.exception)


class TestGetJson(unittest.TestCase):
    """this class test utils.get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """method that returns correct output """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_response.json.assert_called_once()
