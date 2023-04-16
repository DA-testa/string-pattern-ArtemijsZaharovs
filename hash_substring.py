# python3
def read_input():
    iorf = input().rstrip()
    if iorf == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
        return(pattern, text)
    if iorf == 'F':
        with open("test_sample.txt", 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
            return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    
    occurrences = []
    z = 256
    q = 101
    v = len(pattern)
    n = len(text)
    o = pow(z, v - 1) % q
    p = 0
    t = 0

    for i in range(v):
        p = (z * p + ord(pattern[i])) % q
        t = (z * t + ord(text[i])) % q

    for s in range(n - v + 1):
        if p == t:
            if text[s:s + v] == pattern:
                occurrences.append(s)

        if s < n - v:
            t = (z * (t - ord(text[s]) * o) + ord(text[s + v])) % q

            if t < 0:
                t += q

    return occurrences

if __name__ == '__main__':
    occurrences = get_occurrences(*read_input())
    print_occurrences(occurrences)
