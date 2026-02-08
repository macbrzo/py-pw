from playwright.sync_api import Locator, Page

from components.navigation_bar import NavigationBar
from pages.base_page import BasePage


class StreamPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.nav = NavigationBar(self.page)

        self.video_player = self.page.get_by_label("Twitch video player")

        # Added to handle content gate popup (example https://www.twitch.tv/gexsk8)
        self.page.add_locator_handler(
            self.page.get_by_text("This content may not be"),
            lambda: self.page.get_by_role("button", name="Start Watching").click(),
        )

    def get_video_player(self) -> Locator:
        self.page.wait_for_load_state(state="load")
        return self.video_player
