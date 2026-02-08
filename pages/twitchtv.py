from components.navigation_bar import NavigationBar
from config import BASE_URL
from playwright.sync_api import Page, TimeoutError

from pages.base_page import BasePage


class TwitchTv(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.nav = NavigationBar(self.page)

        self.cookies_and_ads_modal = (
            self.page.locator("div").filter(has_text="Cookies and Advertising").nth(3)
        )
        self.accept_btn = self.page.get_by_role("button", name="Accept")

        # Added to handle Activation dialog that appears only in parallel run
        self._activate_gate = self.page.get_by_role("button", name="Activate to close dialog")
        self._activate_gate_keep_using_web_btn = self.page.get_by_role(
            "button", name="Keep using web"
        )
        self.page.add_locator_handler(
            self._activate_gate,
            lambda: [
                # self._activate_gate_keep_using_web_btn.click(force=True),
                self._activate_gate_keep_using_web_btn.dispatch_event("click"),
                self._activate_gate.wait_for(state="hidden"),
            ],
        )

    def accept_cookies_and_ads(self) -> None:
        # TODO: rethink
        try:
            self.cookies_and_ads_modal.wait_for(state="visible", timeout=self.timeout)
            self.accept_btn.click(force=True)
            self.accept_btn.wait_for(state="hidden")
        except TimeoutError:
            pass

    def go_to_page(self, url=BASE_URL) -> None:
        super().go_to_page(url)
        self.accept_cookies_and_ads()
