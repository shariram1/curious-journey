#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:33:53 2018

@author: shariram
"""
from random import choice

def initial_transform(data):
    """
    Flatten nested dicts
    """
    for item in list(data):
        if type(data[item]) is dict:
            for key in data[item]:
                data[key] = data[item][key]
            data.pop(item)

    choicevalue = do_something()
    print (choicevalue)
    return data


def final_transform(transformed_data):
    """
    Transform address structures into a single structure
    """
    if (
        'street' in transformed_data
        and 'state' in transformed_data
        and 'city' in transformed_data
        and 'zip' in transformed_data
        ) :
        transformed_data['address'] = str.format(
                "{0}\n{1}, {2} {3}",
                transformed_data['street'],
                transformed_data['state'],
                transformed_data['city'],
                transformed_data['zip']
        )

    return transformed_data


def print_person(person_data):
    parents = " and ".join(person_data['parents'])
    siblings = " and ".join(person_data['siblings'])
    person_string = str.format(
        "Hello, my name is {0}, my siblings are {1}, "
        "my parents are {2}, and my mailing"
        "address is: \n{3}", person_data['name'],
        parents, siblings, person_data['address'])
    print(person_string)


def do_something():
    return choice([1,2])


john_data = {
    'name': 'John Q. Public',
    'street': '123 Main St.',
    'city': 'Anytown',
    'state': 'FL',
    'zip': 99999,
    'relationships': {
        'siblings': ['Michael R. Public', 'Suzy Q. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
    }
}

suzy_data = {
    'name': 'Suzy Q. Public',
    'street': '456 Broadway',
    'apt': '333',
    'city': 'Miami',
    'state': 'FL',
    'zip': 33333,
    'relationships': {
        'siblings': ['John Q. Public', 'Michael R. Public',
                    'Thomas Z. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
    }
}

def main():
    inputs = [john_data, suzy_data]
    for input_structure in inputs:
        initial_transformed = initial_transform(input_structure)
        final_transformed = final_transform(initial_transformed)
        print_person(final_transformed)

if __name__ == '__main__':
    main()