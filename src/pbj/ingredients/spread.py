"""Shared behavior for ingredients that get spread onto bread.

Peanut butter and jelly are prepared the same way in real life -- scoop an
amount and spread it across a side of bread -- so that logic lives once here
instead of being duplicated in both :class:`~pbj.ingredients.peanut_butter.PeanutButter`
and :class:`~pbj.ingredients.jelly.Jelly`.
"""

from .base import Ingredient


class SpreadableIngredient(Ingredient):
    """Base class for ingredients applied to bread with a spreading motion.

    Parameters
    ----------
    name:
        Human-readable name, e.g. ``"creamy peanut butter"``.
    amount_tbsp:
        Amount to use, in tablespoons. A plain number (rather than a string)
        because subclasses may want to do math with it (e.g. scale a recipe).
    side:
        Which slice of bread this gets spread on, e.g. ``"bottom slice"``.
    """

    def __init__(self, name: str, amount_tbsp: float = 2, side: str = "bottom slice"):
        super().__init__(name=name, quantity=f"{amount_tbsp} tbsp")
        self.amount_tbsp = amount_tbsp
        self.side = side

    def prepare(self) -> str:
        return f"Spread {self.describe()} evenly across the {self.side} of bread."
