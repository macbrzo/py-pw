from pathlib import Path

from config import SCREENSHOTS_PATH, VIDEOS_PATH
import pytest

MOBILE_DEVICES = [
    "iPhone X",
    "iPhone 14 Pro Max",
    "Pixel 7",
    "Pixel 2",
    "Galaxy S5",
    "iPad (gen 7)",
    "iPad Pro 11",
    "Galaxy S20 Ultra",
]


def pytest_configure(config):
    Path(SCREENSHOTS_PATH).mkdir(parents=True, exist_ok=True)
    Path(VIDEOS_PATH).mkdir(parents=True, exist_ok=True)


def pytest_addoption(parser):
    parser.addoption(
        "--all-mobile-devices",
        action="store_true",
        default=False,
        help="To run against all Mobile devices",
    )


def pytest_generate_tests(metafunc):
    if "mobile_device" in metafunc.fixturenames:
        mobile_devices = (
            MOBILE_DEVICES
            if metafunc.config.getoption("--all-mobile-devices")
            else [MOBILE_DEVICES[0]]
        )
        metafunc.parametrize("mobile_device", mobile_devices)


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args, playwright, mobile_device, request):
    context = {
        **browser_context_args,
        **playwright.devices[mobile_device],
    }

    if request.config.getoption("--video").lower() == "on":
        test_dir = request.node.name.split("[")[0]
        record_video_dir = Path(VIDEOS_PATH) / test_dir / mobile_device.replace(" ", "_")
        record_video_dir.mkdir(parents=True, exist_ok=True)
        context["record_video_dir"] = record_video_dir

    return context
