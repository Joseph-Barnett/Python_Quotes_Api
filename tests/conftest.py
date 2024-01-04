import pytest
from application import app, db
from application.quotes.models import Quote

@pytest.fixture(scope='module')
def new_quote():
    quote = Quote(text='A bucket of water could fill an ocean, depending on the size of the bucket', author='Sir Joseph Barnett')
    return quote
