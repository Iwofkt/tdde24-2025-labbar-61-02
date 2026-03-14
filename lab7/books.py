# Encoding: ISO-8859-1

db = [
    [
        ["f�rfattare", ["john", "zelle"]],
        [
            "titel",
            [
                "python",
                "programming",
                "an",
                "introduction",
                "to",
                "computer",
                "science",
            ],
        ],
        ["�r", 2010],
    ],
    [
        ["f�rfattare", ["armen", "asratian"]],
        ["titel", ["diskret", "matematik"]],
        ["�r", 2012],
    ],
    [
        ["f�rfattare", ["j", "glenn", "brookshear"]],
        ["titel", ["computer", "science", "an", "overview"]],
        ["�r", 2011],
    ],
    [
        ["f�rfattare", ["john", "zelle"]],
        [
            "titel",
            [
                "data",
                "structures",
                "and",
                "algorithms",
                "using",
                "python",
                "and",
                "c++",
            ],
        ],
        ["�r", 2009],
    ],
    [
        ["f�rfattare", ["anders", "haraldsson"]],
        ["titel", ["programmering", "i", "lisp"]],
        ["�r", 1993],
    ],
]

pattern = [
    [
        ["f�rfattare", ["john", "zelle"]],
        [
            "titel",
            [
                "python",
                "programming",
                "an",
                "introduction",
                "to",
                "computer",
                "science",
            ],
        ],
        "--",
    ],
    [["f�rfattare", ["armen", "asratian"]], ["titel", ["diskret", "matematik"]], "&"],
    [
        ["f�rfattare", ["j", "glenn", "brookshear"]],
        ["titel", ["computer", "science", "an", "overview"]],
        ["�r", 2011],
    ],
    [
        ["f�rfattare", ["john", "zelle"]],
        [
            "titel",
            [
                "data",
                "structures",
                "and",
                "algorithms",
                "using",
                "python",
                "and",
                "c++",
            ],
        ],
        ["�r", 2009],
    ],
    [
        ["f�rfattare", ["anders", "haraldsson"]],
        ["&", ["programmering", "i", "lisp"]],
        ["�r", 1993],
    ],
]
