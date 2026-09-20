"""Bread: the one ingredient that isn't spread, it's just laid out."""

from .base import Ingredient


class Bread(Ingredient):
    """The two slices of bread that hold everything together.

    Parameters
    ----------
    slices:
        Number of slices. Defaults to 2 -- a sandwich assumption, not a
        general one (a "PB&J open-face" would be a different class entirely).
    bread_type:
        Kind of bread, e.g. ``"white"``, ``"whole wheat"``, ``"sourdough"``.
    """

    def __init__(self, slices: int = 2, bread_type: str = "white"):
        super().__init__(name=f"{bread_type} bread", quantity=f"{slices} slices")
        self.slices = slices
        self.bread_type = bread_type

    def prepare(self) -> str:
        return f"Lay out {self.describe()} on a clean plate or cutting board."
