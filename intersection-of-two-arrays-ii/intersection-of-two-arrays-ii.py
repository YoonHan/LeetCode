class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        selected, compared = [nums1, nums2] if len(nums1) <= len(nums2) else [nums2, nums1]
        
        answer = []
        for num in selected:
            if num in compared:
                answer.append(num)
                compared.remove(num)
        
        return answer