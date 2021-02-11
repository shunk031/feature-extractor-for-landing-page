import argparse
import pathlib


def main():
    parser = argparse.ArgumentParser(
        prog="felp", description="Feature extractor for Japanese landing page."
    )
    parser.add_argument("html-file", type=pathlib.Path, help="Path to html file")
    print(parser.parse_args())


if __name__ == "__main__":
    main()
