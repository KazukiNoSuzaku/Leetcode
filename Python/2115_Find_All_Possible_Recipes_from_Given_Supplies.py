# Author: Kaustav Ghosh
# Problem: Find All Possible Recipes from Given Supplies
# Approach: Start with the base supplies as available. Repeatedly mark any recipe whose ingredients are all available (adding it to the available set) until no new recipe can be made. Those marked recipes are the answer

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        available = set(supplies)
        recipe_ings = dict(zip(recipes, ingredients))
        remaining = set(recipes)
        made = []
        changed = True
        while changed:
            changed = False
            for r in list(remaining):
                if all(ing in available for ing in recipe_ings[r]):
                    available.add(r)
                    made.append(r)
                    remaining.discard(r)
                    changed = True
        return made
