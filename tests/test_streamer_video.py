from uuid import uuid4

from playwright.sync_api import Browser, Playwright, expect


def test__success__stream_started(playwright: Playwright, browser: Browser):
    # TODO: move UI pieces to correct pages
    iphone_13 = playwright.devices["iPhone 13"]
    with browser.new_context(record_video_dir="videos/", **iphone_13) as context:
        page = context.new_page()

        page.goto("https://m.twitch.tv/")
        # Cookies
        page.locator("div").filter(has_text="Cookies and Advertising").nth(3).click()
        page.get_by_role("button", name="Accept").click()

        # Navigation bar actions
        page.get_by_role("link", name="Browse").click()
        page.get_by_role("searchbox", name="Search").click()
        page.get_by_role("searchbox", name="Search").fill("StarCraft II")
        page.get_by_role("listitem").first.click()

        # Scroll x2 - maybe js better?
        viewport_height = page.viewport_size["height"]
        for _ in range(2):
            page.mouse.wheel(0, viewport_height)
            page.wait_for_timeout(500)

        # Collect videos
        # "//div[contains(@class, 'Layout')]/a[starts-with(@href, '/videos/')]" - not best practice in PW
        visible_videos = (
            page.get_by_role("link").filter(has_text=None).and_(page.locator('a[href^="/videos/"]'))
        )
        visible_videos.nth(1).click()

        # # Maybe
        # for i in range(visible_videos.count()):
        #     if visible_videos.nth(i).is_visible():
        #         visible_videos.nth(i).click()
        #         break

        video_player = page.get_by_label("Twitch video player")
        try:
            expect(video_player).to_have_js_property("paused", False)
        except AssertionError:
            page.go_back()

        # if this crap then go back?
        # subscribers_only_msg = page.get_by_text("This video is only available")
        # if subscribers_only_msg.is_visible(timeout=1000):
        #     page.go_back()
        visible_videos = (
            page.get_by_role("link").filter(has_text=None).and_(page.locator('a[href^="/videos/"]'))
        )
        visible_videos.nth(2).click()

        # catch popup

        video_player = page.get_by_label("Twitch video player")
        expect(video_player).to_have_js_property("paused", False)
        page.screenshot(path=f"{uuid4()}.png", full_page=True)
