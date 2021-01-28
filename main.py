# -*- coding: utf-8 -*-
from include.A_star import AStarAlgorithm
from include.racks_manager import RacksManager

if __name__ == "__main__":
    # 这个区域可容纳的移动货架上限，当前移动货架的数目。
    racks_manager = RacksManager(10, 8)
    # 设定这些移动货架当前处于哪一个巷道。
    racks_manager.setRacksPositions([1, 2, 3, 4, 5, 6, 7, 8])
    # 此处的request_alley是机器人申请打开通过的巷道。
    A_star = AStarAlgorithm(racks_manager.getRacksPositions(), racks_manager.capacity,
                            request_alley=4)
    solution = A_star.findSolution()
    # 打印结果。
    if (len(solution) == 0):
        print("Unable to find solution.")
    else:
        print("The way racks move: ")
        for node in solution:
            print(node.racks_positions)
        print("The cost is: %d." % (len(solution)-1))
