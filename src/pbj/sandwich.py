"""The PBJ sandwich itself: assembles ingredients and "makes" the sandwich.

This is intentionally a thin orchestrator: it doesn't know *how* each
ingredient is prepared (that's each :class:`~pbj.ingredients.base.Ingredient`
subclass's job -- see :meth:`~pbj.ingredients.base.Ingredient.prepare`), it
only knows the *order* to assemble them in. That keeps ``PBJ`` open to new
ingredients (e.g. a future ``Honey`` class) without needing to change.
"""

from typing import List, Optional

from .ingredients import Bread, Ingredient, Jelly, PeanutButter


class PBJ:
    """A peanut butter and jelly sandwich, assembled from its ingredients.

    Any ingredient can be swapped out at construction time, so the same
    class can "make" a crunchy-peanut-butter-and-strawberry-jelly sandwich
    just as easily as the classic version.

    Parameters
    ----------
    bread:
        A :class:`~pbj.ingredients.bread.Bread` instance. Defaults to two
        slices of white bread if not provided.
    peanut_butter:
        A :class:`~pbj.ingredients.peanut_butter.PeanutButter` instance.
        Defaults to creamy peanut butter if not provided.
    jelly:
        A :class:`~pbj.ingredients.jelly.Jelly` instance. Defaults to grape
        jelly if not provided.
    """

    def __init__(
        self,
        bread: Optional[Bread] = None,
        peanut_butter: Optional[PeanutButter] = None,
        jelly: Optional[Jelly] = None,
    ):
        self.bread = bread if bread is not None else Bread()
        self.peanut_butter = peanut_butter if peanut_butter is not None else PeanutButter()
        self.jelly = jelly if jelly is not None else Jelly()
        self.is_assembled = False

    @property
    def ingredients(self) -> List[Ingredient]:
        """All ingredients that make up this sandwich, in prep order."""
        return [self.bread, self.peanut_butter, self.jelly]

    def make(self) -> None:
        """Print out the steps to assemble the sandwich.

        This is a teaching demo, not a real kitchen robot -- "making" the
        sandwich just means narrating each ingredient's prep step (by
        calling its polymorphic ``prepare()`` method) in order, then
        printing the final assembly step.
        """
        print("Making a PB&J sandwich...")
        for ingredient in self.ingredients:
            print(f"  - {ingredient.prepare()}")
        print(
            "  - Press the peanut-butter and jelly slices together, "
            "spread sides facing in."
        )
        self.is_assembled = True
        print("Your PB&J sandwich is ready to enjoy!")

    def __repr__(self) -> str:
        return (
            f"PBJ(bread={self.bread!r}, peanut_butter={self.peanut_butter!r}, "
            f"jelly={self.jelly!r})"
        )
