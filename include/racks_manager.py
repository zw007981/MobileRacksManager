# -*- coding: utf-8 -*-


class RacksManager:
    # 这个区域可容纳的移动货架上限，当前移动货架的数目。
    def __init__(self, capacity, num_racks):
        # 显然的可容纳的货架数量大于现有货架的数量同时现有货架的数量不小于0.
        assert (capacity > num_racks and num_racks >= 0)
        # 这个区域可以容纳多少个货架，正好等于这个区域内巷道的条数。
        self.capacity = capacity
        # 这个区域当前有多少个货架。
        self.num_racks = num_racks
        # 这些货架当前的位置，等于当前所处巷道的编号。
        self.racks_positions = [0] * self.num_racks

    # 设定每个货架的位置。
    def setRacksPositions(self, positions):
        assert (len(positions) == self.num_racks)
        for rack_position in positions:
            assert(rack_position >= 0 and rack_position < self.capacity
                   and positions.count(rack_position) == 1)
        self.racks_positions = positions

    def getRacksPositions(self):
        return self.racks_positions
