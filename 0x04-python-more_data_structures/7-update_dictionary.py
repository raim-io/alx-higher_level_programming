#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """replaces or adds key/value in a dictionary.
    @key: dctionary key (always string itc)
    @value: new key-pair value (any type)
    """

    a_dictionary[key] = value

    return a_dictionary
