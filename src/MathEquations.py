
class MathEquations:
    def __init__(self, star, planets, asteroids):
        self.star = star;
        self.planets = planets;
        self.asteroids = asteroids;

    def KeplersFirstLaw(self, planet, sun): # calculates distance between planet and star
        a = (-1) * ((planet.gravity * planet.mass * sun.mass) / 2) # * U  # U = |Ek| - |Ep|
        return a

   # def CalculateEnergy(self, planet, sun):
       # U = # no fkn clue, both Ek and Ep has this radius in their
       # return U







