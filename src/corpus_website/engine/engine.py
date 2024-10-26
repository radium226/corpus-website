from typing import Any
from pathlib import Path
from shutil import copy
from jinja2 import Environment, FileSystemLoader
from PIL import Image
import base64
from hashlib import md5
from io import BytesIO

from ..models import Document


class Engine():

    def __init__(self, theme_folder_path: Path):
        self.theme_folder_path = theme_folder_path

    def render(self, output_folder_path: Path, documents: list[Document]) -> None:
        environment = Environment(
            loader=FileSystemLoader(str(self.theme_folder_path))
        )

        def static_image_filter(image: Image, format: str):
            buffer = BytesIO()
            image.save(buffer, format=format)
            hash = md5(buffer.getvalue()).hexdigest()
            file_path = output_folder_path / "static" / f"{hash}.{format}"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with file_path.open("wb") as stream:
                stream.write(buffer.getvalue())
            return file_path.relative_to(output_folder_path)
            

        environment.filters["static_image"] = static_image_filter

        available_themes = list(set([theme for document in documents for theme in document.themes]))
        
        for input_file_path in filter(lambda p: not p.is_dir(), self.theme_folder_path.rglob("*")):
            output_file_path = output_folder_path / input_file_path.relative_to(self.theme_folder_path)
            output_file_path.parent.mkdir(parents=True, exist_ok=True)
                    
            match input_file_path.suffix:
                case ".j2":
                    output_file_path = output_file_path.with_name(input_file_path.name.removesuffix(".j2"))
                    template = environment.get_template(str(input_file_path.relative_to(self.theme_folder_path)))
                    with output_file_path.open("w") as stream: 
                        stream.write(template.render(
                            documents=documents,
                            available_themes=available_themes,
                        ))
                    
                case _: 
                    copy(input_file_path, output_file_path)                    

