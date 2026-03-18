def longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    longest_sub = ""

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        if right - left + 1 > max_length:
            max_length = right - left + 1
            longest_sub = s[left:right+1]

    return max_length, longest_sub


s = input("Enter a string: ")

length, substring = longest_substring(s)

print("Longest substring without repeating characters:", substring)
print("Length:", length)