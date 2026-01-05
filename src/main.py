import argparse
import wavedrom


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    svg = wavedrom.render(r"""
    {"signal": [
        ["Default",
            {"name" : "Power 1", "wave" : "l..h..."}
        ],
        ["PG_P12V_BUSBAR_EF",
            {"name" : "Power 2", "wave" : "l...h.."}
        ],
        ["POR_VPD_RESET (12 sec delay)",
            {"name" : "Power 3", "wave" : "l....h.", "node" : .....3."},
            {},
            {"name" : "P12V_SYS_SW_[0:1]", "wave" : "l....h."}
        ],
        {"name" : "Power 4", "wave" : "l.....h", "node" : "......4"},
        {"name" : "Power 5", "wave" : "l.....h"}
    ],
    "edge" : [
        '3~>4 12s delay'
    ],
    "head" : {
        "text" :
        ["tspan",
            {"class" : "success h4"}, "SC2 Power Sequence"]
    },
    "foot" : {
        "text" : "Figure 1",
        "tock" : 1
    },
    }
    """)

    svg.saveas(args.out)


if __name__ == "__main__":
    main()
