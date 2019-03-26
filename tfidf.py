import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import math
from pprint import pprint

# text = ""
# with open("description", "r") as f:
#   for line in f.readlines():
#     text += line
#     # text += '.'


def get_descripion(file_name):
  text = ""
  with open(file_name, "r") as f:
    for line in f.readlines():
      text += line
      # text += '.'
  return text


# -------------------------------------
def remove_string_special_charactors(s):
  """
  This function removes special characors from within a string
  :parameter :
    s(str): single input string.

  :return:
    stripped(str): A string with special characters removed
  """
  stripped = re.sub('[^\w\s]', '', s)
  stripped = re.sub('_', '', stripped)
  stripped = re.sub('\s+', ' ', stripped)
  stripped = stripped.strip()

  return stripped


# -------------------------------------
def get_doc(text):
  """
  This function splits the text into sentence and
  considering each sentence as a document, calculates the
  total word count of each.
  """
  doc_info = []
  i = 0
  for sent in text:
    i += 1
    count = count_words(sent)
    temp = {'doc_id': i, 'doc_length': count}
    doc_info.append(temp)
  return doc_info


# -------------------------------------
def count_words(sent):
  """
  This function returs the total
  number of words in the input text.
  """
  count = 0
  words = word_tokenize(sent)
  for word in words:
    count += 1
  return count


# -------------------------------------
def create_freq_dict(sents):
  """
  This function creates a frequency dictionary
  fir each word in each document.
  """
  i = 0
  freqDict_list = []
  for sent in sents:
    i += 1
    freq_dict = {}
    words = word_tokenize(sent)
    # pprint(words)
    for word in words:
      word = word.lower()
      if word in freq_dict:
        freq_dict[word] += 1
      else:
        freq_dict[word] = 1
      temp = {'doc_id': i, 'freq_dict': freq_dict}
    freqDict_list.append(temp)
  return freqDict_list


# -------------------------------------
def computeTF(doc_info, freqDict_list):
  """
  tf = (frequency of the term in the doc/total number of term im the doc)
  """
  TF_scores = []
  for tempDict in freqDict_list:
    id = tempDict['doc_id']
    for k in tempDict['freq_dict']:
      temp = {'doc_id': id,
              'TF_score': tempDict['freq_dict'][k]/doc_info[id-1]['doc_length'],
              'key': k}
      TF_scores.append(temp)
  return TF_scores


# -------------------------------------
def computeIDF(doc_info, freqDict_list):
  """
  idf = ln(total number of docs/number of docs with term in it)
  """
  IDF_scores = []
  counter = 0
  for dict in freqDict_list:
    counter += 1
    for k in dict['freq_dict'].keys():
      count = sum([k in tempDict['freq_dict'] for tempDict in freqDict_list])
      temp = {'doc_id': counter, 'IDF_score': math.log(len(doc_info)/count), 'key': k}
      IDF_scores.append(temp)
  return IDF_scores


# -------------------------------------
def computeTFIDF(TF_scores, IDF_scores):
  TFIDF_scores = []
  for j in IDF_scores:
    for i in TF_scores:
      if j['key'] == i['key'] and j['doc_id'] == i['doc_id']:
        temp = {'doc_id': j['doc_id'],
                'TFIDF_score': (j['IDF_score'] * i['TF_score']),
                'key': i['key']}
    # pprint(temp)
    TFIDF_scores.append(temp)
  TFIDF_scores = sorted(TFIDF_scores, key=lambda score: score['TFIDF_score'], reverse=False)
  return TFIDF_scores


# -------------------------------------
# MAIN
# text = get_descripion("description")
# text_sents = sent_tokenize(text)
# text_sents_clean = [remove_string_special_charactors(s) for s in text_sents]
# doc_info = get_doc(text_sents_clean)
# # pprint(doc_info)
#
# freqDict_list = create_freq_dict(text_sents_clean)
# # pprint(freqDict_list)
#
# TF_scores = computeTF(doc_info, freqDict_list)
# IDF_scores = computeIDF(doc_info, freqDict_list)
# TFIDF_score = computeTFIDF(TF_scores, IDF_scores)

# pprint(TF_scores)
# pprint(IDF_scores)
# pprint(TFIDF_score)
# pprint(remove_string_special_charactors(text))
