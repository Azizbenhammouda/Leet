package leet

import "strconv"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	str := strconv.Itoa(x)
	n := len(str)
	var str1 string
	for i := n - 1; i > -1; i-- {
		str1 += string(str[i])
	}
	return str1 == str
}
