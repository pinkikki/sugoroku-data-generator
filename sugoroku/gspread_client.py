from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


class GspreadClient():

  def __init__(self, client):
    self._delegate = client
    self._wkb_id = None
    self._wks_id = None

  def book(self, book_id):
    self._wkb_id = book_id

  def sheet(self, sheet_id):
    self._wks_id = sheet_id

  def values(self, range_):
    result = self._delegate.values().get(spreadsheetId=self._wkb_id, range=f'{self._wks_id}!{range_}').execute()
    return result.get('values', [])

  @property
  def delegate(self):
    return self._delegate

  class Builder():

    def __init__(self):
      self._key_file = None
      self._scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    def key_file(self, key_file):
      self._key_file = key_file
      return self

    def scopes(self, scopes):
      self._scopes = scopes

    def build(self):
      credentials = ServiceAccountCredentials.from_json_keyfile_name(self._key_file, self._scopes)
      service = build('sheets', 'v4', credentials=credentials)
      return GspreadClient(service.spreadsheets())
