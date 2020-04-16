import codecs
import numpy as np
import logging

logger = logging.getLogger(__name__)

class Embeddings:
    model = None

    def load_embeddings(self, file_path):
        """
        :param file_path: path of embeddings file.
        """

        f = open(file_path, 'r', encoding='utf-8').readlines()
        model = {}
        for line in f[1:]:
            split_line = line.split()
            word = split_line[0]
            embedding = np.array([float(val) for val in split_line[1:]])
            model[word] = embedding
        self.model = model
        print(len(self.model))

    def get_w2v(self, sentence):
        """
        :param sentence: inputs a single sentences whose word embedding is to be extracted.
        :return: returns numpy array containing word embedding of all words in input sentence.
        """
        logger.warn(sentence)

        return np.array([self.model.get(val, np.zeros(300)) for val in sentence.split()], dtype=np.float64)

    def get_w2v_sum(self, sentence):
        """
        :param sentence: inputs a single sentences whose word embedding is to be extracted.
        :return: returns numpy array containing the sum of the word embedding of all words in input sentence.
        """
        items = self.get_w2v(sentence)
        
        ack = [0] * 300
        for item in items:
            ack = np.add(ack, item)
        return ack 

# embeddings = Embeddings()
# embeddings.load_embeddings("c:\dev\swectors-300dim.txt")
# mw = embeddings.get_w2v_sum("presidenten talade till folket")
# kd = embeddings.get_w2v_sum("i norge äter de mackor till lunch")

# print(wasserstein_distance(mw, kd))
