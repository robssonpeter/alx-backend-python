#!/usr/bin/env python3
import unittest
from utils import access_nested_map
from parameterized import parameterized
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
