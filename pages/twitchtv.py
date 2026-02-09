from playwright.sync_api import Page

from components.navigation_bar import NavigationBar
from config import BASE_URL
from pages.base_page import BasePage


class TwitchTv(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.nav = NavigationBar(self.page)
        # Cookies and Ads modal
        self.cookies_and_ads_modal = (
            self.page.locator("div")
            .filter(has_text="Cookies and Advertising")
            .nth(3)  # TODO: find better locator
        )
        self.accept_btn = self.page.get_by_role("button", name="Accept")
        # Activation dialog
        self.activate_gate = self.page.get_by_role("button", name="Activate to close dialog")
        self.activate_gate_keep_using_web_btn = self.page.get_by_role(
            "button", name="Keep using web"
        )

        # Added to handle Activation dialog that appears only in parallel run
        self.page.add_locator_handler(
            self.activate_gate,
            lambda: self._hanlde_activation_dialog(),
        )
        # Added to handle Cookies and Ads modal
        self.page.add_locator_handler(
            self.cookies_and_ads_modal,
            lambda: self._handle_cookies_and_ads(),
        )

    @classmethod
    def navigate_to(cls, page: Page, url=BASE_URL) -> "TwitchTv":
        twitch_page = cls(page)
        twitch_page.go_to(url)
        return twitch_page

    def _handle_cookies_and_ads(self) -> None:
        self.accept_btn.click(force=True)
        self.accept_btn.wait_for(state="hidden")

    def _hanlde_activation_dialog(self) -> None:
        self.activate_gate_keep_using_web_btn.dispatch_event("click")
        self.activate_gate.wait_for(state="hidden")
