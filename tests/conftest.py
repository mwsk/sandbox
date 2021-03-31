import pytest
def pytest_addoption(parser):
    parser.addoption(
        "--device",
        action="store",
        default=None,
        help="device"
    )


@pytest.fixture()
def use_device(request):
    device = request.config.getoption('--device')
    # raise pytest.skip('no hw')
    if not device: 
        raise pytest.skip('no hw')

@pytest.fixture()
def pfr(request):
    device = request.config.getoption('--device')
    if device not in ['lpc', 'n4a']:
        raise pytest.skip("not lpc, not n4a")

@pytest.fixture()
def fuses(request):
    device = request.config.getoption('--device')
    if device not in ['rt', 'n4a']:
        raise pytest.skip("not rt")
