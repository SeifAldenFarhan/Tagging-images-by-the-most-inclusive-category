from pprint import pprint

import tfidf

text = tfidf.get_descripion("description")
text_sents = tfidf.sent_tokenize(text)
text_sents_clean = [tfidf.remove_string_special_charactors(s) for s in text_sents]
doc_info = tfidf.get_doc(text_sents_clean)
freqDict_list = tfidf.create_freq_dict(text_sents_clean)
TF_scores = tfidf.computeTF(doc_info, freqDict_list)
IDF_scores = tfidf.computeIDF(doc_info, freqDict_list)
TFIDF_score = tfidf.computeTFIDF(TF_scores, IDF_scores)
pprint(TFIDF_score)


