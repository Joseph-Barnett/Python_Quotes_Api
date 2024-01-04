import app
from application.quotes.models import Quote

def test_new_post_with_fixture(new_quote):
    assert new_quote.text == 'A bucket of water could fill an ocean, depending on the size of the bucket'
    assert new_quote.author == 'Sir Joseph Barnett'

    assert new_quote.json == {
        "id": new_quote.id,
        "text": new_quote.text,
        "author": new_quote.author,
    }
