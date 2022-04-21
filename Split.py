def split_sql(queries: str):
	return advanced_split(queries, delimiters=';', include_delimiters=True, include_quotes=True, include_escapes=True)


def advanced_split(s: str, delimiters, include_delimiters=False, quotes='\'\"', include_quotes=False, escapes='\\', include_escapes=False, escape_inside_quotes=True, strip_parts=True, allow_empty_parts=False):
	parts = []
	part = ''
	def add_part():
		nonlocal part
		if include_delimiters:
			part += c
		if strip_parts:
			part = part.strip()
		if allow_empty_parts or part:
			parts.append(part)
			part = ''
	quoting = None
	escaping = False
	for c in s:
		if escaping:  # escaping
			part += c
			escaping = False
		elif quoting is None:  # not quoting
			if c in delimiters:  # c is delimiter
				add_part()
			elif c in quotes:  # c is quote
				quoting = c
				if include_quotes:
					part += c
			elif c in escapes:  # c is escape
				escaping = True
				if include_escapes:
					part += c
			else:  # c is regular non-quoted char
				part += c
		elif c == quoting:  # c is the quote
			quoting = None
			if include_quotes:
				part += c
		elif escape_inside_quotes and c in escapes:  # c is escape (inside quote)
			escaping = True
			if include_escapes:
				part += c
		else:  # c is regular quoted char
			part += c
	add_part()
	return parts
