def longest_non_repeat(s):
    start, maxlen = 0, 0
    used_char = {}
    for i, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            maxlen = max(maxlen, i-start+1)
        used_char[char] = i
    return maxlen


if __name__ == "__main__":
    a = "abcabacefbb"
    print(a)
    max_len = longest_non_repeat(a)
    print(max_len)
