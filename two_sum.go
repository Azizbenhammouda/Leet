package leet

func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for h := i + 1; h < len(nums); h++ {
			if nums[i]+nums[h] == target {
				return []int{i, h}
			}
		}
	}
	return nil
}
