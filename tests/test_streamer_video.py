import logging

from pages.browse_page import BrowsePage
from pages.stream_page import StreamPage
from pages.twitchtv import TwitchTv
from playwright.sync_api import expect
import pytest


def test__success__start_sc2_live_stream(page):
    """
    Verifies if stream starts for 1st visible streamer on Live streams list after scrolling two screens

    || Test Scenario ||
    | 1. Go to TwitchTV |
    | 2. Search for StarCraft II |
    | 3. Scroll two screens |
    | 4. Select 1st visible Live stream |
    | 5. Verify Live stream started |
    """
    twitch_page = TwitchTv(page)

    logging.info("1. Go to TwitchTV")
    twitch_page.go_to_page()

    logging.info("2. Search for StarCraft II")
    twitch_page.nav.go_to_browse().search_for("StarCraft II")

    logging.info("3. Scroll two screens")
    browse_page = BrowsePage(page)
    browse_page.scroll_full_screen(amount=2)

    logging.info("4. Select 1st visible Live stream")
    browse_page.click_visible_video(0)

    logging.info("5. Verify Live stream started")
    stream_page = StreamPage(page)
    vide_player = stream_page.get_video_player()
    expect(vide_player, "Video stream did not start").to_have_js_property(
        "paused",
        False,
        timeout=10_000,
    )


@pytest.mark.skip
def test__success__live_stream_content_gate(page):
    """
    Verifies if content gate will be closed for content gated streamer https://www.twitch.tv/gexsk8

    || Test Scenario ||
    | 1. Go to TwitchTV - gexsk8 live stream |
    | 2. Verify Live stream started |
    """
    logging.info("1. Go to TwitchTV - gexsk8 live stream")
    twitch_page = TwitchTv(page)
    twitch_page.go_to_page("https://www.twitch.tv/gexsk8")

    logging.info("2. Verify Live stream started")
    stream_page = StreamPage(page)
    vide_player = stream_page.get_video_player()
    expect(vide_player, "Video stream did not start").to_have_js_property(
        "paused",
        False,
        timeout=10_000,
    )
