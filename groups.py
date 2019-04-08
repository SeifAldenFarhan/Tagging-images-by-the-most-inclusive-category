from pprint import pprint

import tfidf
import getDataES


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


# --- MAIN
groups = Groups()
# pprint(groups.run_tfidf())
pprint(groups.top_score(6))
pprint(groups.split_to_groups(6))

