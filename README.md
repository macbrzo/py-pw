## Python Playwright empowered by pytest

### Project structure

```bash
.
├── artifacts/               # Test execution output
│   ├── screenshots/         # Grouped by test case and device/emulation
│   └── videos/              # Recordings of test execution
├── components/              # Reusable UI elements (Page Components)
│   └── navigation_bar.py    # Global nav logic
├── pages/                   # Page Object Model (POM)
│   ├── base_page.py         # Shared logic/utilities for all pages
│   ├── browse_page.py       # "Browse" category view logic
│   ├── stream_page.py       # Live stream player logic
│   └── twitchtv.py          # Main landing page entry point
├── tests/                   # Test suites
│   └── test_streamer_video.py
├── config.py                # Project-wide constants and variables
├── conftest.py              # Pytest fixtures and Playwright hooks
├── pyproject.toml           # Dependencies and Ruff/Pytest configuration
├── pre-commit-config.yaml   # Git hooks for code quality
└── README.md                # Project documentation
```

### Handling content gate popups
The framework uses Playwright's `add_locator_handler` to automatically deal with non-deterministic overlays that interrupt test flow.
- Mature Content Gate (**StreamPage**): Automatically detects the `This content may not be...` warning and triggers the `Start Watching` button to resume the stream.
- Activation Modal (**TwitchTV**): Specifically handles the `Keep using web` dialog that frequently appears during multi-threaded runs.
By registering these handlers, the main test logic remains clean and focused on the actual scenario, while Playwright manages the popups in the background as they appear.



### Installation
1. Clone the repository

```Bash
git clone <your-repo-url>
```
cd py-pw

2. Install everything (including Dev tools)
The uv sync command will automatically create a virtual environment and install all dependencies listed in pyproject.toml.

```Bash
uv sync
```

3. Install Playwright Browsers
You need to install the browser binaries to run the tests:

```Bash
uv run playwright install chromium
```

### Running Tests
All commands are prefixed with uv run to ensure they use the project's environment.

#### Run with on device emulation with browser visible:

```Bash
uv run pytest --browser chromium --headed
```

#### Run in parallel (4 workers) on all mobile (predefined) devices:

```Bash
uv run pytest --browser chromium --headed --all-mobile-devices -n 4 --video on
```
