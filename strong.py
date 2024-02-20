def naive_search(text, pattern):
    indexes = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            indexes.append(i)
    return indexes
text = "abcaabccbcc"
pattern = "bc"
result = naive_search(text, pattern)
print(result)
