from twttr import shorten


def test_a():
    assert shorten("$twitter!") == "$twttr!"
    assert shorten("TwIttEr") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"


def test_b():
    assert shorten("AMAZON") == "MZN"
    assert shorten("GOOGLE") == "GGL"


def test_c():
    assert shorten("smth") == "smth"
    assert shorten("mngmt") == "mngmt"


def test_d():
    assert shorten("aeiouAEIOU") == ""
