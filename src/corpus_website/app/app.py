from click import command, option, argument, group
from pathlib import Path

from ..engine import Engine
from ..store import Store


@group()
def app():
    pass

@app.command()
@argument("CORPUS_FILE_PATH", type=Path)
@argument("TEMPLATE_FOLDER_PATH", type=Path)
@argument("RENDERED_FOLDER_PATH", type=Path)
def generate(
    corpus_file_path: Path, 
    template_folder_path: Path, 
    rendered_folder_path: Path,
):
    store = Store(corpus_file_path)
    engine = Engine(template_folder_path)

    documents = store.list_documents()
    
    engine.render_templates(
        rendered_folder_path, 
        variables={
            "corpus": documents,
        },
    )

