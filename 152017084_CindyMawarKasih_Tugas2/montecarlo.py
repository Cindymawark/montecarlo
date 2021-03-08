import streamlit as st
import pandas as pd
import numpy as np
import random
import os

st.title('Program Pemodelan Montecarlo')
st.write('NRP  : 152017084')
st.write('Nama : Cindy Mawar Kasih')

data = np.array([[0, 20], [1, 40], [2, 20], [3, 10], [4, 10]])
st.write(pd.DataFrame(data, columns=["Minggu - Ke", "Frekuensi"]))

mingguke = data[:0]
frek = data[:, 1]

SigmaFrek = 0
for i in range(len(frek)):
    SigmaFrek = SigmaFrek + frek[i]
st.write('Nilai Sigma Frekuensi adalah ', SigmaFrek)

probabilitas = []
sumf = 0
for a in range(len(frek)):
    sumf = frek[a]/SigmaFrek
    st.write("Probabilitas minggu ke-", a, "=", sumf)
    probabilitas.append(sumf)

probabilitas_d = np.array([probabilitas])
data = np.concatenate((data, probabilitas_d.T), axis=1)
st.write('Tabel Menambahkan Column Probabilitas')
st.write(pd.DataFrame(data, columns=[
         "Minggu Ke", "Frekuensi", "Probabilitas"]))

probabilitas_k = []
sump = 0
for a in range(len(frek)):
    sump = sump + probabilitas[a]
    st.write("probabilitas kumulatif minggu ke-", a, "=", sump)
    probabilitas_k.append(sump)

probabilitas_kd = np.array([probabilitas_k])
data = np.concatenate((data, probabilitas_kd.T), axis=1)
st.write('Tabel Menambahkan Column Probabilitas Komulatif')
st.write(pd.DataFrame(data, columns=["Minggu Ke", "Frekuensi",
                                     "Probabilitas", "Probabilitas Kumulatif"]))

interval_min = []
min_v = 0
for a in range(len(frek)):
    if(a == 0):
        interval_min.append(min_v)
        st.write("Interval Minggu ke-", a, " = ",
                 min_v, "-", probabilitas_k[a])
    else:
        min_v = probabilitas_k[a-1]+0.001
        interval_min.append(min_v)
        st.write("Interval Minggu ke-", a,
                 " = ", min_v, "-", probabilitas_k[a])

interval_mind = np.array([interval_min])
data = np.concatenate((data, interval_mind.T), axis=1)
interval_maxd = np.array([probabilitas_k])
data = np.concatenate((data, interval_maxd.T), axis=1)
st.write('Tabel Menambahkan Column Interval')
st.write(pd.DataFrame(data, columns=["Minggu Ke", "Frekuensi", "Probabilitas",
                                     "Probabilitas Kumulatif", "Interval Batas Bawah", "Interval Batas Atas"]))

minggu_baru = 101
p_minggu = []
angka_acak = []
permintaan = []
for a in range(16):
    p_minggu.append(minggu_baru)
    acak = random.random()
    angka_acak.append(acak)
    if(acak < 0.2):
        jenis = 0
        permintaan.append(jenis)
    elif(acak < 0.6):
        jenis = 1
        permintaan.append(jenis)
    elif(acak < 0.8):
        jenis = 2
        permintaan.append(jenis)
    elif(acak < 0.9):
        jenis = 3
        permintaan.append(jenis)
    elif(acak <= 1):
        jenis = 4
        permintaan.append(jenis)
    minggu_baru += 1

st.markdown('<style>body{background-color: #E3c7dd;}</style>',unsafe_allow_html=True)
st.write("Minggu Ke-", "|", "Angka Acak", "|", "Permintaan")
for a in range(16):
    st.write(p_minggu[a], "|", angka_acak[a], "|", permintaan[a])
