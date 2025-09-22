"""Main module for ChatGPT Query."""

import argparse
import sys
import webbrowser
from urllib.parse import urlencode


def main():
    parser = argparse.ArgumentParser(description="ChatGPT Query Tool")
    parser.add_argument("query", nargs="*", help="Query to send to ChatGPT")
    args = parser.parse_args()

    if not args.query:
        print("No query provided. Please provide a query string. E.g. `chat Hello`.")
        sys.exit(1)

    url_params = {
        "q": " ".join(args.query),
    }
    url = f"https://chat.openai.com/?{urlencode(url_params)}"

    print(f"Opening URL: {url}")
    webbrowser.open(url)


if __name__ == "__main__":
    main()
