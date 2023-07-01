class ShortestRoute:
    def __init__(self, map, start):
        self.map = map
        self.start = start

    def length(self):
        pass

    def path(self):
        pass


if __name__ == "__main__":
    map = [(1, 4), (2, 4), (3, 2), (4, 5)]
    start = 1
    route = ShortestRoute(map, start)
    print(route.path())