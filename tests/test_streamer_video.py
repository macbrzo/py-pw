import logging

from playwright.sync_api import expect
import pytest

from config import LONG_TIMEOUT
from pages.stream_page import StreamPage
from pages.twitchtv import TwitchTv


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
    logging.info("1. Go to TwitchTV")
    twitch_page = TwitchTv.navigate_to(page)

    logging.info("2. Search for StarCraft II")
    browse_page = twitch_page.nav.navigate_to_browse()
    browse_page.search("StarCraft II")

    logging.info("3. Scroll two screens")
    browse_page.scroll_full_screen(amount=2)

    logging.info("4. Select 1st visible Live stream")
    stream_page = browse_page.click_visible_video(0)

    logging.info("5. Verify Live stream started")
    vide_player = stream_page.get_video_player()
    expect(vide_player, "Video stream did not start").to_have_js_property(
        "paused",
        False,
        timeout=LONG_TIMEOUT,
    )


@pytest.mark.skip(reason="Test added only to verify Mature Content gate handling")
def test__success__live_stream_content_gate(page):
    """
    Verifies if content gate will be closed for content gated streamer https://www.twitch.tv/gexsk8

    || Test Scenario ||
    | 1. Go to TwitchTV - gexsk8 live stream |
    | 2. Verify Live stream started |
    """
    logging.info("1. Go to TwitchTV")
    TwitchTv.navigate_to(page, "https://www.twitch.tv/gexsk8")

    logging.info("2. Verify Live stream started")
    stream_page = StreamPage(page)
    vide_player = stream_page.get_video_player()
    expect(vide_player, "Video stream did not start").to_have_js_property(
        "paused",
        False,
        timeout=LONG_TIMEOUT,
    )
