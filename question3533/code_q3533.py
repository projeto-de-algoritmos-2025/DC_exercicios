class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()
        memo = {}
        potencias_10 = [(10**len(str(num))) % k for num in nums]
        restos_nums = [num % k for num in nums]
        def solve(mask: int, remainder: int) -> List[int] | None:
            if mask == (1 << n) - 1:
                return [] if remainder == 0 else None
            if (mask, remainder) in memo:
                return memo[(mask, remainder)]
            for i in range(n):
                if not (mask & (1 << i)):
                    new_remainder = (remainder * potencias_10[i] + restos_nums[i]) % k
                    result_suffix = solve(mask | (1 << i), new_remainder)
                    if result_suffix is not None:
                        solution = [nums[i]] + result_suffix
                        memo[(mask, remainder)] = solution
                        return solution
            memo[(mask, remainder)] = None
            return None
        final_result = solve(0, 0)
        return final_result if final_result is not None else []
