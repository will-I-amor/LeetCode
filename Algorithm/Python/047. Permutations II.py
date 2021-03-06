# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-06 16:13:16
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-06 16:15:29
# @Email: liangchaowu5@gmail.com

# 直接进行排列，注意从后往前插入数字，从前往后会出错
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            new_result = []
            for seq in result:
                n = len(seq)
                for i in xrange(n,-1,-1):
                    if i < n and seq[i] == num:
                        break
                    new_result.append(seq[:i]+[num]+seq[i:])
            result = new_result
        return result
                        
        