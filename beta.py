from groups import groups
import getDataES

class beta:
  """
  This Function return all the data from the ElasticSearch to new text file
  by the indices type ['labels', 'landmarks', 'logos', 'web', 'faces', 'text'] !!!
  """
  def getDataFromES(self, type):
    # print("HERE1")
    size = getDataES.get_num_of_documents(type)
    documents_ids = getDataES.get_all_documents(type, 0, size)
    descriptions = getDataES.get_all_descriptions(type, documents_ids)
    getDataES.write_to_file(descriptions)
    # print("HERE2")

  def divideToGroups(self, num):
    return groups.toGroups(num)

b = beta()
lab = "labels"
b.getDataFromES(lab)
b.divideToGroups(3)
