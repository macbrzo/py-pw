from components.navigation_bar import NavigationBar
from playwright.sync_api import Page

from pages.base_page import BasePage


class BrowsePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.nav = NavigationBar(self.page)

        self.live_streams = self.page.get_by_role("button").filter(has_text="viewers")

    def click_visible_video(self, num: int) -> None:
        live_stream = self.live_streams.filter(visible=True).nth(num)
        live_stream.nth(num).click()

    def scroll_full_screen(self, amount: int = 1, scroll_timeout: int = 500) -> None:
        self.live_streams.first.wait_for(state="visible")
        super().scroll_full_screen(amount, scroll_timeout)
