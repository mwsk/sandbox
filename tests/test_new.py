import pytest

def test_empty():
    assert True

@pytest.mark.usefixtures('use_device', 'pfr')
def test_pfr():
    assert True

@pytest.mark.usefixtures('use_device')
@pytest.mark.usefixtures('fuses')
def test_fuses():
    assert True
