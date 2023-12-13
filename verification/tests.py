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
            "input": [['p1', 'p1', 'p1', 'p3', 'p4']],
            "answer": False,
            "explanation": 'Two identical pairs in the chitoisu...'
        },
        {
            "input": [['p1', 'p1', 'p1', 'p3', 'p4']],
            "answer": False,
            "explanation": 'Kokushi-muso'
        },
        {
            "input": [['p1', 'p1', 'p1', 'p3', 'p4']],
            "answer": False,
            "explanation": 'No, this is not kokushi'
        },
        {
            "input": [['p1', 'p1', 'p1', 'p3', 'p4']],
            "answer": False,
            "explanation": 'Incorrect number of arguments'
        }
    ]
}
