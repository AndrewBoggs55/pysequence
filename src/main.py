import argparse
import wavedrom


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    svg = wavedrom.render(r"""
    {"signal": [
        {"name" : "Power 1", "wave" : "l..h..."},
        {"name" : "Power 2", "wave" : "l...h.."},
        {"name" : "Power 3", "wave" : "l....h."},
        {"name" : "Power 4", "wave" : "l....h."},
        {"name" : "Power 5", "wave" : "l.....h"}
    ]}
    """)

    svg.saveas(args.out)


if __name__ == "__main__":
    main()
