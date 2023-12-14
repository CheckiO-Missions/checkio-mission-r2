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
            "input": [['p1', 'p1', 'p3', 'p1', 'p4'], []],
            "answer": False,
            "explanation": 'Incorrect number of tiles'
        },
        {
            "input": [['s4', 's3', 's2', 's8', 's4', 's1', 's5', 's6', 's5', 's4', 's7', 's9', 's6', 's6'], []],
            "answer": True,
            "explanation": 'No, this is right hand!'
        },
        {
            "input": [['s9', 'p1', 'p1', 'm8', 'dw', 'dw', 'p8', 'm9', 'p7', 'p9', 's9', 'p1', 's9', 'm6'], []],
            "answer": False,
            "explanation": "There mustn't be alone tiles!"
        },
        {
            "input": [['dw', 'p7', 'p9', 'dw', 'm7', 'p8', 'm8', 'p1', 'p1', 'p1', 'm9'], ['s999']],
            "answer": True,
            "explanation": 'Right hand'
        },
        {
            "input": [['p1', 'p9', 'p1', 'p8', 'p1', 'm8', 'm7', 'p7', 'm9'], ['s999', 'dww']],
            "answer": False,
            "explanation": "Pair can't be open"
        },
        {
            "input": [['s9', 'm2', 's9', 'p1', 'm6', 's3', 'm6', 'p5', 'm2', 'ww', 'ww', 'p1', 's3', 'p5'], []],
            "answer": True,
            "explanation": 'Yes, this is chitoisu!'
        }
    ],
    "Extra": [
        {
            "input": [['m6', 's7', 'm2', 's6', 'm2', 's3', 'p1', 's6', 's7', 's3', 'm6', 'p1', 'p1', 'p1'], []],
            "answer": False,
            "explanation": 'Two identical pairs in the chitoisu...'
        },
        {
            "input": [['s9', 'wn', 's9', 's1', 'dw', 'we', 'p1', 'm1', 'p9', 'dg', 'm9', 'dr', 'ws', 'ww'], []],
            "answer": True,
            "explanation": 'Kokushi-muso'
        },
        {
            "input": [['p9', 's9', 'p1', 'ww', 'ws', 'm9', 's1', 'we', 'm1', 'wn'], ['dwrg']],
            "answer": False,
            "explanation": 'No, this is not kokushi'
        },
        {
            "input": [['p1', 'p1', 'p5', 'p2', 'p5', 'p1', 'p4', 'p4', 'p3', 'p3', 'p4', 'p3', 'p2', 'p2'], []],
            "answer": True,
            "explanation": 'How many ways are there to break this hand into sets?...'
        },
        {
            "input": [['p1', 's1', 's8', 's7', 's9', 'p1', 's5', 's4', 's6', 's3', 's2'], ['weeg']],
            "answer": False,
            "explanation": 'Incorrect open set. Absolutely incorrect.'
        },
        {
            "input": [['p1', 'p1', 's7', 's1', 's6', 's9', 's8', 's5', 's3', 's4', 's2'], ['p222']],
            "answer": True,
            "explanation": 'Correct open set.'
        },
        {
            "input": [['s4', 's1', 's9', 'p1', 's3', 's8', 's6', 's2', 's7', 's5', 'p1'], ['p111']],
            "answer": False,
            "explanation": 'Two many same tiles.'
        },
        {
            "input": [['s9', 'p1', 's7', 's8', 's6', 's3', 's1', 'p1', 's5', 's2', 's4'], ['p1111']],
            "answer": False,
            "explanation": 'Incorrect open set 2'
        },
        {
            "input": [['p1', 's5', 's8', 's9', 's7', 's4', 's2', 's6', 's3', 's1', 'p1'], ['p123']],
            "answer": True,
            "explanation": 'Correct open set 2...'
        },
        {
            "input": [['s2', 's1', 's6', 's4', 's3', 's5', 'p1', 'p1'], ['p123', 's789']],
            "answer": True,
            "explanation": 'Several open sets'
        },
        {
            "input": [['s1', 's6', 'p1', 'p1', 's2', 's4', 's3', 's5'], ['p123', 's781']],
            "answer": False,
            "explanation": 'Incorrect several open sets'
        }
    ]
}
