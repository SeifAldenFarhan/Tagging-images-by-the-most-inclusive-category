from pprint import pprint

import tfidf


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

  # def split_to_groups(self, num):



# --- MAIN
groups = Groups()
# pprint(groups.run_tfidf())
pprint(groups.top_score(3))


