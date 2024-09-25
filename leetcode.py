# EASY PROBLEMS [9/28 Complete]

def two_sum(nums, target):
    mydict = {}
    for i in range(len(nums)):
        if target - nums[i] in mydict:
            return [mydict[target - nums[i]], i]
        mydict[nums[i]] = i 

def contains_duplicates(nums):
    numbers = set()
    for i in nums:
        if i in numbers:
            return True
        numbers.add(i)
    return False 

def missing_number(nums):
    left, right = 0, len(nums)
    nums.sort()
    while left <= right:
        if nums[left] != left:
            return left 
        if nums[right - 1] != right:
            return right  
        left += 1
        right -= 1
    return -1 

def plus_one(digits):
    last = len(digits) - 1
    if digits[last] != 9:
        digits[last] += 1
        return digits 
    while digits[last] == 9:
        digits[last] = 0
        last -= 1
    if digits[last] == 0:
        return [1] + digits 
    digits[last] += 1    
    return digits 

def happy_number(n):
    hset = set() 
    while n != 1:
        digit = 0 
        for i in str(n):
            digit += (int(i)**2) 
        if digit in hset:  
            return False 
        hset.add(digit)
        n = digit  
    return True 

def hammingWeight(n):
    count = 0
    for i in bin(n):
        if i == "1":
            count += 1
    return count

def countBits(n):
    output = []
    for i in range(n + 1):
        output.append(bin(i).count("1")) 
    return output

def isValid(s):
    mydict = {"]":"[", ")":"(", "}":"{"} 
    stack = []
    for i in s:
        if i in mydict and stack and stack[-1] == mydict[i]:
            stack.pop() 
        else:
            stack.append(i) 
    return len(stack) == 0 

def isAnagram(s, t):
    return sorted(s) == sorted(t) 