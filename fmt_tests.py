from app import fmt



def test_ident():
    sample = """
    contract T {
    modifier A { if (msg.sender == A) _; }
}
    """

    expected = """
contract T {
    modifier A { if (msg.sender == A) _; }
}
"""
    assert fmt(sample) == expected


def test_blank_spaces_eq():
    sample = """
Amount =msg.value;
Amount= msg.value;
Amount => msg.value;
Amount > msg.value;
Amount +=msg.value;
Amount+=msg.value;
Amount-=msg.value;
    """

    expected = """
Amount = msg.value;
Amount = msg.value;
Amount => msg.value;
Amount > msg.value;
Amount += msg.value;
Amount += msg.value;
Amount -= msg.value;
"""
    assert fmt(sample) == expected
