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
