from dataclasses import dataclass
from pendulum import Date

from .author import Author
from .country import Country
from .thumbnail import Thumbnail


@dataclass
class Document():

    thumbnail: Thumbnail
    date: Date
    author: Author
    country: Country