"""pbj: a deliberately tiny package for teaching Git/GitHub workflows.

It "makes" a peanut butter and jelly sandwich in the sense that
:meth:`PBJ.make` prints out the steps of assembling one. See the ``README``
for how this package is used in the workshop.
"""

from .ingredients import Bread, Ingredient, Jelly, PeanutButter, SpreadableIngredient
from .sandwich import PBJ

__version__ = "0.1.0"

__all__ = [
    "PBJ",
    "Ingredient",
    "SpreadableIngredient",
    "Bread",
    "PeanutButter",
    "Jelly",
    "__version__",
]
