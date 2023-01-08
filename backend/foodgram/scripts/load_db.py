from recipes.models import Ingredient
import csv


def run():
    with open('recipes/ingredients.csv') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(row)

            name, measurement_unit = Ingredient.objects.get_or_create(name=row)

            ingredient = Ingredient(
                name=name,
                measurement_unit=measurement_unit
            )
            ingredient.save()
