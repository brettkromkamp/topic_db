"""
DataType enumeration. Part of the StoryTechnologies project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from enum import Enum


class DataType(Enum):
    STRING = 1
    NUMBER = 2
    TIMESTAMP = 3
    BOOLEAN = 4

    def __str__(self):
        return self.name
