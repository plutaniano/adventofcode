from contextlib import supress
from .base import Solution, ALL_SOLUTIONS

__all__ = ["Solution", "ALL_SOLUTIONS"]

for year in range(2018, 2022):
    for day in range(1, 26):
        with supress(ImportError):
            __import__(f"aoc.{year}", fromlist=(f"Day{day:02}",))
