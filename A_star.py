# -*- coding: utf-8 -*-
import math
import copy


class Node:
    # 当前货架所处的位置，机器人申请打开的巷道，这个区域内一共有多少条巷道和此节点的父节点。
    def __init__(self, racks_positions, request_alley, capacity, parent_node=None):
        self.racks_positions = racks_positions
        self.request_alley = request_alley
        self.capacity = capacity
        self.parent_node = parent_node
        if self.parent_node is None:
            self.g = 0
        else:
            self.g = self.parent_node.g + 1
        self.h = self.getHeuristicCost()
        self.f = self.g + self.h

    # 计算启发项。
    def getHeuristicCost(self):
        minimal_dist = math.inf
        for rack in range(self.capacity):
            if (rack not in self.racks_positions):
                dist = abs(rack - self.request_alley)
                if (dist < minimal_dist):
                    minimal_dist = dist
        return minimal_dist

    # 改变此节点的父节点。
    def resetParentNode(self, new_parent_node):
        if (new_parent_node != self.parent_node):
            self.parent_node = new_parent_node
            if self.parent_node is None:
                self.g = 0
            else:
                self.g = self.parent_node.g + 1
            self.f = self.g + self.h

    # 检查此时能不能满足机器人的要求。
    def isValidSolution(self):
        return self.racks_positions.count(self.request_alley) == 0


class AStarAlgorithm:
    # 使用货架当前的排列，机器人请求进入的位置和可以容纳货架的数量进行初始化。
    def __init__(self, initial_racks_positions, capacity, request_alley):
        self.capacity = capacity
        self.request_alley = request_alley
        self.open_list = []
        self.closed_list = []
        root_node = Node(initial_racks_positions, self.request_alley,
                         self.capacity)
        self.open_list.append(root_node)

    def findSolution(self):
        final_node = None
        solution = []
        while (len(self.open_list) != 0):
            # 从open list中选出f值最小的节点将它加入到closed list中。
            node = self.getNodeWithMinimalFValueFromOpenList()
            self.open_list.remove(node)
            self.closed_list.append(node)
            # 如果在这个节点中机器人要求的巷道已经开放则找到了答案。
            if node.isValidSolution():
                final_node = node
                break
            # 所有与这个节点相连的节点。
            neighbors = self.getNeighborsOfNode(node)
            for neighbor in neighbors:
                # 如果这个邻节点已经在closed list中则跳过。
                if neighbor in self.closed_list:
                    continue
                # 如果这个邻节点已经在open list中则检查将它的父节点设置为node后是否可以减小它的f值。
                elif neighbor in self.open_list:
                    # 检查将neighbor的父节点设为node会不会减少它的f。
                    if (node.g + 1 + neighbor.h < neighbor.f):
                        neighbor.resetParentNode(node)
                # 如果这个节点之前没有被发现过，将它加入到open list中。
                else:
                    self.open_list.append(neighbor)
        if (final_node != None):
            node = final_node
            solution.append(node)
            while (node.parent_node != None):
                node = node.parent_node
                solution.append(node)
            solution.reverse()
        return solution

    def getNodeWithMinimalFValueFromOpenList(self):
        min_f = math.inf
        for node in self.open_list:
            if node.f < min_f:
                node_chosen = node
                min_f = node.f
        return node_chosen

    def getNeighborsOfNode(self, node):
        neighbors = []
        # 对于当前的每一个货架。
        for i in range(len(node.racks_positions)):
            rack = node.racks_positions[i]
            # 如果可以将它向左移动一步则生成一个新的neighbor节点。
            if (rack - 1 >= 0 and node.racks_positions.count(rack-1) == 0):
                new_racks_positions = copy.deepcopy(node.racks_positions)
                new_racks_positions[i] = rack-1
                neighbors.append(Node(new_racks_positions, self.request_alley, self.capacity,
                                      parent_node=node))
            # 如果可以将它向右移动一步则生成一个新的neighbor节点。
            if (rack + 1 < node.capacity and node.racks_positions.count(rack+1) == 0):
                new_racks_positions = copy.deepcopy(node.racks_positions)
                new_racks_positions[i] = rack+1
                neighbors.append(Node(new_racks_positions, self.request_alley, self.capacity,
                                      parent_node=node))
        return neighbors
