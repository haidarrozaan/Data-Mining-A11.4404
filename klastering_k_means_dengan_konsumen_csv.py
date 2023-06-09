# -*- coding: utf-8 -*-
"""Klastering K-Means dengan konsumen.CSV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19rOrLino-7kKN6PmlfxO05LRiA_QT7-g
"""

#Import Library yang akan digunakan
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

#Menyiapkan data dan memanggil dataset
dataset = pd.read_csv('konsumen.csv')
dataset.keys()

dataku = pd.DataFrame(dataset)
dataku.head()

#Konversi ke data Array
X = np.asarray(dataset)
print(X)

# tampilan data dalam bentuk scatter plot
plt.scatter(X[:,0], X[:,1], label='True Position')
plt.xlabel("tahun_berkerja")
plt.ylabel("Gaji")
plt.title("Grafik Penyebaran Data Konsumen")
plt.show()

#Mengaktifkan K-Means dengan jumlah K=2
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

#Menampilkan nilai Centroid yang digenerate oleh algoritma
print(kmeans.cluster_centers_)

#Plot Data Point
#Memvisualisasikan Hasil Klasterisasi Data Konsumen
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.xlabel("Gaji")
plt.ylabel("Pengeluaran")
plt.title("Grafik Hasil Klasterisasi Data Gaji dan Pengeluaran Konsumen")
plt.show()

#Plot Data Point
#Memvisualisasikan hasil klasterisasi dengan centroid dr masing2 klaster
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color='black')
plt.xlabel("Gaji")
plt.ylabel("Pengeluaran")
plt.title("Grafik Hasil Klasterisasi Data Gaji dan Pengeluaran Konsumen")
plt.show()