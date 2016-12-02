#!/usr/bin/env python3

# Weighted Random Pick
#
# implementor : Pierre Faivre
# date : 2016-12-02
#
# complexity : O(n)

def randpck(elements, rand_function):
    """Pick an element from the dict based on their weight
    @param elements List with elements and their weight (positive value). 
    Example : 
        [
            (obj1, 10),
            (obj2, 5.2),
            (obj3, 15)
        ]
    @param rand_function Reference to the function used to get a random floating
     point number in the range [0.0, 1.0)
    @returns The object from the picked element
    """

    # First, we commpute the total weight (for example 10)
    total_weight = 0
    for e in elements:
        assert e[1] >= 0
        total_weight += e[1]


    # Then we generate a random number multiplied by the total weight (e.g. 0.4218 * 10 = 42.18)
    random_weight = rand_function() * total_weight
    

    # Lastly, we run throught the list to find which one matches with the generated weight
    current_weight = 0;
    for e in elements:
        current_weight += e[1]
        if random_weight < current_weight:
            return e[0]

    return None
