from main import tambah

from main import tambah, kurang


def test_tambah():
    assert tambah(1, 2) == 3


def test_kurang():
    assert kurang(5, 3) == 2
