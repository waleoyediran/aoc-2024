import collections

def main():
    with open('input/day01.txt', 'r') as file:
        lines = file.readlines()
    left, right = [], collections.defaultdict(int)
    for line in lines:
        l, r = map(int, line.split(' ', 1))
        left.append(l)
        right[r] += 1

    cum_score = 0
    for num in left:
        cum_score += num * right[num]

    print(cum_score)


if __name__ == '__main__':
    main()
