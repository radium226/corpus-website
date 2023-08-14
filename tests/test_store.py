from pathlib import Path
from pytest import fixture

from corpus_website.store import Store


@fixture
def excel_file_path():
    return Path(__file__).parent / "corpus.xlsx"


@fixture
def store(excel_file_path: Path) -> Store:
    return Store(excel_file_path)


def test_list_documents(store: Store) -> None:
    documents = store.list_documents()

    assert len(documents) == 2