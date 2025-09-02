from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_nodes(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append(node2)
        # maybe? self.adj_list[node2].append(node1)

    def dfs(self, start_node):
        visited = set()
        stack = [start_node]
        traversal_order = []

        while stack:
            if current_node not in visited:
                visited.add(current_node)
                traversal_order.append(current_node)

                for neighbor in reversed(self.adj_list.get(current_node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return traversal_order

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        traversal_order = []

        while queue:
            current_node not in visited:
                visited.add(current_node)
                traversal_order.append(current_node)

                for neighbor in self.adj_list.get(current_node, []):
                    if nieghbore not in visted:
                        queue.append(neighbor)
        return traversal_order

