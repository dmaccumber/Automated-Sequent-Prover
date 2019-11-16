from parser import *

'''
Below is every rule applied to sequents in order to see whether they hold

Parameters:
sequent(Sequent): an instance of Sequent that holds both sides of a sequent in prefix notation
'''
def two_a(sequent):
	used = False
	updated_left = []
	updated_right = []
	left = sequent.left
	right = sequent.right

	for f in right:
		if used:
			updated_right.append(f)
		else:
			if f[0] == 'neg':
				updated_left.append(f[1])
				used = True
			else:
				updated_right.append(f)
	for f in left:
		updated_left.append(f)
	
	return used, (Sequent(updated_left, updated_right),)

def two_b(sequent):
	used = False
	updated_left = []
	updated_right = []
	left = sequent.left
	right = sequent.right

	for f in left:
		if used:
			updated_left.append(f)
		else:
			if f[0] == 'neg':
				updated_right.append(f[1])
				used = True
			else:
				updated_left.append(f)
	for f in right:
		updated_right.append(f)
	
	return used, (Sequent(updated_left, updated_right),)

def three_a(sequent):
	used = False
	updated_left_a = []
	updated_left_b = []
	updated_right_a = []
	updated_right_b = []
	left = sequent.left
	right = sequent.right

	for f in right:
		if used:
			updated_right_a.append(f)
			updated_right_b.append(f)
		else:
			if f[0] == 'and':
				updated_right_a.append(f[1])
				updated_right_b.append(f[2])
				used = True
			else:
				updated_right_a.append(f)
				updated_right_b.append(f)
	for f in left:
		updated_left_a.append(f)
		updated_left_b.append(f)

	return used, (Sequent(updated_left_a, updated_right_a), Sequent(updated_left_b, updated_right_b))
	
def three_b(sequent):
	used = False
	updated_left = []
	updated_right = []
	left = sequent.left
	right = sequent.right

	for f in left:
		if used:
			updated_left.append(f)
		else:
			if f[0] == 'and':
				updated_left.append(f[1])
				updated_left.append(f[2])
				used = True
			else:
				updated_left.append(f) 
	updated_right = right

	return used, (Sequent(updated_left, updated_right),)
	
def four_a(sequent):
	used = False
	updated_left = []
	updated_right = []
	left = sequent.left
	right = sequent.right

	for f in right:
		if used:
			updated_right.append(f)
		else:
			if f[0] == 'or':
				updated_right.append(f[1])
				updated_right.append(f[2])
				used = True
			else:
				updated_right.append(f)
	updated_left = left

	return used, (Sequent(updated_left, updated_right),)

def four_b(sequent):
	used = False
	updated_left_a = []
	updated_left_b = []
	updated_right_a = []
	updated_right_b = []
	left = sequent.left
	right = sequent.right

	for f in left:
		if used:
			updated_left_a.append(f)
			updated_left_b.append(f)
		else:
			if f[0] == 'or':
				updated_left_a.append(f[1])
				updated_left_b.append(f[2])
				used = True
			else:
				updated_left_a.append(f)
				updated_left_b.append(f)
	for f in right:
		updated_right_a.append(f)
		updated_right_b.append(f)

	return used, (Sequent(updated_left_a, updated_right_a), Sequent(updated_left_b, updated_right_b))
	
def five_a(sequent):
	used = False
	updated_left = []
	updated_right = []
	left = sequent.left
	right = sequent.right

	for f in right:
		if used:
			updated_right.append(f)
		else:
			if f[0] == 'imp':
				updated_left.append(f[1])
				updated_right.append(f[2])
				used = True
			else:
				updated_right.append(f)
	for f in left:
		updated_left.append(f)

	return used, (Sequent(updated_left, updated_right),)

def five_b(sequent):
	used = False
	updated_left_a = []
	updated_left_b = []
	updated_right_a = []
	updated_right_b = []
	left = sequent.left
	right = sequent.right

	for f in left:
		if used:
			updated_left_a.append(f)
			updated_left_b.append(f)
		else:
			if f[0] == 'imp':
				updated_left_a.append(f[2])
				updated_right_b.append(f[1])
				used = True
			else:
				updated_left_a.append(f)
				updated_left_b.append(f)
	for f in right:
		updated_right_a.append(f)
		updated_right_b.append(f)

	return used, (Sequent(updated_left_a, updated_right_a), Sequent(updated_left_b, updated_right_b))

def six_a(sequent):
	used = False
	updated_left_a = []
	updated_left_b = []
	updated_right_a = []
	updated_right_b = []
	left = sequent.left
	right = sequent.right

	for f in right:
		if used:
			updated_right_a.append(f)
			updated_right_b.append(f)
		else:
			if f[0] == 'iff':
				updated_left_a.append(f[1])
				updated_right_a.append(f[2])
				updated_right_b.append(f[1])
				updated_left_b.append(f[2])
				used = True
			else:
				updated_right_a.append(f)
				updated_right_b.append(f)
	for f in left:
		updated_left_a.append(f)
		updated_left_b.append(f)

	return used, (Sequent(updated_left_a, updated_right_a), Sequent(updated_left_b, updated_right_b))

def six_b(sequent):
	used = False
	updated_left_a = []
	updated_left_b = []
	updated_right_a = []
	updated_right_b = []
	left = sequent.left
	right = sequent.right

	for f in left:
		if used:
			updated_left_a.append(f)
			updated_left_b.append(f)
		else:
			if f[0] == 'iff':
				updated_left_a.append(f[1])
				updated_left_a.append(f[2])
				updated_right_b.append(f[1])
				updated_right_b.append(f[2])
				used = True
			else:
				updated_left_a.append(f)
				updated_left_b.append(f)
	for f in right:
		updated_right_a.append(f)
		updated_right_b.append(f)

	return used, (Sequent(updated_left_a, updated_right_a), Sequent(updated_left_b, updated_right_b))

RULES = [two_a,
		two_b,
		three_a,
		three_b,
		four_a,
		four_b,
		five_a,
		five_b,
		six_a,
		six_b]


