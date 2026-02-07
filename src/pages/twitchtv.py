from config import BASE_URL
from playwright.sync_api import Page, TimeoutError
from src.components.navigation_bar import NavigationBar
from src.pages.base_page import BasePage


class TwitchTv(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.nav = NavigationBar(self.page)

        self.cookies_and_ads_modal = (
            self.page.locator("div").filter(has_text="Cookies and Advertising").nth(3)
        )
        self.accept_btn = self.page.get_by_role("button", name="Accept")

    def accept_cookies_and_ads(self) -> None:
        # TODO: rethink
        try:
            self.cookies_and_ads_modal.wait_for(state="visible", timeout=self.timeout)
            self.accept_btn.click()
        except TimeoutError:
            pass

    def go_to_page(self, url=BASE_URL) -> None:
        super().go_to_page(url)
        self.accept_cookies_and_ads()
