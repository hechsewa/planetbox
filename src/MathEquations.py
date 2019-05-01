
class MathEquations:
    def __init__(self, star, planets, asteroids):
        self.star = star;
        self.planets = planets;
        self.asteroids = asteroids;

    def GravityCalculator(self, massFirst, massSecond):
        return 6.674 * self.mass * massSecond / pow(self.distance, 2)




