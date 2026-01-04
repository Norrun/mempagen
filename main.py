vowels = ["a", "e", "i", "o", "u"]
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z",
]

end = "*"

consonants_combo = {
    "b": {
        "l":{end:True},
        "r":{end:True}
        },
    "c":{
        "l":{end:True},
        "r":{end:True},
        "t":{end:True}
    },
    "f":{
        "l":{end:True},
        "r":{end:True}
    },
    "g":{
        "l":{end:True},
        "r":{end:True}
    },
    "n":{
        "t":{end:True}
    },
    "p":{
        "l":{end:True},
        "r":{end:True}
    },
    "s":{
        "c":{
            "r":{end:True}
        },
        "k":{end:True},
        "n":{end:True},
        "p":{
            end:True,
            "r":{end:True},
            "l":{end:True}
            },
        "t":{
            end:True,
            "r":{end:True}
             },
        
    },
    "t":{
        "r":{end:True},
        "h":{
            "r":{end:True}
        }
    }


}