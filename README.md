# pbj

This is another change to the readme on the same line

An example repo for a GitHub lesson. It's a tiny, deliberately
over-engineered Python package that "makes" a peanut butter and jelly
sandwich, based on the class's PB&J pseudocoding activity.

"Making" the sandwich just means printing out the assembly steps -- this
package exists to demonstrate Python packaging, object-oriented design, and
Git/GitHub workflows, not to actually make food.

## Design

- `pbj.ingredients.Ingredient` -- abstract base class for anything that goes
  into the sandwich (a name, a quantity, and a `prepare()` step).
- `pbj.ingredients.SpreadableIngredient` -- shared base for ingredients that
  get spread onto bread, so `PeanutButter` and `Jelly` don't duplicate that
  logic.
- `pbj.ingredients.Bread`, `pbj.ingredients.PeanutButter`,
  `pbj.ingredients.Jelly` -- concrete ingredients.
- `pbj.PBJ` -- assembles a list of ingredients and, via `.make()`, prints out
  the steps to build the sandwich.

## Install (locally, editable)

```bash
pip install -e ".[test]"
```

## Usage

```python
from pbj import PBJ

sandwich = PBJ()
sandwich.make()
```

Or from the command line:

```bash
make-pbj
# or: python -m pbj
```

## Tests

```bash
pytest
```
