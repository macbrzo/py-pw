from typing import TYPE_CHECKING

from playwright.sync_api import Page

if TYPE_CHECKING:
    from pages.browse_page import BrowsePage
    from pages.stream_page import StreamPage

from components.navigation_bar import NavigationBar
from pages.base_page import BasePage


class BrowsePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.nav = NavigationBar(self.page)
        self.search_input = self.page.get_by_role("searchbox", name="Search")

        self._category_href = self.page.locator('a[href^="/directory/category"]')
        self.first_category_suggestion = self.page.get_by_role("listitem").filter(
            has=self._category_href
        )
        self.live_streams = self.page.get_by_role("button").filter(has_text="viewers")

    def search(self, text: str) -> "BrowsePage":
        from pages.browse_page import BrowsePage

        self.search_input.fill(text)
        self.first_category_suggestion.click()
        return BrowsePage(self.page)

    def click_visible_video(self, num: int) -> "StreamPage":
        from pages.stream_page import StreamPage

        live_stream = self.live_streams.filter(visible=True).nth(num)
        live_stream.click()
        return StreamPage(self.page)

    def scroll_full_screen(self, amount: int = 1, scroll_timeout: int = 500) -> None:
        self.live_streams.first.wait_for(state="visible")
        super().scroll_full_screen(amount, scroll_timeout)
