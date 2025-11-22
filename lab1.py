import sys 

def count_alive_neighbors(field, r, c):
    h = len(field)
    w = len(field[0])
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr = (r + dr) % h
            nc = (c + dc) % w
            if field[nr][nc] == 'x':
                count += 1
    return count

def next_generation(field):
    h = len(field)
    w = len(field[0])
    new_field = [list(row) for row in field]
    for r in range(h):
        for c in range(w):
            alive_neighbors = count_alive_neighbors(field, r, c)
            if field[r][c] == 'x':
                if alive_neighbors == 2 or alive_neighbors == 3:
                    new_field[r][c] = 'x'
                else:                
                    new_field[r][c] = '.'
            else :
                if alive_neighbors == 3:
                    new_field[r][c] = 'x'
                else:
                    new_field[r][c] = '.'
    return [''.join(row) for row in new_field]

def evolve(field, generations):
    for _gen in range(generations):
        field = next_generation(field)
    return field

def main():
    data = sys.stdin.read().strip().splitlines()
    generations = int(data[0].strip())
    w_h = data[1].split()
    w = int(w_h[0])
    h = int(w_h[1])
    field = [line.strip() for line in data[2:2+h]]
    field = evolve(field, generations)
    for row in field:
        print(row)

if __name__ == "__main__":
    main()

