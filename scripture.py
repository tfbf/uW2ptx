class scripture:

    __invalid_book_msg = "Invalid Book Name!"

    __books = {
        "GEN": [1, "genesis", "gen", "gn", "1"],
        "EXO": [2, "exodus",  "exo", "ex", "2"],
        "LEV": [2, "leviticus",  "lev", "le", "3"],
        "NUM": [2, "number",  "num", "nu", "4"],
        "DEU": [2, "deuteronomy",  "deu", "de", "5"],
        "JOS": [2, "joshua",  "jos", "js", "6"],
        "JDG": [2, "judges",  "jud", "jd", "7"],
        "RUT": [2, "ruth",  "rut", "ru", "8"],
        "1SA": [2, "1 samuel",  "1sa", "1s", "9"],
        "2SA": [2, "2 samuel",  "2sa", "2s", "10"],
        "1KI": [2, "1 kings",  "1ki", "1k", "11"],
        "2KI": [2, "2 kings",  "2ki", "2k", "12"],
        "1CH": [2, "1 chronicles",  "1ch", "1c", "13"],
        "2CH": [2, "2 chronicles",  "2ch", "2c", "14"],
        "EZR": [2, "ezra",  "ezr", "ez", "15"],
        "NEH": [2, "nehemiah",  "neh", "ne", "16"],
        "EST": [2, "esther",  "est", "es", "17"],
        "JOB": [2, "job",  "job", "jb", "18"],
        "PSA": [2, "psalms",  "psa", "ps", "19"],
        "PRO": [2, "psalms",  "psa", "ps", "20"],
        "ECC": [2, "ecclesiastes",  "ecc", "ec", "21"],
        "SNG": [2, "song of songs",  "sng", "sn", "22"],
        "ISA": [2, "isaiah",  "isa", "is", "23"],
        "JER": [2, "jeremiah",  "jer", "je", "24"],
        "LAM": [2, "lamentations",  "lam", "la", "25"],
        "EZK": [2, "ezekiel",  "ezk", "ek", "26"],
        "DAN": [2, "daniel",  "dan", "da", "27"],
        "HOS": [2, "hosea",  "hos", "ho", "28"],
        "JOL": [2, "joel",  "joe", "jl", "29"],
        "AMO": [2, "amos",  "amo", "am", "30"],
        "OBA": [2, "obadiah",  "oba", "ob", "31"],
        "JON": [2, "jonah",  "jon", "ja", "32"],
        "MIC": [2, "micah",  "mic", "mi", "33"],
        "NAM": [2, "nahum",  "nah", "na", "34"],
        "HAB": [2, "habakkuk",  "hab", "ha", "35"],
        "ZEP": [2, "zephaniah",  "zep", "ze", "36"],
        "HAG": [2, "haggai",  "hag", "hg", "37"],
        "ZEC": [2, "zechariah",  "zec", "ze", "38"],
        "MAL": [2, "malachi",  "mal", "ml", "39"],
        "MAT": [2, "matthew",  "mat", "mt", "40"],
        "MRK": [2, "mark",  "mrk", "mk", "41"],
        "LUK": [2, "luke",  "luk", "lu", "42"],
        "JHN": [2, "john",  "jhn", "jn", "43"],
        "ACT": [2, "acts",  "act", "ac", "44"],
        "ROM": [2, "romans",  "rom", "rm", "45"],
        "1CO": [2, "1corinthians",  "1co", "1c", "46"],
        "2CO": [2, "2corinthians",  "2co", "2c", "47"],
        "GAL": [2, "galatians",  "gal", "ga", "48"],
        "EPH": [2, "ephesians",  "eph", "ep", "49"],
        "PHP": [2, "philippians",  "php", "ph", "50"],
        "COL": [2, "colossians",  "col", "co", "51"],
        "1TH": [2, "1thessalonians",  "1th", "1t", "52"],
        "2TH": [2, "2thessalonians",  "2th", "2t", "53"],
        "1TI": [2, "1timothy",  "1ti", "1t", "54"],
        "2TI": [2, "2timothy",  "2ti", "1t", "55"],
        "TIT": [2, "titus",  "tit", "ti", "56"],
        "PHM": [2, "philemon",  "phm", "pm", "57"],
        "HEB": [2, "hebrews",  "heb", "he", "58"],
        "JAS": [2, "james",  "jas", "jm", "59"],
        "1PE": [2, "1peter",  "1pe", "1p", "60"],
        "2PE": [2, "2peter",  "2pe", "2p", "61"],
        "1JN": [2, "1john",  "1jn", "1j", "62"],
        "2JN": [2, "2john",  "2jn", "2j", "63"],
        "3JN": [2, "3john",  "3jn", "3j", "64"],
        "JUD": [2, "jude",  "jud", "ju", "65"],
        "REV": [2, "revelation",  "rev", "re", "66"],
    }

    @staticmethod
    def get_book(bk):
        return scripture.__books.get(bk.upper(), scripture.__invalid_book_msg)

    @staticmethod
    def get_book_seq(bk, paratext=False):
        book = scripture.get_book(bk)

        book_seq = 0
        if book == scripture.__invalid_book_msg:
            return scripture.__invalid_book_msg
        else:
            book_seq = int(book[-1])

        if paratext:
            return book_seq if book_seq < 40 else (book_seq + 1)
        else:
            return book_seq
