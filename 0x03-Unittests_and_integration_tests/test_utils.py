#!/usr/bin/env python3
""" The testing class for the module utils """
import unittest
from utils import access_nested_map
from utils import requests
from utils import get_json
from utils import memoize
from parameterized import parameterized
from unittest.mock import MagicMock, patch
from typing import Mapping


class TestAccessNestedMap(unittest.TestCase):
    """ The class itself for testing utils """

    @parameterized.expand([
        ([{"a": 1}, ("a",)], 1),
        ([{"a": {"b": 2}}, ("a",)], {"b": 2}),
        ([{"a": {"b": 2}}, ("a", "b")], 2)
    ])
    def test_access_nested_map(self, input, expected):
        output = access_nested_map(input[0], input[1])
        return self.assertEqual(output, expected)


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


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        mock = MagicMock(spec=TestClass)
        mock.__call__()
        mock.a_method()
        mock.a_method()
        mock.assert_called_once()
        """ patch('TestClass', test)
        test.a_method """
