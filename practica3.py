from math import *
import random


def func(x):
    return pow(((sin(pi * sqrt(pow(x[0], 2) + pow(x[1], 2)))) /
                (pi * sqrt((pow(x[0], 2) + pow(x[1], 2))))), 2)

# aux = round(random.uniform(0.0, 100.0), 3)


class Individual:
    def __init__(self):
        self.gens = []
        self.fitness = 0
        self.probability = 0
        self.random_init()
        self.eval()

    def eval(self):
        self.fitness = func(self.gens)
        # print(self.fitness)

    def random_init(self):
        aux = []
        pool = round(random.uniform(-4, 4), 1)
        while pool == 0:
            pool = round(random.uniform(-4, 4), 1)
        aux.append(pool)
        pool = round(random.uniform(-4, 4), 1)
        while pool == 0:
            pool = round(random.uniform(-4, 4), 1)
        aux.append(pool)
        # print(aux)
        self.gens = aux

    def __repr__(self):
        return ("{} \n".format(
                self.gens))


class Genetic:
    def __init__(self, iterations, elitism, temperature=100):
        self.iterations = iterations
        self.elitism = elitism
        self.temperature = temperature
        self.poblation = Individual()

    def mutation(self, key):
        key[0] = key[0] * round(random.uniform(-1, 1), 1)
        key[1] = key[1] * round(random.uniform(-1, 1), 1)
        return key

    def rulete(self, temperature=None):
        if temperature is None:
            temperature = self.temperature
        nxt_gen = Individual()
        self.poblation.probability = (exp(self.poblation.fitness) / temperature) / ((exp(self.poblation.fitness) / temperature) + exp(nxt_gen.fitness))
        nxt_gen.probability = 1 - self.poblation.probability
        '''
        if round(random.uniform(0, 1), 2) <= mutation_prob:
            nxt_gen = mutation(nxt_gen)
            nxt_gen.eval(nxt_gen)
        '''
        if(nxt_gen.probability > self.poblation.probability):
            if round(random.uniform(0, 1), 2) > self.poblation.probability:
                self.poblation = nxt_gen

        return self.poblation

    def step(self):
        for x in range(0, 10):
            self.rulete()
        return self.poblation

    def run(self):
        for x in range(0, self.iterations):
            self.step()
            self.temperature = self.temperature * 0.99995
            print("temperature")
            print(self.temperature)
            print("poblation")
            print(self.poblation)
            print("fitness")
            print(self.poblation.fitness)


my_genetic = Genetic(100000, 1, 100)
my_genetic.run()

ind = Individual()
