# # KODE 1-1
# def norm_data(data):

#     data_max = max(data)
#     data_min = min(data)
#     data_len = len(data)

#     for i in range(0, data_len):
#         data[i] = (data[i] - data_min) / (data_max - data_min)
    
#     return data

# #Contoh Penggunaan
# data = [10, 11, 12, 13, 14, 16]
# n_data = norm_data(data) #Normalisasi
# print(n_data)


# # KODE 1-2
# import numpy as np
# from sklearn.preprocessing import MinMaxScaler

# np.set_printoptions(precision=6) # bulatkan 4 angkat koma
# np.set_printoptions(suppress=True) # hilangkan nilai e

# # Kita akan membentuk data
# # Hal ini dikarenakan, scikit-learn hanya menerima input dalam bentuk n-dimensional array
# data = [
#     [100, 0.0001],
#     [50, 0.05],
#     [30, 0.003]
# ]

# # Ubah ke bentuk numpy n-dimensional array
# data = np.asarray(data)
# print('Data Asli')
# print(data)

# # Mendefinisikan obyek MinMaxScaler
# scaler = MinMaxScaler()
# # Transformasikan data
# scaled = scaler.fit_transform(data)
# print('Data Normalisasi')
# print(scaled)


# # KODE 1-3
# import numpy as np
# from sklearn.discriminant_analysis import StandardScaler

# np.set_printoptions(precision=6) # bulatkan 4 angkat koma
# np.set_printoptions(suppress=True) # hilangkan nilai e

# # Kita akan membentuk data
# # Hal ini dikarenakan, scikit-learn hanya menerima input dalam bentuk n-dimensional array
# data = [
#     [100, 0.0001],
#     [50, 0.05],
#     [30, 0.003]
# ]

# # Ubah ke bentuk numpy n-dimensional array
# data = np.asarray(data)
# print('Data Asli')
# print(data)

# # Mendefinisikan obyek MinMaxScaler
# scaler = StandardScaler()
# # Transformasikan data
# scaled = scaler.fit_transform(data)
# print('Data Standarisasi')
# print(scaled)


# # # KODE 1-4
# from sklearn.preprocessing import OrdinalEncoder

# # Inisiasi obyek Ordinal Encoder
# oe = OrdinalEncoder()

# # Definisikan data
# # dalam bentuk 2d

# data = [
#     ['Politeknik Negeri Malang'],
#     ['Politeknik Elektronika Negeri Surabaya'],
#     ['Politeknik Negeri Jakarta'],
#     ['Politeknik Negeri Semarang']
# ]

# # Transformasi Ordinal Encoder
# transform_oe = oe.fit_transform(data)

# print('Data Asli')
# print(data)

# print('Data Transformasi Ordinal Encoder')
# print(transform_oe)


# # KODE 1-5
# from sklearn.preprocessing import OneHotEncoder

# # Inisiasi obyek Ordinal Encoder
# ohe = OneHotEncoder()

# # Definisikan data
# # dalam bentuk 2d

# data = [
#     ['Politeknik Negeri Malang'],
#     ['Politeknik Elektronika Negeri Surabaya'],
#     ['Politeknik Negeri Jakarta'],
#     ['Politeknik Negeri Semarang']
# ]

# # Transformasi Ordinal Encoder
# transform_ohe = ohe.fit_transform(data)

# print('Data Asli')
# print(data)

# print('Data Transformasi One-Hot Encoding')
# print(transform_ohe.toarray())

# # KODE 1-6
# from sklearn.preprocessing import OneHotEncoder

# # Inisiasi obyek Ordinal Encoder
# de = OneHotEncoder(drop='first')

# # Definisikan data
# # dalam bentuk 2d

# data = [
#     ['Politeknik Negeri Malang'],
#     ['Politeknik Elektronika Negeri Surabaya'],
#     ['Politeknik Negeri Jakarta'],
#     ['Politeknik Negeri Semarang']
# ]

# # Transformasi Ordinal Encoder
# transform_de = de.fit_transform(data)

# print('Data Asli')
# print(data)

# print('Data Transformasi One-Hot Encoding')
# print(transform_de.toarray())


