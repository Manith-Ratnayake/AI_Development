import numpy



class Word2vec:

    def __init___(self):
        self.N = 10
        self.X_train = []
        self.Y_train = []
        self.window_size = 2
        self.alpha = 0.001
        self.word = []
        self.word_index = {}

    def 