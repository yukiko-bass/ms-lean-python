import os
import tempfile
import pytest


"""
戻り値は、それを使用するすべてのテストに対して計算されます。
関数にクリーンアップが必要な場合は、それを使用するすべてのテストの後に行われます。
"""


@pytest.fixture
def tmp_file(request):
    temp = tempfile.NamedTemporaryFile(delete=False)

    def create():
        return temp.name

    def cleanup():
        os.remove(temp.name)

    request.addfinalizer(cleanup)
    return create


# テストでは、"フィクスチャの名前" を引数として指定することでフィクスチャを要求できます。
def test_file(tmp_file):
    path = tmp_file()
    assert os.path.exists(path)


"""
function: テストごとに 1 回実行されます
class: クラスごとに 1 回実行されます
module: モジュールに対して 1 回実行されます
session: テスト セッションに対して 1 回実行されます
"""


@pytest.fixture(scope="module")
def tmp_file_with_contents(request):
    temp = tempfile.NamedTemporaryFile(delete=False)

    def create(contents):
        return temp.name

    def cleanup():
        os.remove(temp.name)

    request.addfinalizer(cleanup)
    return create
