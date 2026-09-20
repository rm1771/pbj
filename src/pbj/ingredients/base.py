"""Abstract base class shared by every ingredient in the ``pbj`` package.

Design note: every concrete ingredient (bread, peanut butter, jelly, ...)
needs a human-readable name, a quantity, and a way to describe how it gets
"prepared" as part of assembling the sandwich. Putting that shared state and
behavior here means subclasses only need to implement what's actually unique
about them (see :mod:`pbj.ingredients.spread` for the next layer of reuse).
"""

from abc import ABC, abstractmethod


class Ingredient(ABC):
    """Base class for anything that can go into a :class:`pbj.PBJ` sandwich.

    Parameters
    ----------
    name:
        Human-readable name of the ingredient, e.g. ``"whole wheat bread"``.
    quantity:
        Human-readable amount, e.g. ``"2 slices"`` or ``"2 tbsp"``. Optional
        because some hypothetical future ingredient (a pinch of cinnamon?)
        might not need one -- kept as a plain string rather than a number to
        stay agnostic about units (slices vs. tablespoons vs. "a smear").
    """

    def __init__(self, name: str, quantity: str = ""):
        self.name = name
        self.quantity = quantity

    @abstractmethod
    def prepare(self) -> str:
        """Return a description of the prep step for this ingredient.

        Subclasses must implement this -- it's what makes each ingredient
        behave differently when :meth:`pbj.PBJ.make` assembles the sandwich.
        """
        raise NotImplementedError

    def describe(self) -> str:
        """Return a human-readable ``"<quantity> <name>"`` string."""
        if self.quantity:
            return f"{self.quantity} {self.name}"
        return self.name

    def __str__(self) -> str:
        return self.describe()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, quantity={self.quantity!r})"
