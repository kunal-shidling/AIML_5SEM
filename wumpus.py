import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.world = [['' for _ in range(size)] for _ in range(size)]
        self.agent_pos = (0, 0)
        self.has_gold = False
        positions = [(i, j) for i in range(size) for j in range(size) if (i, j) != (0, 0)]
        random.shuffle(positions)
        self.wumpus = positions.pop()
        self.gold = positions.pop()
        self.pits = random.sample(positions, k=size // 2)
        self._add_percepts()

    def _add_percepts(self):
        for (i, j) in self.pits:
            for x, y in self._adjacent_cells(i, j):
                if 'B' not in self.world[x][y]:
                    self.world[x][y] += 'B'
        (i, j) = self.wumpus
        for x, y in self._adjacent_cells(i, j):
            if 'S' not in self.world[x][y]:
                self.world[x][y] += 'S'

    def _adjacent_cells(self, i, j):
        cells = []
        if i > 0: cells.append((i - 1, j))
        if i < self.size - 1: cells.append((i + 1, j))
        if j > 0: cells.append((i, j - 1))
        if j < self.size - 1: cells.append((i, j + 1))
        return cells

    def get_percepts(self, pos):
        i, j = pos
        percepts = self.world[i][j]
        if pos == self.gold:
            percepts += 'G'
        return percepts

class KnowledgeBase:
    def __init__(self, size=4):
        self.safe = set([(0, 0)])
        self.unsafe = set()
        self.visited = set()
        self.possible_pits = set()
        self.possible_wumpus = set()
        self.size = size

    def tell(self, pos, percepts):
        self.visited.add(pos)
        if 'B' not in percepts and 'S' not in percepts:
            for adj in self._adjacent_cells(pos):
                if adj not in self.visited:
                    self.safe.add(adj)
        else:
            for adj in self._adjacent_cells(pos):
                if 'B' in percepts:
                    self.possible_pits.add(adj)
                if 'S' in percepts:
                    self.possible_wumpus.add(adj)

    def _adjacent_cells(self, pos):
        i, j = pos
        cells = []
        if i > 0: cells.append((i - 1, j))
        if i < self.size - 1: cells.append((i + 1, j))
        if j > 0: cells.append((i, j - 1))
        if j < self.size - 1: cells.append((i, j + 1))
        return cells

    def choose_next_move(self):
        candidates = list(self.safe - self.visited)
        if candidates:
            return random.choice(candidates)
        else:
            return None

class Agent:
    def __init__(self, env):
        self.env = env
        self.kb = KnowledgeBase(size=env.size)
        self.position = env.agent_pos

    def explore(self):
        while True:
            percepts = self.env.get_percepts(self.position)
            print(f"At {self.position} | Percepts: {percepts}")
            if 'G' in percepts:
                print("💰 Found the gold! Agent wins!")
                return
            self.kb.tell(self.position, percepts)
            next_move = self.kb.choose_next_move()
            if not next_move:
                print("No safe moves left. Exploration ends.")
                return
            print(f"→ Moving to {next_move}\n")
            self.position = next_move

if __name__ == "__main__":
    wumpus_world = WumpusWorld(size=4)
    agent = Agent(wumpus_world)
    agent.explore()
