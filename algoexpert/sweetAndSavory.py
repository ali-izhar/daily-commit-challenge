"""
PROBLEM STATEMENT:
You're hosting an event at a food festival and want to showcase the best possible pairing of sweet and savory foods.

Each dish has a favor profile represented by an integer. A negative integer means a dish is sweet, while a positive integer means a dish is savory. The absolute value of the integer represents the strength of the dish's flavor profile.

You're given an array of these dishes and a target combined favor profile. Write a function that returns the pair of dishes that have the closest combined flavor profile to the target flavor profile. The function should return an array containing the two dishes in any order. If multiple pairs have the same combined flavor profile, you can return any of them.

If there isn't a pair that is within the target flavor profile, the function should return [0, 0].
"""

# Time: O(nlogn) | Space: O(n)
def sweetAndSavory(dishes, target):
    """Intuition:
    - We can solve this problem using the two-pointer technique
    - First, we sort the dishes array
    - We then initialize two pointers, left and right, to the start and end of the array
    - We also initialize two variables, minDiff and closestPair, to keep track of the minimum difference and the closest pair of dishes
    - We then iterate through the array using the two pointers
    - At each iteration, we calculate the combined flavor profile of the two dishes
    - If the combined flavor profile is equal to the target, we return the two dishes
    - Otherwise, we update the minDiff and closestPair if the combined flavor profile is closer to the target
    - If the combined flavor profile is less than the target, we increment the left pointer
    - If the combined flavor profile is greater than the target, we decrement the right pointer
    - At the end, we return the closestPair
    """
    dishes.sort()
    left = 0
    right = len(dishes) - 1
    minDiff = float('inf')
    closestPair = [0, 0]
    while left < right:
        combined = dishes[left] + dishes[right]
        if combined == target:
            return [dishes[left], dishes[right]]
        elif abs(combined - target) < minDiff:
            minDiff = abs(combined - target)
            closestPair = [dishes[left], dishes[right]]
        if combined < target:
            left += 1
        else:
            right -= 1
    return closestPair

# Time: O(nlogn) | Space: O(n)
def sweetAndSavory(dishes, target):
    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savoryDishes = sorted([dish for dish in dishes if dish > 0])

    bestPair = [0, 0]
    bestDiff = float('inf')
    sweetIndex, savoryIndex = 0, 0

    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes):
        currentSum = sweetDishes[sweetIndex] + savoryDishes[savoryIndex]

        if currentSum <= target:
            currentDiff = target - currentSum
            if currentDiff < bestDiff:
                bestDiff = currentDiff
                bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]
            savoryIndex += 1
        else:
            sweetIndex += 1
    return bestPair