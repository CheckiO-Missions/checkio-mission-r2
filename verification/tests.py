"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [['p1', 'p1', 'p1', 'p3', 'p4']],
            "answer": False,
            "explanation": 'Incorrect number of arguments'
        },
        {
            "input": [['s1', 's2', 's3', 's4', 's4', 's4', 's5', 's5', 's6', 's6', 's6', 's7', 's8', 's9']],
            "answer": True,
            "explanation": 'No, this is right hand!'
        },
        {
            "input": [['m6', 'm8', 'm9', 'p1', 'p1', 'p1', 'p7', 'p8', 'p9', 's9', 's9', 's9', 'dw', 'dw']],
            "answer": False,
            "explanation": 'There mustn't be alone tiles!'
        },
        {
            "input": [['m6', 'm8', 'm9', 'p1', 'p1', 'p1', 'p7', 'p8', 'p9', 'dw', 'dw'], ['s999']],
            "answer": True,
            "explanation": 'Right hand'
        },
        {
            "input": [['m6', 'm8', 'm9', 'p1', 'p1', 'p1', 'p7', 'p8', 'p9'], ['s999', 'dww']],
            "answer": False,
            "explanation": 'Pair can't be open'
        },
        {
            "input": [['p1', 'p1', 'p5', 'p5', 'm2', 'm2', 'm6', 'm6', 's3', 's3', 's9', 's9', 'ww', 'ww']],
            "answer": False,
            "explanation": 'Yes, this is chitoisu!'
        }
    ],
    "Extra": [
        {
            "input": [['p1', 'p1', 'p1', 'p1', 'm2', 'm2', 'm6', 'm6', 's3', 's3', 's6', 's6', 's7', 's7']],
            "answer": False,
            "explanation": 'Two identical pairs in the chitoisu...'
        },
        {
            "input": [['p1', 'p9', 's1', 's9', 'm1', 'm9', 'dw', 'dg', 'dr', 'ww', 'we', 'ws', 'wn', 's9'],
            "answer": True,
            "explanation": 'Kokushi-muso'
        },
        {
            "input": [['p1', 'p9', 's1', 's9', 'm1', 'm9', 'ww', 'we', 'ws', 'wn'], ['dwrg']],
            "answer": False,
            "explanation": 'No, this is not kokushi'
        },
        {
            "input": [['p1', 'p1', 'p1', 'p2', 'p2', 'p2', 'p3', 'p3', 'p3', 'p4', 'p4', 'p4', 'p5', 'p5']],
            "answer": True,
            "explanation": 'How many ways are there to break this hand into sets?...'
        },
        {
            "input": [['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'p1', 'p1']['weeg']],
            "answer": False,
            "explanation": 'Incorrect open set. Absolutely incorrect.'
        },
        {
            "input": [['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'p1', 'p1'], ['p222']],
            "answer": True,
            "explanation": 'Correct open set.'
        },
        {
            "input": [['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'p1', 'p1'], ['p111']],
            "answer": False,
            "explanation": 'Two many same tiles.'
        },
        {
            "input": [['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'p1', 'p1'], ['p1111']],
            "answer": False,
            "explanation": 'Incorrect open set 2'
        },
        {
            "input": [['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'p1', 'p1'], ['p123']],
            "answer": True,
            "explanation": 'Correct open set 2...'
        },
        {
            "input": [['s1', 's2', 's3', 's4', 's5', 's6', 'p1', 'p1'], ['p123', 's789']],
            "answer": True,
            "explanation": 'Several open sets'
        },
        {
            "input": [['s1', 's2', 's3', 's4', 's5', 's6', 'p1', 'p1'], ['p123', 's781']],
            "answer": True,
            "explanation": 'Incorrect several open sets'
        }
    ]
}
