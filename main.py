import os

TEXT = (
    "Picture a post road of wire joining every town on earth, where a man may "
    "in one breath send a letter across the sea or open any book in the "
    "library of the world and read it without leaving his chair."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
