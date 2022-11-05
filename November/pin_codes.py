# https://www.codewars.com/kata/5b02ae6aa2afd8f1b4001ba4/train/python
"""
Task:
Peter enjoys taking risks, and this time he has decided to take it up a notch!

Peter asks his local barman to pour him n shots, after which Peter then puts laxatives 
in x of them. He then turns around and lets the barman shuffle the shots. 
Peter approaches the shots and drinks a of them one at a time. 
Just one shot is enough to give Peter a runny tummy.
What is the probability that Peter doesn't need to run to the loo?

Test: 

test.assert_equals(get_chance(2, 1, 1), 0.5)
test.assert_equals(get_chance(4, 1, 3), 0.25)
test.assert_equals(get_chance(100, 10, 10), 0.33)
test.assert_equals(get_chance(1000, 150, 20), 0.04)
test.assert_equals(get_chance(25, 5, 5), 0.29)
test.assert_equals(get_chance(9, 3, 2), 0.42)
"""

def get_chance_loo(n, x, a):
    prob = 1.0
    # sum the probabilities a times
    for i in range(a):
        """
        This will calculate the probability of not goint to the loo
        n - x - i: 
            From all dring we will remove all "infected"
            And (-i) 
        """
        prob *= (n - x - i)/(n - i)
    return print(round(prob, 2))


get_chance_loo(9, 3, 2)