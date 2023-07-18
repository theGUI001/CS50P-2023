import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str:
    match = re.search(r'<iframe[^>]*src="([^"]+)"', s)

    if match:
        url = match.group(1)

        video_id_match = re.search(r"youtube\.com/embed/([\w-]+)", url)

        if video_id_match:
            return f"https://youtu.be/{video_id_match.group(1)}"

    return None


if __name__ == "__main__":
    main()
