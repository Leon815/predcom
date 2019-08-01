print(__doc__)

from sklearn.cluster import AffinityPropagation
import numpy as np
import math
from scipy import sparse
from sklearn.metrics.pairwise import euclidean_distances

value = None

def getNumberFromDiference(S1, S2):
    difference = list(S1.symmetric_difference(S2))
    result = (len(S1)+len(S2))-len(difference)

    return result

def categoricalDist(line1, line2):

    value = 0.0
    for index in range(0, len(line1)-1):
        #is categorical
        if isinstance( line1[index], int ) and isinstance( line2[index], int ):
            if (line1[index] == line2[index]):
                value += 0.0
            else:
                value += 1.0
        else:
            value += (line1[index]-line2[index])**2

    result = math.sqrt(value)

    return result

def getLineFromList(list, indexLine):

    cont = 0
    for line in list:

        if cont == indexLine:
            return line
            break
        cont+=1

    return "erro"

def distanceForText(textVet):

    from sklearn.feature_extraction import text
    from sklearn.feature_extraction.text import TfidfVectorizer

    stopwords = text.ENGLISH_STOP_WORDS.union(
        ['10', '11', '2001', 'amto', 'cc', 'know', 'just', 'like', 'friday', 'monday', 'fw', 'week', 'make', 'day',
         'don', 'today', 'use', 'questions', 'october', 'november', 'work', '08', '15', '26', 'time', '2002', 'gas',
         'contract', 'meeting', 'said', 'ees', 'EES', 'NA',
         'tuesday', 'wednesday', 'ect', 'com', 'new', 'let', 'need', 'hou', 'pm', 'pmto', 'mark', 'sent', 'subject',
         'thanks', 'message', 'want', 'thursday', 'think', '0003', '66', '199', '42', '688', '57', 'ga', 'corp',
         'agreement',
         'original', '00', '01', '02', '03', '04', '05', '09', '12', '20', '2000', '30', '646', '713', '853',
         'attached', 'going', 'll', 'mail', 'forward', 'forwarded', 'will', 'enron', 'energy', 'california', 'power',
         'EE', 'ET', 'ee', 'et'])

 #   tfidf_vectorizer = TfidfVectorizer(max_df=0.9, max_features=200000,
 #                                      min_df=0.1, analyzer='word', stop_words=stopwords,
 #                                      use_idf=True)

  #  corpus = []
  #  for texts in textVet:
  #      corpus.append(texts[0])

   # tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
   # print tfidf_matrix
   # return tfidf_matrix

    #isso eh para arXvi
    #years = []
    corpus = []
    correspondencia = {}
    i = 0
    j = 0
    for texts in textVet:
        palavras = texts[0].split(';')
        corpus += palavras
        for palavra in palavras:
            correspondencia[j] = i
            j += 1
        i += 1
        #years.append(texts[1])
    tfidf_vectorizer = TfidfVectorizer(max_df=0.9, max_features=200000,
                                   min_df=0.01, analyzer='word', stop_words=stopwords,
                                   use_idf=True)
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    print tfidf_matrix
    print ("esse e o corpus",corpus)

    preX = tfidf_matrix.todense()
    dist = euclidean_distances(tfidf_matrix, tfidf_matrix)
    min = np.min(np.min(dist, axis=1), axis=0)
    max = np.max(np.max(dist, axis=1), axis=0)
    global value
    value = min - (max - min)
    print "o valor e", value
    import gc
    del tfidf_matrix, tfidf_vectorizer
    gc.collect()
    #x = np.hstack((preX, np.atleast_2d(years).T))

    mat = euclidean_distances(preX, preX) #INCLUSAO_CAMILA
    #print mat
    return correspondencia, mat

def makeCategoricalX(X_temp, isHomogeneousNetwork):

    if isHomogeneousNetwork:
        return distanceForText(X_temp)

    squareMatriz = np.zeros(shape=(len(X_temp),len(X_temp)))
    contLine = 0
    contCol = 0

    for line in squareMatriz:

        X_line1 = getLineFromList(X_temp, contLine)

        for col in line:

            if contCol == contLine:
                squareMatriz[contLine, contCol] = 0.0
            else:
                X_line2 = getLineFromList(X_temp, contCol)
                squareMatriz[contLine, contCol] = categoricalDist(X_line1, X_line2)

            contCol+=1
        contCol = 0
        contLine+=1
    #print squareMatriz
    return squareMatriz

def obter_aresta_correspondente_a_id_palavra_chave(cont, X, correspondencia):
    return X[correspondencia[cont]]


def recoveryClusterFromX(X,class_members, correspondencia):

    cont = 0
    cluster = []
    for index in class_members:
        if index:
            #cluster.append(X[cont])
            aresta_correspondente_a_posicao = obter_aresta_correspondente_a_id_palavra_chave(cont, X, correspondencia)
            if not aresta_correspondente_a_posicao in cluster:
                cluster.append(aresta_correspondente_a_posicao)
        cont+=1

    return cluster


def saveToTxtBagOfWords(file, newCluser_k):

    for item in newCluser_k:
        aux=''
        for col in item:
            aux += col.__str__()+' '

        file.write('{0}\n'.format(aux.rstrip()))



def ap(file_name, categorical, isHomogeneousNetwork):

    ##############################################################################
    # Generate data
    if categorical:
        loadFromFile = False
        X_temp = buildAsCategorical(file_name, isHomogeneousNetwork)

        if loadFromFile:
            X = np.loadtxt('output/x.txt')
        else:
            correspondencia, X = makeCategoricalX(X_temp, isHomogeneousNetwork)
            print "X: ", X
            #np.savetxt('output/x.txt',X, fmt='%1.5e')
    else:
        X = _buildV(file_name)
    #print X

    ##############################################################################
    # Compute Affinity Propagation
    #af = AffinityPropagation(preference=-15, damping=0.9, convergence_iter=200, max_iter=2000).fit(X)


    if categorical and not isHomogeneousNetwork:
        af = AffinityPropagation( affinity='precomputed', preference=value, damping=0.985, convergence_iter=200, max_iter=2000).fit(X)
    else:
        af = AffinityPropagation( preference=value, damping=0.985, convergence_iter=200, max_iter=2000).fit(X)

    cluster_centers_indices = af.cluster_centers_indices_
    #affinity_matrix = af.affinity_matrix_a
    #print affinity_matrix
    #print X #("o X 2 e", X)
    labels = af.labels_
    n_clusters_ = len(cluster_centers_indices)

    print('Estimated number of clusters: %d' % n_clusters_)

    ##############################################################################
    # Plot result
    #import matplotlib.pyplot as plt
    from itertools import cycle

    #plt.close('all')
    #plt.figure(1)
    #plt.clf()

    file = open("detcomNV/output/clusters.txt", "w")

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        cont_labels = labels == k
        class_members = cont_labels
        #cluster_center = X[cluster_centers_indices[k]]
        #plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
        #plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
        #         markeredgecolor='k', markersize=14)

        #print("\nCluster: %d\n" % k)

        file.write('cluster: {0}\n'.format(k))

        if not categorical:
            cluster_k = X[class_members]
            np.savetxt(file, cluster_k, fmt='%1.5e')

            #print cluster_k
        else:
            newCluser_k = recoveryClusterFromX(X_temp, class_members, correspondencia)
            if isHomogeneousNetwork:
                saveToTxtBagOfWords(file, newCluser_k)
            else:
                np.savetxt(file, newCluser_k, fmt='%1.5e')
        print newCluser_k


            #print newCluser_k

        #for x in X[class_members]:
        #   plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

    file.close()

    #plt.title('Estimated number of clusters: %d' % n_clusters_)
    #plt.show()

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def treatStringVetToNumber(vet):

    newVet = []
    for item in vet:
        if RepresentsInt(item):
            newVet.append(int(item))
        elif RepresentsFloat(item):
            newVet.append(float(item))
        else:
            newVet.append(item)
    print newVet
    return newVet

#as is possible to have categorical values and noncategorical values, need to create this matrix
# for the categoricalDist function
#_buildV transform all values to float, but I want int (categorical) and float (noncategorical)
def buildAsCategorical(file_, isHomogeneousNetwork):

    vetResult = []
    with open(file_) as f:
        content = f.read().splitlines()
        for line in content:
            partitionList = line.split('   ')
            partitionList.pop(0)

            if not isHomogeneousNetwork:
                partitionList = treatStringVetToNumber(partitionList)

            vetResult.append(partitionList)

    return vetResult


def _buildV(file_):
    darry = np.loadtxt(file_)
    darry = sparse.csr_matrix(darry)
    return darry

if __name__ == "__main__":
    ap()