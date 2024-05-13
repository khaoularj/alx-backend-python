#!/usr/bin/env python3
"""unittest"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock
from unittest import TestCase, mock


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


class TestMemoize(unittest.TestCase):
    """this class test the memoize funcion"""
    class TestClass:
        """this class test memoization"""
        def a_method(self):
            """method that return 42"""
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    with patch.object(TestClass, 'a_method', return_value=42) as patched:
        test_class = TestClass()
        result = test_class.a_property
        result = test_class.a_property

        self.assertEqual(result, 42)
        patched.assert_called_once()
