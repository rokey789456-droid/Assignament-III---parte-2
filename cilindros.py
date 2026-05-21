import sys
import random
import matplotlib.pyplot as plt


DISK_SIZE = 5000
MIN_CYLINDER = 0
MAX_CYLINDER = DISK_SIZE - 1
NUMBER_OF_REQUESTS = 1000


def generateRequests():
    requests = []

    for _ in range(NUMBER_OF_REQUESTS):
        request = random.randint(MIN_CYLINDER, MAX_CYLINDER)
        requests.append(request)

    return requests


def calculateMovement(path):
    totalMovement = 0

    for i in range(1, len(path)):
        totalMovement += abs(path[i] - path[i - 1])

    return totalMovement


def fcfs(requests, initialHead):
    path = [initialHead] + requests
    totalMovement = calculateMovement(path)

    return totalMovement, path


def scan(requests, initialHead):
    lowerRequests = []
    higherRequests = []

    for request in requests:
        if request < initialHead:
            lowerRequests.append(request)
        else:
            higherRequests.append(request)

    lowerRequests.sort(reverse=True)
    higherRequests.sort()

    path = [initialHead]

    for request in higherRequests:
        path.append(request)

    if path[-1] != MAX_CYLINDER:
        path.append(MAX_CYLINDER)

    for request in lowerRequests:
        path.append(request)

    totalMovement = calculateMovement(path)

    return totalMovement, path


def cScan(requests, initialHead):
    lowerRequests = []
    higherRequests = []

    for request in requests:
        if request < initialHead:
            lowerRequests.append(request)
        else:
            higherRequests.append(request)

    lowerRequests.sort()
    higherRequests.sort()

    path = [initialHead]

    for request in higherRequests:
        path.append(request)

    if path[-1] != MAX_CYLINDER:
        path.append(MAX_CYLINDER)

    path.append(MIN_CYLINDER)

    for request in lowerRequests:
        path.append(request)

    totalMovement = calculateMovement(path)

    return totalMovement, path


def graphHeadMovement(path, algorithmName):
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(path)), path, marker="o", markersize=2)
    plt.title(f"Movimiento del cabezal - {algorithmName}")
    plt.xlabel("Orden de atención")
    plt.ylabel("Cilindro")
    plt.grid(True)
    plt.savefig(f"{algorithmName}_head_movement.png")
    plt.show()


def graphPerformanceComparison(fcfsMovement, scanMovement, cScanMovement):
    algorithms = ["FCFS", "SCAN", "C-SCAN"]
    movements = [fcfsMovement, scanMovement, cScanMovement]

    plt.figure(figsize=(8, 5))
    plt.bar(algorithms, movements)
    plt.title("Comparación de movimiento total del cabezal")
    plt.xlabel("Algoritmo")
    plt.ylabel("Movimiento total en cilindros")
    plt.grid(axis="y")
    plt.savefig("performance_comparison.png")
    plt.show()


def main():
    if len(sys.argv) != 2:
        print("Uso: python cilindros.py <posicionInicial>")
        return

    initialHead = int(sys.argv[1])

    if initialHead < MIN_CYLINDER or initialHead > MAX_CYLINDER:
        print("Error: la posicion inicial debe estar entre 0 y 4999.")
        return

    requests = generateRequests()

    fcfsMovement, fcfsPath = fcfs(requests, initialHead)
    scanMovement, scanPath = scan(requests, initialHead)
    cScanMovement, cScanPath = cScan(requests, initialHead)

    print("Resultados de planificacion de disco")
    print("-----------------------------------")
    print(f"Posicion inicial del cabezal: {initialHead}")
    print(f"Cantidad de solicitudes generadas: {NUMBER_OF_REQUESTS}")
    print()
    print(f"Movimiento total FCFS: {fcfsMovement} cilindros")
    print(f"Movimiento total SCAN: {scanMovement} cilindros")
    print(f"Movimiento total C-SCAN: {cScanMovement} cilindros")

    graphHeadMovement(fcfsPath, "FCFS")
    graphHeadMovement(scanPath, "SCAN")
    graphHeadMovement(cScanPath, "C-SCAN")
    graphPerformanceComparison(fcfsMovement, scanMovement, cScanMovement)


main()