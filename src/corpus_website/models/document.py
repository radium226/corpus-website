from dataclasses import dataclass
from pendulum import Date

from .author import Author
from .country import Country
from .thumbnail import Thumbnail
from .job import Job
from .title import Title
from .publication import Publication
from .source import Source
from .medium import Medium
from .criticized_theme import CriticizedTheme
from .aesthetic_paradigm import AestheticParadigm
from .aesthetic_pattern import AestheticPattern
from .register import Register
from .interpretation import Interpretation

# - [x] Miniature
# - [x] Date
# - [x] Auteur
# - [x] Profession
# - [x] Pays
# - [x] Titre
# - [x] Source
# - [x] Medium
# - [x] Publication
# - [x] Thème(s) critique(s) (idées primaires)
# - [x] Paradigme esthétique (idées primaires)
# - [x] Motifs esthétiques
# - [x] Registre(s)
# - [x] Interprétation


@dataclass
class Document():

    thumbnail: Thumbnail
    date: Date
    author: Author
    job: Job
    country: Country
    title: Title
    source: Source
    medium: Medium
    publication: Publication
    criticized_themes: list[CriticizedTheme]
    aesthetic_paradigms: list[AestheticParadigm]
    aesthetic_patterns: list[AestheticPattern]
    registers: list[Register]
    interpretation: Interpretation