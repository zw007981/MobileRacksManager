from racks_manager import *
from A_star import *

if __name__ == "__main__":
    racks_manager = RacksManager(10, 8)
    racks_manager.setRacksPositions([1, 2, 3, 4, 5, 6, 7, 8])
    A_star = AStarAlgorithm(racks_manager.getRacksPositions(), racks_manager.capacity,
                            request_rack=3)
    solution = A_star.findSolution()
    if (len(solution) == 0):
        print("Unable to find solution.")
    else:
        print("The way racks move: ")
        for node in solution:
            print(node.racks_positions)
        print("The cost is: %d." % (len(solution)-1))
