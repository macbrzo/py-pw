from typing import Self

from playwright.sync_api import Page


class NavigationBar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.browse_link = page.get_by_role("link", name="Browse")
        self.search_input = page.get_by_role("searchbox", name="Search")
        self.first_suggestion = page.get_by_role("listitem").first

    def go_to_browse(self) -> Self:
        self.browse_link.click()
        return self

    def search_for(self, text: str) -> None:
        self.search_input.click()
        self.search_input.fill(text)
        self.first_suggestion.click()
