# # KODE 1-10
# from sklearn.feature_extraction.text import TfidfVectorizer

# corpus = [
#     'the house had a tiny little mouse',
#     'the cat saw the mouse',
#     'the mouse ran away from the house',
#     'the cat finally ate the mouse',
#     'the end of the mouse story'
# ]

# # Inisiasi obyek TFidVectorizer
# vect = TfidfVectorizer(stop_words='english')

# # Pembobotan TF-IDF
# resp = vect.fit_transform(corpus)

# # Cetak hasil
# print('Hasil TF-IDF')
# print(resp)

# # Cetak token hasil stopword
# print('Hasil Token')
# print(vect.get_feature_names_out())


# PRAKTIKUM
from sklearn.feature_extraction.text import TfidfVectorizer

# Membaca file 'corpus.txt'
with open('corpus.txt', 'r') as file:
    corpus = file.readlines()

# Inisiasi obyek TfidfVectorizer, dan hilangkan stopwords bahasa Inggris
vect = TfidfVectorizer(stop_words='english')

# Lakukan pembobotan TF-IDF
resp = vect.fit_transform(corpus)

# Cetak hasil TF-IDF dalam bentuk sparse matrix
print('Hasil TF-IDF')
print(resp)

# Cetak token hasil setelah stopword dihilangkan
print('Hasil Token')
print(vect.get_feature_names_out())