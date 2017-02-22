#
# File:        ProductExcept.py
# Created by:  Tim Shur
# Date:        2/21/17
#
# Description: This program takes an array of n integers, nums, and returns an array
#              output such that output[i] equals the product of all nums except nums[i].
#              This product does not use division, but instead maintains two product terms
#              from each end and multiplies them into the product. This takes two passes of
#              the array.
#
# Big-O complexity: O(n) with two passes of the nums array.
#


def product_except(nums):
    output = []

    # forward pass through nums, maintaining running_product
    running_product = 1
    for i in range(len(nums)):
        output.append(running_product)
        running_product *= nums[i]

    # reverse pass through nums, maintaining running_product
    running_product = 1
    for i in range(1, len(nums) + 1):
        output[-i] *= running_product
        running_product *= nums[-i]

    return output

args = [1, 2, 3, 4]
print(product_except(args))
