def legnagyobb_stadion(path):
    with open(path, "r") as file:
        rows = file.readlines()

        if len(rows) > 0:
            del rows[0]

        largest_stadium = []
        largest_capacity = 0
        for row in rows:
            col = row.split(",")
            current_capacity = int(col[4].strip())

            if current_capacity > largest_capacity:
                largest_capacity = current_capacity
                largest_stadium = col

        with open("legnagyobb.txt", "w") as f:
            if largest_capacity == 0:
                output = "Nincs (Nincs)"
            else:
                output = str(largest_stadium[3].strip()) + " (" + str(largest_stadium[2].strip()) + ")\n"

            f.write(output)


def osszes_arena(path):
    with open(path, "r") as file:
        rows = file.readlines()

        if len(rows) > 0:
            del rows[0]

        arenas = []
        for row in rows:
            col = row.split(",")

            if col[3].strip().endswith("Arena"):
                arenas.append([col[3], col[2], col[7], True if int(col[4].strip()) > 50000 else False])

        with open("arena_park.csv", "w") as f:
            f.write("Stadium,City,Country,Big\n")

            for arena in arenas:
                f.write(
                    f"{str(arena[0].strip())},{str(arena[1].strip())},{str(arena[2].strip())},{str(str(arena[3]))}\n")


def osszes_park(path):
    with open(path, "r") as file:
        rows = file.readlines()

        if len(rows) > 0:
            del rows[0]

        parks = []
        for row in rows:
            col = row.split(",")

            if col[3].strip().endswith("Park"):
                parks.append([col[3], col[2], col[7], True if int(col[4].strip()) > 20000 else False])

        with open("arena_park.csv", "a") as f:
            for park in parks:
                f.write(f"{str(park[0].strip())},{str(park[1].strip())},{str(park[2].strip())},{str(str(park[3]))}\n")


def varosok_szama(path, *c):
    if len(c) == 0:
        raise Exception("Nincs megadva egy orszag sem!")

    with open(path, "r") as file:
        rows = file.readlines()

        if len(rows) > 0:
            del rows[0]

        countries = {}
        for row in rows:
            col = row.split(",")
            country = col[7].strip()

            if country in c:
                if not countries.get(country):
                    countries[country] = []

                if not col[2].strip() in countries[country]:
                    countries[country].append(col[2].strip())

        with open("varosok.txt", "w") as f:
            for country in countries:
                f.write(f"{country} varosai:\n")

                countries[country].sort()

                for city in countries[country]:
                    f.write(f"\t{city}\n")

                f.write("----------\n")
