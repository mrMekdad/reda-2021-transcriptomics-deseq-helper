import argparse
from transcriptomics_deseq_helper.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Helpers to prepare count matrices, contrasts, and downstream result packs.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
