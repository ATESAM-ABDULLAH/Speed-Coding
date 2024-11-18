import heapq
from copy import deepcopy


def max_rounds(queries):
    heroes = []
    artifacts = []

    for query_type, value in queries:
        if query_type == 1:
            heroes.append(value)
        else:
            artifacts.append(value)

        # Create copies of the current state for the simulation
        sim_heroes = deepcopy(heroes)
        sim_artifacts = deepcopy(artifacts)

        rounds = 0
        while sim_heroes:
            damage = round(1 / (len(sim_heroes) + len(sim_artifacts)), 2)

            rounds += 1
            



        print(rounds)


# Example usage:
queries = [(2, 5), (1, 4), (1, 10)]
max_rounds(queries)
