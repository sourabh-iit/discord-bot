

def write_to_file(filename, data):
  """Appends data to file. If file doesn't exist, then creates it"""
  file_handler = open(filename, 'a+')
  file_handler.write(data+'\n')
  file_handler.close()

def get_filename(author):
  """Utility function to get file name"""
  return f"{author.id}.txt"


def search_file(filename, query):
  """Searches file for queries which contains the given query"""
  results = []
  file_handler = open(filename, 'r')
  for res in file_handler.readlines():
    if query in res:
      results.append(res[:-1])
  file_handler.close()
  return results