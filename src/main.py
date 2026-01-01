import wavedrom

svg = wavedrom.render("""  # Creates a class of wavedrom render
    {
    "config" : {
        "bgcolor": "white"
    },
    "signal": [
        {"name" : "Power 1", "wave" : "l..h..."},
        {"name" : "Power 2", "wave" : "l...h.."},
        {"name" : "Power 3", "wave" : "l....h."},
        {"name" : "Power 4", "wave" : "l....h."},
        {"name" : "Power 5", "wave" : "l.....h"}
    ]
    }
""")

svg.saveas("power_sequence.svg")
