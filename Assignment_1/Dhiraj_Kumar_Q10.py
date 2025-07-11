def second_largest(nums):
    """
    Return the second largest unique number in the list.
    If it doesn’t exist, return None.
    """
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]
print(second_largest([2,5,1,4,5]))    # 4
print(second_largest([7,7,7]))    # None
print(second_largest([10,9,8]))    # 9