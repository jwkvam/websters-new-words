import dictparse

def test_split():
    line = 'ABERRANCE; ABERRANCY'
    hds = dictparse.headers(line)
    assert hds[0] == 'ABERRANCE'
    assert hds[1] == 'ABERRANCY'

def test_headers():
    assert dictparse.isheader('A')

def test_multiheaders():
    line = 'ABERRANCE; ABERRANCY'
    assert dictparse.isheader(line)

def test_defn1():
    line = '1. hello there'
    assert dictparse.isdefn(line)
    line = 'Defn: hello there'
    assert dictparse.isdefn(line)
    line = '3. hello there'
    assert dictparse.isdefn(line)
    line = 'Defn: An instrument for ascertaining the degree of fermentation'
    assert dictparse.isdefn(line)
