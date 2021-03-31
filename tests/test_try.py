import pytest
@pytest.mark.hw_lpc_specific
def test_hw_lpc():
    pass


@pytest.mark.hw
def test_hw():
    pass

def test_empty():
    assert True
