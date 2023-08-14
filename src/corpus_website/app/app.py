from click import command, option, argument, group
from pathlib import Path

from ..engine import Engine
from ..store import Store
from ..server import Server


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


@app.command()
@argument("EXCEL_FILE_PATH", type=Path)
@argument("THEME_FOLDER_PATH", type=Path)
def serve(

    excel_file_path: Path, 
    theme_folder_path: Path, 
) -> None:

    store = Store(excel_file_path)
    engine = Engine(theme_folder_path)

    output_folder_path = Path("/tmp/corpus-website/output")
    output_folder_path.mkdir(parents=True, exist_ok=True)

    server = Server(
        output_folder_path=output_folder_path, 
        port=8888,
    )

    def callback():
        documents = store.list_documents()
        engine.render(output_folder_path, documents=documents)

    server.serve(callback)