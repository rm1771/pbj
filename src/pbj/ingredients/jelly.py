"""Jelly: a spreadable ingredient with a "flavor" (grape/strawberry/...)."""

from .spread import SpreadableIngredient


class Jelly(SpreadableIngredient):
    """Jelly (or jam), spread on the other slice of bread.

    Parameters
    ----------
    amount_tbsp:
        How much jelly to use, in tablespoons.
    flavor:
        Fruit flavor, e.g. ``"grape"``, ``"strawberry"``, ``"raspberry"``.
        Defaults to ``"grape"`` as the classic PB&J pairing.
    side:
        Which slice of bread to spread it on. Defaults to the slice opposite
        peanut butter's default so the two don't collide when both classes
        are used with their defaults.
    """

    def __init__(self, amount_tbsp: float = 2, flavor: str = "grape", side: str = "top slice"):
        self.flavor = flavor
        super().__init__(name=f"{flavor} jelly", amount_tbsp=amount_tbsp, side=side)
