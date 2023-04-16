# python3
def get_input_from_user():
    text1 = input()
    text2 = input()
    return text1.rstrip(), text2.rstrip()


def get_input_from_file(file_path):
    with open(file_path, "r") as f:
        text1 = f.readline()
        text2 = f.readline()
    return text1.rstrip(), text2.rstrip()


def read_input():
    text = input()

    if "I" in text[:1]:
        return get_input_from_user()
    else:
        return get_input_from_file("./tests/06")


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    result = []
    hash_pattern = hash(pattern)

    for i in range(len(text) - len(pattern) + 1):
        hash_text = hash(text[i:i + len(pattern)])
        if hash_text == hash_pattern:
            if text[i:i + len(pattern)] == pattern:
                result.append(i)
    return result


def main():
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)


if __name__ == '__main__':
    main()
