import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GspreadClient(object):

  def __init__(self, client):
    self._delegate = client
    self._wkb = None
    self._wks = None

  def open(self, book_name):
    self._wkb = self.delegate.open(book_name)

  def sheet(self, sheet_name):
    # TODO 一旦sheet1を返却
    self._wks = self._wkb.sheet1

  def update_cell(self, cell, text):
    self._wks.update_acell(cell, text)

  def find_cell(self, cell):
    return self._wks.acell(cell)

  @property
  def delegate(self):
    return self._delegate


  class Builder(object):

    def __init__(self):
      self._key_file = None
      self._scope = ['https://spreadsheets.google.com/feeds',
                    'https://www.googleapis.com/auth/drive']

    def key_file(self, key_file):
      self._key_file = key_file
      return self

    def scope(self, scope):
      self._scope = scope

    def build(self):
      credentials = ServiceAccountCredentials.from_json_keyfile_name(self._key_file, self._scope)
      client = gspread.authorize(credentials)
      return GspreadClient(client)
