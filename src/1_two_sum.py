#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# 1. Two Sum
# Easy

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class solution(object):
    def twoSum(self,nums,target):
        temp = {}
        for i in range(len(nums)):
            if target-nums[i] in temp:
                return [temp.get(target-nums[i]),i]
            temp[nums[i]] = i
                
# test
p = solution()
print(p.twoSum([2,11,15,7],9))