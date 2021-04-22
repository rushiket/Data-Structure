from Stack import Stack

def is_match(top,paren):
	p1 = top
	p2 = paren
	if p1 == "(" and p2 == ")":
		return True
	elif p1 == "{" and p2 == "}":
		return True
	elif p1 == "[" and p2 == "]":
		return True
	else:
		return False

def is_paren_balanced(paren_string):
	s = Stack()
	is_balanced = True
	index = 0

	while index < len(paren_string) and is_balanced:
		paren = paren_string[index]
		if paren in "({[":
			s.push(paren)
		else:
			if s._isempty():
				is_balanced = False
			else:
				top = s.pop()
				if not is_match(top,paren):
					is_balanced = False
		index += 1
	


	if s._isempty() and is_balanced :
		return True
	else:
		return False

print(is_paren_balanced("{(([{}]))"))
print(is_paren_balanced("{(([{}))"))
print(is_paren_balanced("(([{}]))"))