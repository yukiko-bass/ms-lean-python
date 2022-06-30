import os


def test_os(monkeypatch):
    # 常にfalseを返す関数(lamdba)を定義
    monkeypatch.setattr("os.path.exists", lambda x: False)
    assert os.path.exists("/") is False

    monkeypatch.setattr(os.path, "exists", lambda x: False)
    assert os.path.exists("/") is False
