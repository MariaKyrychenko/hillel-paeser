from urllib import parse

def parse(url):

    parse.urlsplit(url)
    parse.parse_qs(parse.urlsplit(url).query)
    a = dict(parse.parse_qsl(parse.urlsplit(url).query))
    return {a}
#f __name__ == '__main__':
    #Testing function `parse`
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/') == {}
    assert parse('https://example.com/?') == {}
    assert parse('https://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'feirret', 'color': 'purple'}