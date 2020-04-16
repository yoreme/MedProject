from scipy.stats import wasserstein_distance

class Embeddings:
    def tryMeOut(self):
        wd1 = wasserstein_distance([0, 1, 3], [5, 6, 8])

        wd2 = wasserstein_distance([0, 1], [0, 1.1])

        wd3 = wasserstein_distance([3.4, 3.9, 7.5, 7.8], [4.5, 1.4], [1.4, 0.9, 3.1, 7.2], [3.2, 3.5])

        print(wd1)
        print(wd2)
        print(wd3)

embeddings = Embeddings()
embeddings.tryMeOut()