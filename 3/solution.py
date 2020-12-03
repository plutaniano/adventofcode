l = open('input.txt').read().split()

def slope(x_step, y_step, tree_map=l):
	x = 0
	trees = 0
	width = len(tree_map[0])
	for i in range(0, len(tree_map), y_step):
		if tree_map[i][x] == '#':
				trees += 1
		x += x_step
		x %= width
	return trees


print(f'Part 1: {slope(3, 1)}')


print('Part 2: ', end='')
print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
