# Author: Kaustav Ghosh
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from collections import defaultdict, deque

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        indegree = {}
        graph = defaultdict(list)
        recipe_set = set(recipes)

        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)

        queue = deque(supplies)
        result = []

        while queue:
            item = queue.popleft()
            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)

        return result
