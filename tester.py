"""module intended to test the shortest path functionality using the small data base.


we will import everything from degrees.
1. load the data base using the load data function
2. select a random actor from teh DB
3. get all his neighbors
4. for each neighbor
    4,a check that his path from the original actor is of length1. 
    4.b check that his distance from all other neighbors is 2.
    4.c. check that the path item #1 in the path between each two neighbors is the original actor. 
"""

from degrees import *
import random
from datetime import datetime
import time


def check_and_print_path(path):
    print(f" Number of actors is {len(path)}")
    print(path)

    for i in range(len(path)-1):
        prev_movie_id, person1_id = path[i]
        joint_movie_id, person2_id = path[i+1]
        assert(joint_movie_id in people[person1_id]['movies'])
        assert(joint_movie_id in people[person2_id]['movies'])
        assert((joint_movie_id, person2_id) in neighbors_for_person(person1_id))
        print(f"{i + 1}: {people[person1_id]['name']} and {people[person2_id]['name']} "
              f"starred in {movies[joint_movie_id]['title']}")


def test_sp(directory, iterations):
    print("Loading data...")
    load_data(directory)
    print("Data loaded !")

    total_time = 0
    random.seed(datetime.now())

    for i in range(iterations):
        print(f"*************** iteration {i} ************\n")
        test_source = str(random.choice(list(range(130, 300, 1))))
        test_target = str(random.choice(list(range(130, 300, 1))))
        print(f"calculating path from {people[test_source]['name']} to {people[test_target]['name']}")
        start_time = time.time()
        path = shortest_path(test_source, test_target)
        end_time = time.time()
        print(f"duration for path was {1000* (end_time - start_time)} milli-seconds")
        total_time += end_time - start_time

        if path is None:
            print("No path\n")
        else:
            path = [(None, test_source)] + path
            check_and_print_path(path)

    print(f" total time was {total_time*1000} millisecond. average per path was {total_time*1000/iterations} milliseconds")


def main(directory, iterations):
    #with cProfile.Profile() as pr:
    test_sp(directory, iterations)
    #pr.print_stats(sort = 1)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
