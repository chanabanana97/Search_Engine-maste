from ranker import Ranker
import utils

class Searcher:

    def __init__(self, inverted_index):
        """
        :param inverted_index: dictionary of inverted index
        """
        self.ranker = Ranker()
        self.inverted_index = inverted_index
        self.letters_files = {}
        self.query_terms_count = {}
        self.max_term_in_query = 0
        self.SIZE = 4000

        self.documents = {}
        self.total_num_of_docs = 0
        for i in range(10):
            self.documents[i] = utils.load_obj("document" + str(i))
            self.total_num_of_docs += len(self.documents[i])


    def relevant_docs_from_posting(self, query: list):
        """
        This function loads the posting list and count the amount of relevant documents per term.
        :param query: query as list tokenized from our parser
        :return: dictionary of relevant documents.
        """
        letters_in_query_set = set()

        for term in query:
            if term in self.inverted_index: # check if term is in inverted index - if not, we dont need to add to set (which will ultimately load posting)
                letters_in_query_set.add(term[0].lower())
                if term not in self.query_terms_count:
                    self.query_terms_count[term] = 1
                else:
                    self.query_terms_count[term] += 1

        self.max_term_in_query = max(len(self.query_terms_count), max(self.query_terms_count.values()))



        for letter in letters_in_query_set:
            if letter.isdigit():
                self.letters_files['1'] = utils.load_obj("C:\\Users\Chana\Documents\SearchEngine\Search_Engine-master\output_files\WithoutStem\\" + "1")
            else:
                self.letters_files[letter] =utils.load_obj("C:\\Users\Chana\Documents\SearchEngine\Search_Engine-master\output_files\WithoutStem\\" + letter) # TODO fix - get self.out....

        relevant_docs = {}
        for term in query:
            try:
                posting_dict = self.letters_files[term[0].lower()]
                if term in posting_dict:
                    posting_doc = posting_dict[term]
                    for doc_tuple in posting_doc[:-1]:
                        doc = doc_tuple[0]
                        if doc not in relevant_docs:
                            relevant_docs[doc] = 1
                        else:
                            relevant_docs[doc] += 1
            except:
                print('term {} not found in posting'.format(term))

        doc_weights = {}
        # for doc in relevant_docs:
        #     doc_weights[doc] = self.cos_sim(query, doc)

        relevant_docs_return = sorted(relevant_docs.items(), key=lambda x: x[1], reverse=True)
        # length = min(len(relevant_docs_return), self.SIZE)

        return relevant_docs_return[:4000], self.documents


    # def cos_sim(self, query, relevant_doc_id):
    #
    #     count_word_in_doc = 0
    #     mone = 0
    #     count_word_in_query = 0
    #     max_tf = 0
    #     tf = 0
    #     idf = 0
    #     tf_idf_pow = 0
    #     modulo = int(relevant_doc_id) % 10
    #     for word in query:
    #         if word in self.documents[modulo][relevant_doc_id][0]: # term_doc_dictionary -> word: num of times word is in doc
    #             count_word_in_doc = self.documents[modulo][relevant_doc_id][0][word]
    #             max_tf = self.documents[modulo][relevant_doc_id][1]
    #             posting_dict = self.letters_files[word[0].lower()]
    #             num_docs_with_word = posting_dict[word.lower()][-1]
    #
    #             tf = count_word_in_doc/max_tf
    #             idf = math.log(self.total_num_of_docs/num_docs_with_word, 2)
    #
    #             mone += tf*idf
    #             tf_idf_pow += math.pow(tf*idf, 2)
    #
    #     mechane = math.sqrt(tf_idf_pow)
    #
    #     return mone/mechane



        # count_word_in_doc = 0
        # mone = 0
        # wij_pow = 0
        # wiq_pow = 0
        #
        # max_tf = self.documents[relevant_doc].max_tf
        # len_docs = len(self.documents)
        # for word in query:
        #     if word in self.documents[relevant_doc].term_doc_dictionary:
        #         count_word_in_doc += self.documents[relevant_doc].term_doc_dictionary[word]
        #     else:
        #         continue
        #     w1 = count_word_in_doc / max_tf
        #     posting_dict = self.letters_files[word[0].lower()]
        #     count_doc_for_word = posting_dict[word.lower()][-1]
        #
        #     w2 = math.log((len_docs/count_doc_for_word), 2)
        #     w3 = self.query_terms_count[word]/self.max_term_in_query # *1 query
        #
        #
        #     mone += w1 * w2 * w3
        #     wij_pow += math.pow(w1*w2, 2)
        #     wiq_pow += math.pow(w3, 2)
        #
        # mechane = math.sqrt(wij_pow*wiq_pow)
        # # if mechane == 0:
        # #     print(w1)
        # #     print(w2)
        # #     print(w3)
        #
        #
        # return mone/mechane




