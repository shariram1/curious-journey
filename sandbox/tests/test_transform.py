#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 09:50:45 2018

@author: shariram
"""

import pytest
from sandbox import transform


@pytest.fixture(params=["nodict", "dict"])
def generate_initial_transform_parameters(request):

    test_input = {
        "name": "John Q. Public",
        "street": "123 Main St.",
        "city": "Anytown",
        "state": "FL",
        "zip": 99999,
    }

    expected_output = {
        "name": "John Q. Public",
        "street": "123 Main St.",
        "city": "Anytown",
        "state": "FL",
        "zip": 99999,
    }

    if request.param == "dict":
        test_input["relationships"] = {
            "siblings": ["Michael R. Public", "Suzy Q. Public"],
            "parents": ["John Q. Public Sr.", "Mary S. Public"],
        }
        expected_output["siblings"] = ["Michael R. Public", "Suzy Q. Public"]
        expected_output["parents"] = ["John Q. Public Sr.", "Mary S. Public"]

    return test_input, expected_output


@pytest.fixture(params=["noReqKeys", "allReqKeys"])
def generate_final_transform_parameters(request):

    test_input = {
        "name": "John Q. Public",
        "siblings": ["Michael R. Public", "Suzy Q. Public"],
        "parents": ["John Q. Public Sr.", "Mary S. Public"],
    }

    expected_output = {
        "name": "John Q. Public",
        "siblings": ["Michael R. Public", "Suzy Q. Public"],
        "parents": ["John Q. Public Sr.", "Mary S. Public"],
    }

    if request.param == "allReqKeys":
        test_input.update(
            {"street": "123 Main St.", "city": "Anytown", "state": "FL", "zip": 99999}
        )
        expected_output.update(
            {
                "street": "123 Main St.",
                "city": "Anytown",
                "state": "FL",
                "zip": 99999,
                "address": "123 Main St.\nFL, Anytown 99999",
            }
        )

    return test_input, expected_output


def test_initial_transform(generate_initial_transform_parameters):
    test_input = generate_initial_transform_parameters[0]
    expected_output = generate_initial_transform_parameters[1]
    assert transform.initial_transform(test_input) == expected_output


def test_final_transform(generate_final_transform_parameters):
    test_input = generate_final_transform_parameters[0]
    expected_output = generate_final_transform_parameters[1]
    assert transform.final_transform(test_input) == expected_output
