try:
    import pytest
    from files import genome
    
except Exception as e:
    print(e)


def test_load_data():
    assert genome.load_data