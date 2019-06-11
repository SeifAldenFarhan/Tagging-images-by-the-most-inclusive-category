from collections import defaultdict
from pprint import pprint

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

import tfidf
import getDataES

from getDataES import documents_ids
class Groups:

  # def __init__(self):

  @staticmethod
  def run_tfidf():
    text = tfidf.get_descripion("description")
    text_sents = tfidf.sent_tokenize(text)
    text_sents_clean = [tfidf.remove_string_special_charactors(s) for s in text_sents]
    doc_info = tfidf.get_doc(text_sents_clean)
    freqDict_list = tfidf.create_freq_dict(text_sents_clean)
    TF_scores = tfidf.computeTF(doc_info, freqDict_list)
    IDF_scores = tfidf.computeIDF(doc_info, freqDict_list)
    TFIDF_score = tfidf.computeTFIDF(TF_scores, IDF_scores)
    # pprint(TFIDF_score)
    return TFIDF_score

  def top_score(self, num):
    list_ = self.run_tfidf()
    top_tags = []
    for i, v in enumerate(list_):
      if list_[i]['key'] in top_tags:
        pass
      else:
        top_tags.append(list_[i]['key'])
      top_tags = top_tags[:num]
    return top_tags

  def split_to_groups(self, num):
    size = getDataES.get_num_of_documents('labels')
    documents_ids = getDataES.get_all_documents('labels', 0, size)
    descriptions = getDataES.get_all_descriptions('labels', documents_ids)
    top_tags = self.top_score(num)
    photo_groups = {}

    # pprint(descriptions)
    for i in range(num):
      photo_groups[top_tags[i]] = []
      for j in range(len(documents_ids)):
        for k in range(len(descriptions[j])):
          if top_tags[i] in descriptions[j][k].split(" "):
            #or [[top_tags[i] in descriptions[j][k].split()] for k in range(len(descriptions[j]))]:
            # pprint("-0-0-0-0" + documents_ids[j])
            photo_groups[top_tags[i]].append(documents_ids[j])

    return photo_groups

  def toGroups(self, num):
    text = tfidf.get_descripion("description")
    text_1 = (text.split('.\n'))
    # pprint(text_1)
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(text_1)
    # print(X)
    true_k = num
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)

    # print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    # pprint(order_centroids)
    terms = vectorizer.get_feature_names()
    # pprint(terms)
    # for i in range(true_k):
    #   print("Cluster %d:" % i),
    #   for ind in order_centroids[i, :10]:
    #     print(' %s' % terms[ind]),
    #   print()

    # print("\n")
    # print("Prediction")
    groups_list = defaultdict(list)
    # print(groups_list)
    for i in range(len(text_1)-1):
      Y = vectorizer.transform([text_1[i]])
      prediction = model.predict(Y)
      groups_list[f"{prediction}"].append(documents_ids[i])
      # print(documents_ids[i], prediction)
    # pprint(groups_list)
    return groups_list

# --- MAIN
groups = Groups()
# pprint(groups.run_tfidf())
# pprint(groups.top_score(6))
# pprint(groups.split_to_groups(6))
groups.toGroups(4)
