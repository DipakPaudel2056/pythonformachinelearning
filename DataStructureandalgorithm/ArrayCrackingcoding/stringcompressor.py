# aaaaabbbcccaa
# should return
# a5b3c3a2

def compress_string(s):
    if not s:
        return ""
    
    compressed = ""
    count = 1
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i]
            if count > 1:
                compressed += str(count)
            count = 1
    
    return compressed if len(compressed) < len(s) else s

print(compress_string("aaabbbcccdde"))