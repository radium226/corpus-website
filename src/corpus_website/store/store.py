from pathlib import Path
from openpyxl import load_workbook
import pendulum as p
import dateparser as dp
from PIL import Image

from ..models import Document, Thumbnail, Author, Country


def parse_date(text: str) -> p.Date:
    # return p.instance(dp.parse(text))
    return p.parse(text, format="%Y")


class Store():

    def __init__(self, excel_file_path: Path):
        self.excel_file_path = excel_file_path
    
    def list_documents(self) -> list[Document]:
        workbook = load_workbook(filename=str(self.excel_file_path), rich_text=True)
        worksheet = workbook.active
        return [
            Document(
                thumbnail=Thumbnail(Image.open(Path(__file__).parent / "placeholder.png")),
                date=parse_date(str(row[1])),
                author=Author(row[2]),
                country=Country(row[3]),
            )
            for row in worksheet.iter_rows(min_row=2, values_only=True)
        ]
            