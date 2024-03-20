def ascii_hash(input: str) -> str:
    result = 0
    for c in input:
        result += ord(c)
    return str(result)

