
def main():
    with open('input/day01.txt', 'r') as file:
        lines = file.readlines()
    left, right = [], []
    for line in lines:
        l, r = map(int, line.split(' ', 1))
        left.append(l)
        right.append(r)
    left.sort()
    right.sort()

    cum_distance = 0
    for i in range(len(left)):
        cum_distance += abs(left[i] - right[i])

    print(cum_distance)


if __name__ == '__main__':
    main()
