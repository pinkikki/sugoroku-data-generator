from sugoroku.gspread_client import GspreadClient


def main():
  client = GspreadClient.Builder().key_file('[json-file]').build()
  client.open('bunbou-sugoroku-data')
  client.sheet('Stage1')
  text = client.find_cell('A1')
  print(text)


if __name__ == '__main__':
    main()
