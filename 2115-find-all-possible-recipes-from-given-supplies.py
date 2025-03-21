"""
Level: Medium
Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
Tags: array, hash-table, string, graph, topological-sort
Description:
You have information about n different recipes. You are given a string array
recipes and a 2D string array ingredients. The ith recipe has the name
recipes[i], and you can create it if you have all the needed ingredients from
ingredients[i]. A recipe can also be an ingredient for other recipes, i.e.,
ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that
you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer
in any order.

Note that two recipes may contain each other in their ingredients.
"""
from collections import deque
class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        recipe_list = {}
        item_list = {}
        preparing = deque(supplies)
        for recipe, ingredient in zip(recipes, ingredients):
            recipe_list[recipe] = set(ingredient)
            for item in ingredient:
                item_list[item] = item_list.get(item, []) + [recipe]
        valid_recipes = []
        while len(preparing) > 0:
            supply = preparing.popleft()
            if supply in item_list:
                for item_supply in item_list[supply]:
                    recipe_list[item_supply].discard(supply)
                    if not recipe_list[item_supply]:
                        valid_recipes.append(item_supply)
                        preparing.append(item_supply)
                        del recipe_list[item_supply]
        return valid_recipes