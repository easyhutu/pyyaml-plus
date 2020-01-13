from yamlplus import load, dump


def test_load():
    a = r'a.yml'
    b = r'b.yml'
    with open(a) as f:
        la = load(f.read())

    ea = {'usr3': {'usr3_ee': 'b', 'usr3_dd': 456}, 'usr1': {'usr3_ee': 'b', 'usr3_dd': 456},
          'usr2': {'name': 'b', 'psw': 456, 'aslw': {'usr3_ee': 'b', 'usr3_dd': 456}}}

    assert ea == la

    with open(b) as f:
        lb = load(f.read())
    eb = {'usr3': {'usr3_ee': 'b', 'usr3_dd': 456}, 'usr1': {'usr3_ee': 'b', 'usr3_dd': 456}}

    assert eb == lb


if __name__ == '__main__':
    test_load()