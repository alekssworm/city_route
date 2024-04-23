import random

# Create a list of cities and their coordinates (x, y)
cities = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (2, 5),
    'D': (4, 3),
    'E': (5, 0)
}

# Function to calculate the length of a route
def route_length(route):
    total_distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_distance += ((cities[city1][0] - cities[city2][0]) ** 2 + 
                           (cities[city1][1] - cities[city2][1]) ** 2) ** 0.5
    return total_distance

# Genetic algorithm to find the shortest route
def genetic_algorithm(cities, population_size=100, generations=1000):
    num_cities = len(cities)
    population = [list(cities.keys()) for _ in range(population_size)]
    for _ in range(generations):
        population = sorted(population, key=lambda x: route_length(x))
        # Select the best routes for mating
        selected = population[:population_size // 2]
        # Create a new generation
        new_generation = []
        while len(new_generation) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            crossover_point = random.randint(0, num_cities - 1)
            child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
            new_generation.append(child)
        population = new_generation
    best_route = min(population, key=lambda x: route_length(x))
    return best_route, route_length(best_route)

# Run the genetic algorithm
best_route, shortest_distance = genetic_algorithm(cities)
print("Shortest route:", best_route)
print("Length of the route:", shortest_distance)
