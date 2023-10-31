#!/usr/bin/env python3
import unittest
from utils import access_nested_map
from utils import requests
from utils import get_json
from parameterized import parameterized
from unittest.mock import MagicMock, patch
from typing import Mapping
""" The testing class for the module utils"""


class TestAccessNestedMap(unittest.TestCase):
    """ The class itself for testing utils"""

    @parameterized.expand([
        ([{"a": 1}, ("a",)], 1),
        ([{"a": {"b": 2}}, ("a",)], {"b": 2}),
        ([{"a": {"b": 2}}, ("a", "b")], 2)
    ])
    def test_access_nested_map(self, input, expected):
        output = access_nested_map(input[0], input[1])
        return self.assertEqual(output, expected)
    
    """@parameterized.expand([
        ({"nested_map":{}, "path":("a",)},),
        ({"nested_map":{"a": 1}, "path":("a", "b")},),
    ])
    def test_access_nested_map_exception(self, input):
        nested_map = input['nested_map']
        iter = 0
        for key in input['path']:
            if not isinstance(nested_map, Mapping):
                paths = input['path'][iter:]
                self.assertRaises(KeyError(key), access_nested_map(nested_map, paths))
            nested_map = nested_map[key]
            iter = iter + 1"""

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, input, output, mocked):
        mocked.json.return_value = output
        mock = get_json(input)
        mock.__call__(url=input)
        mock.assert_called_once_with(url=input)
