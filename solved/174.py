from collections import Counter


def laminae_tiles(hole_size=2, ring_size=2):
    tot_size = hole_size + 2 * ring_size
    return tot_size * tot_size - hole_size * hole_size


def solve(max_tiles=1000):
    counts = Counter()
    hole_size = 0
    while True:
        hole_size += 1
        ring_size = 1
        n_laminae = laminae_tiles(hole_size, ring_size)
        if n_laminae > max_tiles:
            break
        while True:
            ring_size += 1
            counts[n_laminae] += 1
            n_laminae = laminae_tiles(hole_size, ring_size)
            if n_laminae > max_tiles:
                break
    grouped = Counter(counts.values())
    return sum(grouped[j] for j in range(1, 11))


def main():
    print(solve(1000000))


if __name__ == '__main__':
    main()
