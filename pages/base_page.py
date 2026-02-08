from pathlib import Path
from uuid import uuid4

from playwright.sync_api import Page

from config import SCREENSHOTS_PATH


class BasePage:
    def __init__(self, page: Page, timeout: int = 3000) -> None:
        self.page = page
        self.timeout = timeout

    def go_to_page(self, url: str) -> None:
        self.page.goto(url)
        self.page.wait_for_load_state("load")

    def take_screenshot(self, name: str | None = None) -> None:
        if not name:
            name = uuid4()
        self.page.screenshot(path=Path(SCREENSHOTS_PATH).join(f"{name}.png"), full_page=True)

    def scroll_full_screen(self, amount: int = 1, scroll_timeout: int = 500) -> None:
        viewport_height = self.page.viewport_size["height"]
        for _ in range(amount):
            self.page.mouse.wheel(0, viewport_height)
            self.page.wait_for_timeout(scroll_timeout)
