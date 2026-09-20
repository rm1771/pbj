"""Example unit test for the pbj package (run with ``pytest``).

Just one illustrative test for now -- more can be added as part of the
workshop lesson on testing.
"""

import pytest

from pbj import PBJ, Ingredient, Jelly, PeanutButter


def test_make_prints_assembly_steps(capsys):
    """PBJ.make() should narrate each ingredient and finish the sandwich."""
    sandwich = PBJ()
    sandwich.make()

    output = capsys.readouterr().out.lower()
    assert "peanut butter" in output
    assert "jelly" in output
    assert "bread" in output
    assert "ready to enjoy" in output
    assert sandwich.is_assembled is True


def test_custom_ingredients_are_used():
    """Swapping in custom ingredients should be reflected in the sandwich."""
    pb = PeanutButter(amount_tbsp=3, style="crunchy")
    jelly = Jelly(amount_tbsp=1, flavor="strawberry")
    sandwich = PBJ(peanut_butter=pb, jelly=jelly)

    assert sandwich.peanut_butter.style == "crunchy"
    assert sandwich.jelly.flavor == "strawberry"


def test_ingredient_is_abstract():
    """Ingredient can't be instantiated directly since prepare() is abstract."""
    with pytest.raises(TypeError):
        Ingredient(name="mystery ingredient")
