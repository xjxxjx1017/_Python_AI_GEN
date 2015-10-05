import random

#---- A wrapped random number generator
class RandomEx(object):

    # $ Create a random generator with a seed (default: system time)
    def __init__(self, _seed=-1):
        self.seed = 0
        self.r = 0

        self.seed = _seed
        self.r = random.Random()
        if self.seed != -1:
            self.r.seed(self.seed)

    # # a <= N <= b (int)
    def randomInt(self, min, max):
        return self.r.randint(min, max)

    # # a <= N < b (float)
    def randomFloat(self, min, max):
        return self.r.uniform(min, max)

    # # 0 <= N < 1 (float)
    def random(self):
        return self.r.random()

# $ To initialize static parameters (below)
def instance_r():
    return RandomEx()

# $ A global random number generator, for common use
r = instance_r()