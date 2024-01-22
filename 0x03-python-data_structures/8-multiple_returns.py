#!.usr/bin/python3

def multiple_returns(sentence):
    ret_tuple = ()

    if len(sentence) == 0:
        ret_tuple = (len(sentence), None)
    ret_tuple = (len(sentence), sentence[0])
    return (ret_tuple)
