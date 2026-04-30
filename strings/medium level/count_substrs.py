def atMostK(s, k):
    left = 0
    count = 0
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        count += right - left + 1

    return count
s=input()
k=int(input())
print(atMostK(s, k))