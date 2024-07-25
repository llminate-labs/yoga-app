import pytest
from bs4 import BeautifulSoup


@pytest.mark.parametrize(
    'expected_src', [
        ('https://oaidalleapiprodscus.blob.core.windows.net/private/org-xoveDohUTeWTwd7uYScv2uyz/user-7E63qmNDGeNd8DOac52nI0qL/img-di2G3LR9DZVhTZONixgqHMRW.png')
    ]
)
def test_yoga_pose_image_source(browser, expected_src):
    browser.get('file:///path/to/index.html')
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    image_src = soup.find('img')['src']
    assert image_src == expected_src


def test_unit_test_results_displayed_correctly(browser):
    browser.get('file:///path/to/index.html')
    unit_test_results = browser.find_element_by_id('unit-test-results').text
    assert 'Unit tests passed!' in unit_test_results or 'Unit tests failed!' in unit_test_results
