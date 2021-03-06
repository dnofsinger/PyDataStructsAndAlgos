

"""
>>> testValues = [-1, 0, 3, 5, 9, 12]
>>> binarySearch( testValues, 9)
4

"""
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
