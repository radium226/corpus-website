from pytest import fixture
from pendulum import today
from faker import Faker
from pathlib import Path

from corpus_website.models import Document, Author, Country
from corpus_website.engine import Engine


@fixture
def documents():
    faker = Faker()
    yield [
        Document(
            date=today(),
            author=Author(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
            ),
            country=Country(faker.country()),
        )
        for _ in range(0, 25)
    ]


@fixture
def theme_folder_path() -> Path:
    return Path(__name__).parent / "theme"


@fixture
def engine(theme_folder_path: Path) -> Engine:
    return Engine(theme_folder_path)


@fixture
def output_folder_path() -> Path:
    yield Path("/tmp/corpus-website/output")


def test_render(engine, output_folder_path, documents):
    engine.render(
        output_folder_path, 
        documents=documents,
    )

    assert ( output_folder_path / "nested" / "test.txt" ).exists()
    