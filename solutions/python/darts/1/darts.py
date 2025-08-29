"""
Functions to calculate the points scored in a single toss of a Darts game.

Darts is a game where players throw darts at a target.
In our particular instance of the game, the target rewards 4 different amounts of points, depending on where the dart lands:
"""

outter_radius = 10
middle_radius = 5
inner_radius = 1

def score(x, y):
    ''' Calculates the given score with the given coordinates of the arrow
    :param x: real - given x cartesian coordinate
    :param y: real - given y cartesian coordinate

    1. 0 points: If the dart lands outside the target
    2. 1 point: If the dart lands in the outer circle of the target
    3. 5 points: If the dart lands in the middle circle of the target
    4. 10 points: If the dart lands in the inner circle of the target

    Outter radius 10 units
    Middle radius 5 units
    Inner radius 1 unit

    Use circle equation (x – xM)² + (y – yM)² = r²; with xM and yM equals center of circle

    IF x² + y² <= r² then arrow in circle
    '''

    if x**2 + y**2 <= inner_radius**2: return 10
    if x**2 + y**2 <= middle_radius**2: return 5
    if x**2 + y**2 <= outter_radius**2: return 1
    
    return 0
    