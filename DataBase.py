#!/bin/python
from itertools import repeat
from os import environ
from pathlib import Path
from subprocess import DEVNULL, run, STDOUT
from typing import AnyStr, Dict, Generator, Iterable, List, Optional, Union

from psycopg2 import connect
from psycopg2._psycopg import connection, cursor

from Split import split_sql


class DataBase:
	host: str
	port: int
	db_home: str
	db_name: str
	con: connection
	cur: cursor
	_env: Dict[AnyStr, AnyStr]
	_running: bool

	def __init__(self, host: str, port: int, db_name: str, db_home=None):
		self.host = host
		self.port = port
		self.db_name = db_name
		self.db_home = db_home if db_home is not None else str(Path.cwd() / db_name)
		self._running = False
		self._env = environ.copy()
		self._env.update({
			'PGHOST': self.host,
			'PGPORT': str(self.port)
		})

	def start(self, capture_output=False, timeout: Optional[float] = None):
		if not self._running:
			self._run_all((self._init_db_cmd(), self._start_server_cmd(), self._create_db_cmd()), capture_output, timeout)
			self.con = connect(host=self.host, port=self.port, database=self.db_name)
			self.cur = self.con.cursor()
			self._running = True

	def stop(self, capture_output=False, timeout: Optional[float] = None):
		if self._running:
			self._run(self._stop_sever_cmd(), capture_output, timeout)
			self._running = False

	def exec(self, query: str):
		# Executes the query, returning the results.
		self.cur.execute(query)
		return self._get_output()

	def exec_single_value(self, query: str):
		# Executes the query, returning a single value, or None if no result was found.
		try:
			return next(self.exec(query))[0]
		except:
			return None

	def exec_single_row(self, num_values: int, query: str):
		# Executes the query, returning a single row, or None if no result was found.
		# This is designed for conveniently unpacking the row into a variable per value.
		try:
			row = next(self.exec(query))
			if len(row) == num_values:
				return row
		except:
			pass
		return repeat(None, num_values)

	def exec_multi(self, queries: Union[str, Iterable[str]]):
		# Executes multiple queries (if a str is given, smartly splits by ';'), returning the results.
		if isinstance(queries, str):
			queries = split_sql(queries)
		return [self.exec(query) for query in queries]

	def exec_file(self, file):
		# Executes the queries in the file, returning the results.
		with open(file, 'rt') as f:
			queries = f.read()
		return self.exec_multi(queries)

	def _get_output(self):
		try:
			for record in self.cur:
				yield record
		except:
			pass

	def _run(self, cmd, capture_output=False, timeout: Optional[float] = None):
		run(cmd, stdout=None if capture_output else DEVNULL, stderr=STDOUT, env=self._env, timeout=timeout)

	def _run_all(self, cmds, capture_output=False, timeout: Optional[float] = None):
		for cmd in cmds:
			self._run(cmd, capture_output, timeout)

	def _init_db_cmd(self):
		return 'initdb', self.db_home

	def _start_server_cmd(self):
		return 'pg_ctl', '-D', self.db_home, '-o', '-k ' + self.host, 'start'

	def _create_db_cmd(self):
		return 'createdb', self.db_name

	def _stop_sever_cmd(self):
		return 'pg_ctl', '-D', self.db_home, 'stop'


def _de_gen(output):
	for o in output:
		if isinstance(o, Generator):
			_de_gen(o)
		else:
			yield o


def print_out(output):
	for o in _de_gen(output):
		print(o)


def main():
	db = DataBase(host='/tmp', port=8888, db_name='PhoneFinderDB')
	print('Starting DataBase...')
	# db.start(capture_output=True)
	db.start()
	print('\nCreating Tables...')
	print_out(db.exec_file('CreateTables.sql'))
	print('\nInserting Test Data...')
	print_out(db.exec_file('InsertTestData.sql'))
	print('\nData in PhoneFinder:')
	print_out(db.exec('select * from PhoneFinder;'))
	print('\nData in PhoneModel:')
	print_out(db.exec('select * from PhoneModel;'))
	print('\nStopping DataBase...')
	# db.stop(capture_output=True)
	db.stop()


if __name__ == '__main__':
	main()
