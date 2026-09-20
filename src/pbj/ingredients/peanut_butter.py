"""Peanut butter: a spreadable ingredient with a "style" (creamy/crunchy)."""

from .spread import SpreadableIngredient


class PeanutButter(SpreadableIngredient):
    """Peanut butter, spread on one slice of bread.

    Parameters
    ----------
    amount_tbsp:
        How much peanut butter to use, in tablespoons.
    style:
        ``"creamy"`` or ``"crunchy"``. Defaults to ``"creamy"`` -- an
        arbitrary but common default, easily overridden by crunchy-PB fans.
    side:
        Which slice of bread to spread it on.
    """

    def __init__(self, amount_tbsp: float = 2, style: str = "creamy", side: str = "bottom slice"):
        self.style = style
        super().__init__(name=f"{style} peanut butter", amount_tbsp=amount_tbsp, side=side)
