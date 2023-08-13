from dataclasses import dataclass
from pendulum import Date

from .author import Author
from .country import Country


@dataclass
class Document():

    date: Date
    author: Author
    country: Country