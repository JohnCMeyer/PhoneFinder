import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Container, List, Optional, Union


class InsertStatements:
	pass


def _list_params(*values):
	return ', '.join(values)


def _list_values(*values):
	return ', '.join(repr(value) for value in values)


def _insert_stmt(table_name, params, values):
	return f"INSERT INTO {table_name}({_list_params(params)}) VALUES({_list_values(values)});"


def _insert_stmt_2(table_name, params, values):
	return f"INSERT INTO {table_name}({params}) VALUES{repr(values)};"


def add_funcs():
	with open('InsertTestData.sql', 'rt') as f:
		lines = f.readlines()
	for line in lines:
		if line.startswith('INSERT'):
			parts = line.split(maxsplit=2)[2].split('(', 1)
			table_name = parts[0]
			params = parts[1].split(')', 1)[0]
			setattr(InsertStatements, f"insert_{table_name}", lambda values, name=table_name, par=params: _insert_stmt_2(name, par, values))


def rand_color():
	return random.choice(('Black', 'Grey', 'Red', 'Blue', 'Green'))


def rand_case():
	return rand_color()


def rand_screen_protector():
	return random.choice(('Glass', 'Plastic'))


def rand_aspect_ratio():
	return random.choice(('1.5:1', '2:1', '3:1'))


def rand_price():
	return random.randint(299, 499) + 0.99


def rand_battery_life():
	return f"{random.randint(100, 300)} hours"


def rand_ram():
	return f"{random.choice(('256', '512'))} MB"


_STORE_NAMES = ('T-Mobile', 'AT&T', 'Verizon')


def rand_availability():
	return [random.choice(_STORE_NAMES) for _ in range(random.randint(1, 4))]


@dataclass
class Store:
	id: int
	name: str
	address: str
	city: str
	state: str


_DIRECTIONS = ('N', 'S', 'E', 'W')
_STREETS = ('University Dr', 'College Ave', 'Mill Ave', 'Rural Rd', 'Broadway Rd', 'Main St', 'Apache Blvd', 'McClintock Dr', 'Rio Salado Pkwy', 'Southern Ave')


class RandStore:
	def __init__(self):
		self.stores = []
		self.last_id = 10000

	def rand_store(self, name):
		self.last_id += 1
		store = Store(self.last_id, name, self._rand_address(), 'Tempe', 'AZ')
		self.stores.append(store)
		return store

	def _rand_address(self):
		return f"{random.randint(100, 9999)} {random.choice(_DIRECTIONS)} {random.choice(_STREETS)}"


_RAND_STORE = RandStore()


def _max_words(s: str, n: int):
	return ' '.join(s.split(maxsplit=n)[:n])


def _stop_before_word(s: str, stop_words: Union[str, Container[str]]):
	if isinstance(stop_words, str):
		stop_words = [stop_words]
	out = []
	for word in s.split():
		if word in stop_words:
			break
		out.append(word)
	return ' '.join(out)


_UNIT_ABREV = {
	('pico',):								'p',
	('nano',):								'n',
	('micro',):								'µ',
	('milli',):								'm',
	('centi',):								'c',
	('deci',):								'd',
	('deca',):								'da',
	('hecto',):								'h',
	('kilo',):								'k',
	('mega',):								'M',
	('giga',):								'G',
	('tera',):								'T',
	('bits', 'bit'):						'b',
	('bytes', 'byte'):						'B',
	('pixels', 'pixel'):					'P',
	('grams', 'gram'):						'g',
	('meters', 'meter'):					'm',
	('seconds', 'second'):					's',
	('minutes', 'minute'):					'm',
	('hours', 'hour'):						'h',
	('days', 'day'):						'd',
	('months', 'month'):					'm',
	('weeks', 'week'):						'w',
	('years', 'year'):						'y',
	('dots per inch', 'dots-per-inch'):		'DPI',
}


def _save_capitals(s: str):
	caps = {}
	out = ''
	for i, c in enumerate(s):
		if c.isupper():
			try:
				out += caps[c]
			except KeyError:
				while True:
					replacement = str(random.randint(10000000, 99999999))
					if replacement not in caps.values():
						break
				caps[c] = replacement
				out += replacement
		else:
			out += c
	return out, caps


def _restore_capitals(s: str, caps: dict):
	for c, replacement in caps.items():
		s = s.replace(replacement, c)
	return s


def _fix_value(value: str):
	s, caps = _save_capitals(value)
	for values, replacement in _UNIT_ABREV.items():
		for value in values:
			s = s.replace(value, replacement)
	return _restore_capitals(s, caps)


def _alpha_num_space(s: str):
	return ''.join(c for c in s if c.isalnum() or c.isspace())


def _fix_phone_name(name: str):
	return _stop_before_word(_alpha_num_space(name), ('a', 'by')).title()


def _fix_dimensions(dimensions):
	# _max_words(d, 2) would add units, but it wouldn't fit in the table cell
	return 'x'.join(_max_words(d, 1).replace(' ', '') for d in dimensions)


def _fix_availability(store_names: List[str]):
	return [name.strip().strip(',').strip().replace('amp;', '') for name in store_names]


def _fix_cpu(cpu: str):
	return _fix_value(_stop_before_word(_max_words(cpu, 3), 'processor'))


_LAST_MODEL_NUMBER = 1000


# parses phones from https://github.com/IgorMinar/angular-phonecat-tutorial/tree/master/app/phones
def parse_json_igor(d: dict, phone_names_out: Optional[List[str]] = None):
	global _LAST_MODEL_NUMBER
	_LAST_MODEL_NUMBER += 1
	model_number = _LAST_MODEL_NUMBER
	name = _fix_phone_name(d['name'])
	if phone_names_out is not None:
		phone_names_out.append(name)
	manufacturer = _max_words(name, 1)
	display: dict = d['display']
	screen: list = display['screenResolution'].split(maxsplit=1)
	screen_type: str = screen[0]
	screen_res: str = screen[1].lstrip('(').rstrip(')')
	hw: dict = d['hardware']
	size_weight: dict = d['sizeAndWeight']
	battery: dict = d['battery']
	dimensions = _fix_dimensions(size_weight['dimensions'])
	storage: dict = d['storage']
	availability: list = d['availability']
	if not availability:
		availability = rand_availability()
	availability = _fix_availability(availability)
	cpu = _fix_cpu(hw['cpu'])
	weight = _fix_value(size_weight['weight'])
	battery_life = battery['standbyTime']
	if not battery_life:
		battery_life = rand_battery_life()
	battery_life_fixed = _fix_value(battery_life)
	ram = storage['ram']
	if not ram:
		ram = rand_ram()
	ram_fixed = _fix_value(ram)
	statements = [
		InsertStatements.insert_PhoneModel((model_number, manufacturer, name)),
		InsertStatements.insert_Accessories((model_number, rand_case(), rand_screen_protector())),
		InsertStatements.insert_ScreenType((model_number, screen_type, screen_res, rand_aspect_ratio())),
		InsertStatements.insert_Specs((model_number, cpu, rand_color(), weight, battery_life_fixed, dimensions, ram_fixed)),
	]
	for store_name in availability:
		for _ in range(random.randint(1, 3)):
			store = _RAND_STORE.rand_store(store_name)
			statements.append(InsertStatements.insert_Store((store.id, store.name, store.address, store.city, store.state, rand_price())))
			statements.append(InsertStatements.insert_SoldAt((model_number, store.id)))
	return statements


def parse_files(path, phone_names_out: Optional[List[str]] = None):
	p = Path(path)
	statements = []
	if p.is_dir():
		for child in p.iterdir():
			statements.extend(parse_files(child, phone_names_out))
	elif p.suffix == '.json' and p.stem != 'phones':
		with p.open() as f:
			statements.extend(parse_json_igor(json.load(f), phone_names_out))
	return statements
