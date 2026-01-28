"""
Problem: Find All Possible Recipes from Given Supplies
Difficulty: Medium

You are given information about n different recipes. Each recipe is listed in the
array recipes, and its corresponding ingredients are provided in the 2D array
ingredients. The i-th recipe, recipes[i], can be prepared if all the necessary
ingredients listed in ingredients[i] are available.

Some ingredients might need to be created from other recipes, meaning ingredients[i]
may contain strings that are also in recipes.

Additionally, you have a string array supplies that contains all the ingredients
you initially have, and you have an infinite supply of each.

Return a list of all the recipes you can create. The answer can be returned in any order.

Note: It is possible for two recipes to list each other as ingredients. However,
if these are the only two recipes provided, the expected output is an empty list.

Constraints:
- n == recipes.length == ingredients.length
- 1 <= n <= 100
- 1 <= ingredients[i].length, supplies.length <= 100
- 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
- recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
- All the combined values of recipes and supplies are unique.
- Each ingredients[i] doesn't contain any duplicate values.

Example 1:
Input: recipes = ["bread"], ingredients = [["yeast", "flour"]], supplies = ["yeast", "flour", "sugar"]
Output: ["bread"]
Explanation: We have yeast and flour in supplies, so we can make bread.

Example 2:
Input: recipes = ["bread", "sandwich"], ingredients = [["yeast", "flour"], ["bread", "meat"]],
       supplies = ["yeast", "flour", "meat"]
Output: ["bread", "sandwich"]
Explanation: We can make bread (from yeast, flour). Then we can make sandwich (from bread, meat).

Example 3:
Input: recipes = ["bread", "sandwich", "burger"],
       ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
       supplies = ["yeast", "flour", "meat"]
Output: ["bread", "sandwich", "burger"]
Explanation: bread -> sandwich -> burger (chain of dependencies)

Example 4:
Input: recipes = ["a", "b"], ingredients = [["b"], ["a"]], supplies = []
Output: []
Explanation: Recipe "a" needs "b", and "b" needs "a" - circular dependency, neither can be made.

Example 5:
Input: recipes = ["tea", "omelette"]
       ingredients = [["milk", "caffeine", "sugar"], ["salt", "egg", "pepper"]]
       supplies = ["salt", "milk", "egg", "caffeine", "sugar"]
Output: ["tea"]
Explanation: Tea needs milk, caffeine, sugar - all available. Omelette needs pepper which is missing.

Example 6:
Input: recipes = ["sandwich", "mojito"]
       ingredients = [["cheese", "vegetables", "bread", "salad"], ["rum", "mint", "syrup"]]
       supplies = ["cheese", "rum", "bread", "salad", "vegetables", "mint", "syrup"]
Output: ["sandwich", "mojito"]
Explanation: Both recipes have all their ingredients available in supplies.
"""

"""
r = ["tea", "omlette"]
i = [["milk","caffeine","sugar"], ["salt", "egg", "pepper"]]
s = ["salt","milk","egg","caffeine","sugar"]

indegrees = {"tea":0, "omlette":1}
adj = {"milk":["tea"], "caffeine": ["tea"], "sugar": ["tea"], "salt":["omlette"], "egg":["omlette"], "pepper": ["omlette"]}

q = []

res = [tea]

"""
from collections import deque
def solution(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    indegree = {}
    adj = {}
    recipe_set = set(recipes)

    for i, r in enumerate(recipes):
        indegree[r] = 0
        for ing in ingredients[i]:
            adj[ing] = []
    

    for i, r in enumerate(recipes):
        for ing in ingredients[i]:
            indegree[r] += 1
            adj[ing].append(r)

    q = deque()

    for s in supplies:
        q.append(s)

    res = []
    while len(q) != 0 :
        s = q.popleft()
        if s in recipe_set:
            res.append(s)

        for a in adj.get(s, []):
            indegree[a] -= 1
            if indegree[a] == 0 :
                q.append(a)
        
    return res



# Comparator: order doesn't matter, just check same recipes can be made
def compare_results(result: list[str], expected: list[str]) -> bool:
    return sorted(result) == sorted(expected)


TEST_CASES = [
    # Basic: single recipe with available supplies
    ((["bread"], [["yeast", "flour"]], ["yeast", "flour", "sugar"]), ["bread"]),

    # Chain: recipe depends on another recipe
    ((["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"]),
     ["bread", "sandwich"]),

    # Longer chain
    ((["bread", "sandwich", "burger"],
      [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
      ["yeast", "flour", "meat"]),
     ["bread", "sandwich", "burger"]),

    # Circular dependency - impossible
    ((["a", "b"], [["b"], ["a"]], []), []),

    # Missing supply - can't make recipe
    ((["bread"], [["yeast", "flour"]], ["yeast"]), []),

    # Independent recipes - both makeable
    ((["bread", "soup"], [["flour", "yeast"], ["water", "vegetables"]],
      ["flour", "yeast", "water", "vegetables"]),
     ["bread", "soup"]),

    # Partial: only some recipes makeable
    ((["bread", "cake"], [["flour", "yeast"], ["flour", "eggs", "sugar"]],
      ["flour", "yeast"]),
     ["bread"]),

    # Recipe needs another recipe that can't be made
    ((["sandwich", "bread"], [["bread", "meat"], ["yeast", "flour"]], ["meat"]), []),

    # Empty recipes
    (([], [], ["flour", "yeast"]), []),

    # All supplies available, multiple independent recipes
    ((["a", "b", "c"], [["x"], ["y"], ["z"]], ["x", "y", "z"]), ["a", "b", "c"]),

    # Sample example 1: tea vs omelette (pepper missing)
    ((["tea", "omelette"],
      [["milk", "caffeine", "sugar"], ["salt", "egg", "pepper"]],
      ["salt", "milk", "egg", "caffeine", "sugar"]),
     ["tea"]),

    # Sample example 2: sandwich and mojito (all supplies available)
    ((["sandwich", "mojito"],
      [["cheese", "vegetables", "bread", "salad"], ["rum", "mint", "syrup"]],
      ["cheese", "rum", "bread", "salad", "vegetables", "mint", "syrup"]),
     ["sandwich", "mojito"]),
]
