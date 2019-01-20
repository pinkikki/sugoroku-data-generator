import configparser
from os import environ
from os.path import dirname, join, normpath

from sugoroku.gspread_client import GspreadClient
from sugoroku.sqlite_data_generator import SqliteDataGenerator


def main():
  key_file = environ['sugoroku_data_key_file_path']
  config = configparser.ConfigParser()
  config.read(normpath(join(dirname(__file__), 'settings.ini')))
  book_id = config.get('default', 'book_id')
  sheet_name_prefix = config.get('default', 'sheet_name_prefix')
  start = int(config.get('default', 'start'))
  end = int(config.get('default', 'end'))
  range_ = config.get('default', 'range')
  gen(key_file, book_id, sheet_name_prefix, start, end, range_)


def gen(key_file, book_id, sheet_name_prefix, start, end, range_):
  client = GspreadClient.Builder().key_file(key_file).build()
  client.book(book_id)
  for stage_id in range(start, end):
    sheet_name = f'{sheet_name_prefix}{stage_id}'
    client.sheet(sheet_name)
    SqliteDataGenerator().generate(stage_id, sheet_name, client.values(range_))


if __name__ == '__main__':
  main()
