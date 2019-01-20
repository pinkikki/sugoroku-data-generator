from os.path import join, normpath

from jinja2 import Environment, FileSystemLoader


class SqliteDataGenerator():

  def __init__(self, template_name='insert.template', template_dir='../templates/', encoding='utf8'):
    self.env = Environment(loader=FileSystemLoader(normpath(template_dir), encoding))
    self.template = self.env.get_template(template_name)

  def generate(self, stage_id, stage_name, values):
    with open(self._generate_file_name('all_data.sql'), 'a') as f_all:
      with open(self._generate_file_name(f'{stage_name}.sql'), 'w') as f_stage:
        count = 0
        for i, row in enumerate(values):
          row_index = i + 1
          for j, value in enumerate(row):
            column_index = j + 1
            if value:
              count += 1
              record = self.template.render({'stage_id': stage_id, 'no': count, 'row': row_index, 'column': column_index, 'type': value})
              f_all.write(f'{record}\n')
              f_stage.write(f'{record}\n')
              print(record)

  def _generate_file_name(self, file_name):
    return normpath(join('../output', file_name))
