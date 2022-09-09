"""
These tests cover DuckDuckGo searches.
"""

from playwright.sync_api import Page, expect
def test_basic_duckduckgo_search(page: Page) -> None:
    # Given the DuckDuckGo home page is displayed
    page.goto('https://www.duckduckgo.com') #, wait_until='networkidle')
    # When the user searches for a phrase
    page.locator('#search_form_input_homepage').fill('panda')

    # page.locator('id=search_form_input_homepage').fill('panda')
    page.locator('#search_button_homepage').click()
    # Then the search result query is the phrase

    # id=search_form_input
    expect( page.locator('#search_form_input')).to_have_value('panda')
    page.locator('a[data-testid="result-title-a"]').nth(4).wait_for()
    titles = page.locator('a[data-testid="result-title-a"]').all_text_contents()
    matches = [t for t in titles if 'panda' in t.lower()]
    print('result length ================', len(matches))
    assert len(matches)>0
    expect(page).to_have_title('panda at DuckDuckGo')


    # And the search result links pertain to the phrase
    # And the search result title contains the phrase

