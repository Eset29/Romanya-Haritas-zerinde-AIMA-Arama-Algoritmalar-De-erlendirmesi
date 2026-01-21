from collections import deque

# Romania şehir haritası (AIMA örneği)
romania_map = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Pitesti": 138, "Rimnicu Vilcea": 146},
    "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucharest": 90},
    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87},
}


def dfs_tree_search(start: str, goal: str):
    stack = [(start, None)]
    parents = {start: None}
    iterations = 0

    while stack:
        node, parent = stack.pop()
        iterations += 1

        if node not in parents:
            parents[node] = parent

        if node == goal:
            return iterations, reconstruct_path(parents, goal), True

        for child in romania_map[node]:
            if child != parent:  # aynı yöne geri dönmekten kaçınma
                stack.append((child, node))

    return iterations, [], False


def bfs_tree_search(start: str, goal: str):
    queue = deque([(start, None)])
    parents = {start: None}
    iterations = 0

    while queue:
        node, parent = queue.popleft()
        iterations += 1

        if node not in parents:
            parents[node] = parent

        if node == goal:
            return iterations, reconstruct_path(parents, goal), True

        for child in romania_map[node]:
            if child != parent:
                queue.append((child, node))

    return iterations, [], False


def dfs_graph_search(start: str, goal: str):
    stack = [start]
    parents = {start: None}
    visited = set()
    iterations = 0

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        iterations += 1

        if node == goal:
            return iterations, reconstruct_path(parents, goal), True

        for child in romania_map[node]:
            if child not in visited:
                parents.setdefault(child, node)
                stack.append(child)

    return iterations, [], False


def bfs_graph_search(start: str, goal: str):
    queue = deque([start])
    parents = {start: None}
    visited = {start}
    iterations = 0

    while queue:
        node = queue.popleft()
        iterations += 1

        if node == goal:
            return iterations, reconstruct_path(parents, goal), True

        for child in romania_map[node]:
            if child not in visited:
                visited.add(child)
                parents[child] = node
                queue.append(child)

    return iterations, [], False


def reconstruct_path(parents, goal):
    path = []
    node = goal
    while node is not None and node in parents:
        path.append(node)
        node = parents[node]
    path.reverse()
    return path


def main():
    start, goal = "Arad", "Bucharest"

    dfs_tree = dfs_tree_search(start, goal)
    bfs_tree = bfs_tree_search(start, goal)
    dfs_graph = dfs_graph_search(start, goal)
    bfs_graph = bfs_graph_search(start, goal)

    print(f"DFS-Tree: {dfs_tree}")
    print(f"BFS-Tree: {bfs_tree}")
    print(f"DFS-Graph: {dfs_graph}")
    print(f"BFS-Graph: {bfs_graph}")


if __name__ == "__main__":
    main()


