# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
# O(n) time | O(1) Space
def productSum(array, multiplier=1):
    """
    Write a function that takes in a "special" array and returns its product sum. A "special" array is a non-empty
    array that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of
    its elements, where "special" arrays inside it are summed themselves and then multiplied by their level of depth.
    """
    total = 0
    for num in array:
        if type(num) == list:
            total += productSum(num, mul + 1)
        else:
            total += num
    return total * mul