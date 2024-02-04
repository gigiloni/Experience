class Station:
    def __init__(self, name, routes=None):
        self.name = name
        if routes is None:
            self.routes = {}

    def add_route(self, station, time):
        self.routes[station] = time

    def shortest_path_to(self, destination):
        best_previous_stopovers = self.stopover_table_for(self)

        best_path = []
        current_station = destination.name

        while current_station != self.name:
            best_path.append(current_station)
            current_station = best_previous_stopovers[current_station]
        best_path.append(self.name)

        # best_path.sort(reverse=True)
        best_path = sorted(best_path, reverse=True)
        return best_path

    def stopover_table_for(self, starting_station):
        fastest_table = {}
        unvisited_stations = [starting_station]
        visited_stations = {}
        best_previous_stopovers = {}

        fastest_table[starting_station.name] = 0
        current_station = starting_station

        while unvisited_stations:
            current_station = unvisited_stations.pop(0)
            visited_stations[current_station.name] = True

            for adjacent_station, time in current_station.routes.items():
                if not visited_stations.get(adjacent_station.name):
                    unvisited_stations.append(adjacent_station)

                time_through_current_station = fastest_table[current_station.name] + time

                if (not fastest_table.get(adjacent_station.name) or time_through_current_station <
                        fastest_table[adjacent_station.name]):
                    fastest_table[adjacent_station.name] = time_through_current_station
                    best_previous_stopovers[adjacent_station.name] = current_station.name

        return best_previous_stopovers


a = Station(name='Academic')
b = Station(name='Barrikad')
c = Station(name='Selikat')
d = Station(name='Dinamo')
e = Station(name='Electro')

a.add_route(station=b, time=5)
a.add_route(station=d, time=8)

b.add_route(station=a, time=5)
b.add_route(station=c, time=6)
b.add_route(station=d, time=9)

c.add_route(station=e, time=15)

d.add_route(station=c, time=2)
d.add_route(station=e, time=4)

shortest_path_a_e = a.shortest_path_to(e)
print(f'Shortest path: {shortest_path_a_e}')

shortest_path_b_e = b.shortest_path_to(e)
print(f'Shortest path: {shortest_path_b_e}')
