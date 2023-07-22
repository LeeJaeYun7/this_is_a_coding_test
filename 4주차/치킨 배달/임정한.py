#wrong
class City:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.houses = []
        self.chicken_shops = []

    def add_house(self, r, c):
        self.houses.append((r, c))

    def add_chicken_shop(self, r, c):
        self.chicken_shops.append((r, c))

    def chicken_distance(self, house, chicken_shop):
        hx, hy = house
        cx, cy = chicken_shop
        return abs(hx-cx) + abs(hy-cy)

    def min_chicken_distance(self, open_shops):
        distance = 0
        for house in self.houses:
            single_distance = 1e9
            for chicken_shop in open_shops:
                single_distance =  min(single_distance, self.chicken_distance(house, chicken_shop))
            distance +=single_distance
        return distance


    def find_optimal_shops(self):
        def worker(open_shops):
            if len(open_shops) == 1:
                return self.min_chicken_distance(open_shops), open_shops
            min_distance, efficient_shopcase = 1e9, []
            n_shops = len(open_shops)
            for i in range(n_shops):
                local_shops = open_shops[0:i]+open_shops[i+1:n_shops]
                local_distance, _ = worker(local_shops)
                if local_distance < min_distance:
                    efficient_shopcase = local_shops
                    min_distance = local_distance
                print("?", local_shops, local_distance, min_distance)

            return min_distance, efficient_shopcase
        case = self.chicken_shops
        for i in range(len(self.chicken_shops) - self.M):
            print(i, case)
            distance, case = worker(case)
        return case




N, M = map(int, input().split())

city = City(N, M)

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            city.add_house(r+1, c+1)
        elif row[c] == 2:
            city.add_chicken_shop(r+1, c+1)

case = city.find_optimal_shops()
distance = city.min_chicken_distance(case)
print(case)
print(distance)
