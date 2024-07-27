# Desafio 1 da Leetcode.com

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they 
# add up to target.

# You may assume that each input would have exactly 
# one solution, and you may not use the same 
# element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
                    

# Essa não é a solução mais rápida, pois ela tem 
# runtime de 2133ms e usa 12,6MB de memória, porém, 
# é extremamente simples, usa um laço For pra passar 
# pelsd posições i e outro pra passar pelas posições j, 
# depois um IF pra verificar em quais posições estavam 
# os números que foram usados para compor o target.