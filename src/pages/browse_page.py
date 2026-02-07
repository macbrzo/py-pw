from playwright.sync_api import Page
from src.components.navigation_bar import NavigationBar
from src.pages.base_page import BasePage


class BrowsePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.nav = NavigationBar(self.page)

        # "//div[contains(@class, 'Layout')]/a[starts-with(@href, '/videos/')]"
        self.visible_videos = (
            self.page.get_by_role("link")
            .filter(has_text=None)
            .and_(self.page.locator('a[href^="/videos/"]'))
        )

    def go_to_visible_video(self, num: int) -> None:
        self.visible_videos.nth(num).click()

    def scroll_full_screen(self, amount: int = 1, scroll_timeout: int = 500) -> None:
        self.visible_videos.first.wait_for(state="visible")
        super().scroll_full_screen(amount, scroll_timeout)
