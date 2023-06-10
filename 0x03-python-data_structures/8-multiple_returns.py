#!/usr/bin/python3

def multiple_returns(sentence):
    for i in range(len(sentence)):
        if sentence:
            return(len(sentence), sentence[i])
        else:
            return(None, None)
