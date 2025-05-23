class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # number : index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

##Here we use hashmaps coz the answer we are getting is values but we needa get the index, accha so here what we do is store index as value and number as key, 
##ABout hashmaps, if we wan the key then we just say the number directly but if we want the value of the number (key)  we Say map(complement)
        
