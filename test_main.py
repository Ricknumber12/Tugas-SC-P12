from main import kurang, tambah


def test_tambah():
    assert tambah(1, 2) == 3


def test_kurang():
    assert kurang(5, 3) == 2