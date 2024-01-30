def twoSum(self, nums:list[int], target: int) -> list[int]:
    dictionary_check = {}
    i = 0
    while i < len(nums):
        spacious = target - nums[i]
        if spacious in dictionary_check:
            return [dictionary_check[spacious], i]
        dictionary_check[nums[i]] = i
        i += 1
    return "ERR"

if __name__ == '__main__':
    nums = input( f"Insert an array:[{list}]")
    target = input(f"target:{int}")
    print(twoSum(nums, target))
