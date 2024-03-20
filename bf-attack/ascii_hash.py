def ascii_hash(input: str) -> str:
    result = ""
    for c in input:
        result += str(ord(c))
    return result

