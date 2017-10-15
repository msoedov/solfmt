from solfmt import fmt


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


def test_ident_v2():
    sample = """
    contract T
{
}
    """

    expected = """
contract T {

}
"""
    assert fmt(sample) == expected


def test_blank_spaces_eq():
    sample = """
Amount =msg.value;
Amount ==msg.value;
Amount= msg.value;
Amount => msg.value;
Amount > msg.value;
Amount +=msg.value;
Amount+=msg.value;
Amount-=msg.value;
    """

    expected = """
Amount = msg.value;
Amount == msg.value;
Amount = msg.value;
Amount => msg.value;
Amount > msg.value;
Amount += msg.value;
Amount += msg.value;
Amount -= msg.value;
"""
    assert fmt(sample) == expected


def test_add_semicol():
    sample = """
Amount = msg.value
Call(1)
function A(bool b, string reason) {
    if (!b) {
        C = reason
        require(b)
    }
}
    """

    expected = """
Amount = msg.value;
Call(1);
function A(bool b, string reason) {
    if (!b) {
        C = reason;
        require(b);
    }
}
"""
    assert fmt(sample) == expected
