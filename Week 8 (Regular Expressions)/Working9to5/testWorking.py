from working import convert
import pytest

def valid():
    assert convert("2 PM to 12 AM") == ("14:00 to 00:00")

def invalid():
    with pytest.raises(ValueError):
        convert("6:60 AM to 14:00 PM")