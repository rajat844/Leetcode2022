from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine = defaultdict(lambda: SortedSet(key = lambda x: (-x[0],x[1])))
        self.food_to_cuisine = dict()
        self.food_to_rating = dict()
        
        for i in range(len(foods)):
            self.cuisine[cuisines[i]].add((ratings[i],foods[i]))
            self.food_to_cuisine[foods[i]] = cuisines[i]
            self.food_to_rating[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        rat = self.food_to_rating[food]
        cui = self.food_to_cuisine[food]
        
        self.cuisine[cui].discard((rat,food))
        self.cuisine[cui].add((newRating,food))
        self.food_to_rating[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)