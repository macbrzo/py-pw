from typing import TYPE_CHECKING

from playwright.sync_api import Page

if TYPE_CHECKING:
    from pages.browse_page import BrowsePage


class NavigationBar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.browse_link = self.page.get_by_role("link", name="Browse")

    def navigate_to_browse(self) -> "BrowsePage":
        from pages.browse_page import BrowsePage

        self.page.wait_for_load_state("load")
        self.browse_link.click()
        return BrowsePage(self.page)
