"""Office joke entry: writes one one-line office joke to /output/entry.txt."""

import os

JOKE = "I asked IT for a faster laptop and got a motivational poster about patience."


def main():
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert JOKE.strip() == JOKE and "\n" not in JOKE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
