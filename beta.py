from groups import groups
import getDataES

class beta:
  """
  This Function return all the data from the ElasticSearch to new text file
  by the indices type ['labels']
  """
  def getDataFromES(self, type):
    size = getDataES.get_num_of_documents(type)
    documents_ids = getDataES.get_all_documents(type, 0, size)
    descriptions = getDataES.get_all_descriptions(type, documents_ids)
    getDataES.write_to_file(descriptions)

  def divideToGroups(self, num):
    res = groups.toGroups(num)
    return res[0]

  def groupsDiscription(self, num):
    res = groups.toGroups(num)
    return res[1]


b = beta()
