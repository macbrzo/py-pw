from pages.browse_page import BrowsePage
from pages.stream_page import StreamPage
from pages.twitchtv import TwitchTv
from playwright.sync_api import expect
import pytest


def test__success__start_sc2_live_stream(page):
    twitch_page = TwitchTv(page)
    twitch_page.go_to_page()

    twitch_page.nav.go_to_browse().search_for("StarCraft II")
    # twitch_page.nav.go_to_browse().search_for("Fortinite")

    browse_page = BrowsePage(page)
    browse_page.scroll_full_screen(2)
    browse_page.go_to_visible_video(0)

    stream_page = StreamPage(page)
    vide_player = stream_page.get_video_player()
    expect(vide_player).to_have_js_property("paused", False, timeout=10_000)


@pytest.mark.skip
def test__success__live_stream_content_gate(page):
    twitch_page = TwitchTv(page)
    twitch_page.go_to_page("https://www.twitch.tv/gexsk8")
    stream_page = StreamPage(page)
    vide_player = stream_page.get_video_player()
    expect(vide_player).to_have_js_property("paused", False, timeout=10_000)
