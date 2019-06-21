import json
# import logging
import os
from pprint import pprint

from elasticsearch import Elasticsearch


# The possible indices in storage:
indices = ['labels', 'landmarks', 'logos', 'web', 'faces', 'text']

# Disable all non-ERROR level messages.
# This allows to check the connection without logging traceback.
# logging.basicConfig(level=logging.ERROR)

es = Elasticsearch()  # Represents the elasticsearch client.


# ---------------------

def get_data(index, image_id):
  '''This function gets an image id and index,
     and prints the data of the image in the index.'''

  if not es.indices.exists(index=index):
    print('\nThere is no', index, 'index.\n')
    return False

  if image_id == '':
    return False

  data = es.get(index=index, doc_type='doc', id=image_id, ignore=404)
  if data['found'] is False:
    print('\nThere is no data in', index, 'index for the given image.\n')
    return False
  else:
    print(json.dumps((data), indent=4))
    return json.dumps((data), indent=4)


# -----------------------

def get_images_by_words(words, start=0):
  '''This function gets words, and prints all images that contain
     data with the words, at least in one index.'''

  query = {
    'query': {
      'bool': {
        'should': [
          {'match_phrase': {'labelAnnotations.description': {"query": words, "slop": 100}}},
          {'match': {'landmarkAnnotations.description': words}},
          {'match': {'logoAnnotations.description': words}},
          {'match': {'textAnnotations.description': words}},
          {'match': {'webDetection.webEntities.description': words}}
        ]
      }
    }  # , fuzzy
    # 'stored_fields' : ['Image path']
  }

  files = []

  res = es.search(index='*', doc_type='doc', body=query, _source=['Image path'], from_=start, size=1, ignore=404)
  print(res)

  if int(res['hits']['total']) == 0:
    print('\nThere are no images with the word/s \'', words, '\'.')

  else:
    print('\nAll images with the word/s \'', words, '\' :')
    for i in res['hits']['hits']:
      print(i['_id'])
      files.append(i['_source']['Image path'] + '/' + i['_id'])

  # Return path of all files, and number of total files that were found.
  return [files, res['hits']['total']]


# --------------------------

def get_num_of_documents(index):
  """This function prints the munber of images in a specific index."""

  if not es.indices.exists(index=index):
    print('\nThere is no', index, 'index.\n')
    return

  num = es.count(index=index, doc_type='doc')
  num = num['count']

  # print('\nNumber of images in', index, 'index:', num, '.\n')
  return num

# --------------------------

def get_all_documents(index, start=0, size=2):
  '''This function prints a list of all images in a specific index.'''

  if not es.indices.exists(index=index):
    print('\nThere is no', index, 'index.\n')
    return None

  image_ids = []
  description_list = []

  query = {'query': {'match_all': {}}, 'stored_fields': []}

  res = es.search(index=index, doc_type='doc', body=query, from_=start, size=size)
  # res1 = es.get_source(index=index, doc_type='doc', id='download.jpg')
  # print(res1['labelAnnotations']['description'])

  if int(res['hits']['total']) == 0:
    print('\nThere are no images in', index, 'index.\n')

  else:
    # print('\nAll images in', index, 'index:')
    for i in res['hits']['hits']:
      # print(i['_id'])
      # print(i['_source'])
      # print(i['_score'])
      image_ids.append(i['_id'])

      # ---- get the description for each image
      # res1 = es.get_source(index=index, doc_type='doc', id=i['_id'])
      # print([i['description'] for i in res1['labelAnnotations']])
      # description_list.append([i['description'] for i in res1['labelAnnotations']])

  # pprint(description_list)
  return image_ids


# ----------------------

def get_all_descriptions(index, image_ids):
  description_list = []

  for id in image_ids:
    res1 = es.get_source(index=index, doc_type='doc', id=id)
    # print([i['description'] for i in res1['labelAnnotations']])
    description_list.append([i['description'].lower() for i in res1['labelAnnotations']])

  return description_list


def write_to_file(descriptionList):
  with open("description", "w") as f:
    for item in descriptionList:
      for i in item:
        f.write("%s, " % i)
      f.write(".\n")


# ---------------
# ------- MAIN
# ---------------
# if not os.path.isfile('./description'):
size = get_num_of_documents('labels')
documents_ids = get_all_documents('labels', 0, size)
# pprint(documents_ids)
# print()
# print("----------------")
# print()
descriptions = get_all_descriptions('labels', documents_ids)
# pprint(descriptions)
write_to_file(descriptions)
