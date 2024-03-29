"""
Given an array of integers. Return an array, 
where the first element is the count of positives 
numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array.
"""

def count_positives_sum_negatives(arr):
    count_positive = 0
    sum_negative = 0
    if len(arr) != 0:
        for element in arr:
            if element > 0:
                count_positive = count_positive + 1
            if element < 0:
                sum_negative = sum_negative + element   
        array = [count_positive, sum_negative]
    elif len(arr) == 0:
        array = []
    print (array)
    return(array)

count_positives_sum_negatives([5,6,2,3,4,5,-3,-3,-8,7])
