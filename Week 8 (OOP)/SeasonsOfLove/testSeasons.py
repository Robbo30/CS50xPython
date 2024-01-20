from seasons import delta
from seasons import words
from datetime import date

def testMins():
    birthDate = date.fromisoformat('2006-12-14')
    timeDelta = date.today() - birthDate
    assert delta(birthDate) == timeDelta.days * 24 * 60

def valid():
    assert words(8994240) == "Eight million, nine hundred and ninety-four thousand, two hundred and forty minutes"