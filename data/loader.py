import csv
from models.aircraft import Aircraft
from models.route import Route

def load_fleet(filepath):
    fleet = []

    with open(filepath, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            fleet.append(
                Aircraft(
                    name=row["name"],
                    seats=int(row["seats"]),
                    range=int(row["range"]),
                    availableCount=int(row["availableCount"])
                )
            )

    return fleet

def load_routes(filepath):
    routes = []

    with open(filepath, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            routes.append(
                Route(
                    origin=row["origin"],
                    destination=row["destination"],
                    distance=int(row["distance"]),
                    demand=int(row["demand"])
                )
            )

    return routes
print("Data loader functions defined successfully.")
