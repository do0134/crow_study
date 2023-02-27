class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # Set the range of possible weight capacities
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            day_count = 1
            total_weight = 0

            for weight in weights:
                total_weight += weight

                if total_weight > mid:
                    day_count += 1
                    total_weight = weight

            if day_count > D:
                left = mid + 1
            else:
                right = mid

        return left