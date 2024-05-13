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
