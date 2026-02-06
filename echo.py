def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real world echo."""

    # By default, echoed_strings is an empty list
    echoed_strings = []

    # Iterate over repetitions in reverse
    # Append specified substring to echoed_strings each time
    for i in reversed(range(1, repetitions + 1)):
        echoed_strings.append(text[-i:])

    # Format the output so there is a new line between list elements
    return "\n".join(echoed_strings)


if __name__ == "__main__":
    text = input("Yell something at a mountain\n")
    print(echo(text))
