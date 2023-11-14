def rabin_karp_search(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    p = 0  # Hash value for the pattern
    t = 0  # Hash value for the text

    h = pow(prime, m - 1) % prime  # Hash for rolling window

    # Calculate the initial hash values
    for i in range(m):
        p = (p * prime + ord(pattern[i])) % prime
        t = (t * prime + ord(text[i])) % prime

    matches = []
    for i in range(n - m + 1):
        if p == t:  # Check if the hash values match
            if text[i:i + m] == pattern:
                matches.append(i)

        if i < n - m:
            t = (t - ord(text[i]) * h) % prime  # Remove the first character's contribution
            t = (t * prime + ord(text[i + m])) % prime  # Add the next character's contribution

    return matches

if __name__ == '__main__':
    text = "ababcababcabc"
    pattern = "abc"
    matches = rabin_karp_search(text, pattern)

    if matches:
        print(f"Pattern found at positions: {matches}")
    else:
        print("Pattern not found in the text.")
