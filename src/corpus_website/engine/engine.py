from typing import Any
from pathlib import Path
from shutil import copy
from jinja2 import Environment
from jinja2 import FileSystemLoader

from ..models import Document


class Engine():

    def __init__(self, theme_folder_path: Path):
        self.theme_folder_path = theme_folder_path

    def render(self, output_folder_path: Path, documents: list[Document]) -> None:
        environment = Environment(
            loader=FileSystemLoader(str(self.theme_folder_path))
        )
        for input_file_path in filter(lambda p: not p.is_dir(), self.theme_folder_path.rglob("*")):
            match input_file_path.suffix:
                case ".j2":
                    output_file_path = (output_folder_path / input_file_path.relative_to(self.theme_folder_path)).with_name(input_file_path.name.removesuffix(".j2"))
                    template = environment.get_template(str(input_file_path.relative_to(self.theme_folder_path)))
                    with output_file_path.open("w") as stream: 
                        stream.write(template.render(documents=documents))

                    
                case _: 
                    output_file_path = output_folder_path / input_file_path.relative_to(self.theme_folder_path)
                    output_file_path.parent.mkdir(parents=True, exist_ok=True)
                    copy(input_file_path, output_file_path)                    

