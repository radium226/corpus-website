from pytest import fixture
from pendulum import today
from faker import Faker
from pathlib import Path
from PIL import Image

from corpus_website.models import Document, Author, Country, Thumbnail
from corpus_website.engine import Engine


@fixture()
def thumbnail() -> Thumbnail:
    placeholder_file_path = Path(__file__).parent / "placeholder.png"
    return Thumbnail(Image.open(placeholder_file_path))


@fixture
def documents(thumbnail: Thumbnail):
    faker = Faker()
    return [
        Document(
            thumbnail=thumbnail,
            date=today(),
            author=Author(faker.name()),
            country=Country(faker.country()),
        )
        for _ in range(0, 25)
    ]


@fixture
def theme_folder_path() -> Path:
    return Path(__file__).parent / "theme"


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
    assert ( output_folder_path / "index.html" ).exists()
    assert ( output_folder_path / "static" / "afad38e481198111f9e7dc6468463f7b.png" ).exists()
    