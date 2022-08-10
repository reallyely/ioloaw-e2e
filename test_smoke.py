import re
from playwright.sync_api import Page, expect


def test_can_access_kinship_connector(page: Page):
    page.goto("https://iolaw.net/run/KIN/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Kinship Connector"))
