from src.biz_fuzz import controller

def test_store_data():
    results = controller.store_data("test.txt", "testing")
    assert results

