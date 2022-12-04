import pickle
import streamlit as st

#membaca model

mobil_model = pickle.load(open('mobil_model.sav', 'rb'))

#Nama Web
st.title('Prediksi harga Mobil Bekas Eropa')


col1, col2 = st.columns(2)

with col1 :
    year = st.text_input ('masukan Tahun(skala : 2015 - 2020)')
    mileage = st.text_input('masukan Jarak tempuh(skala : 10k - 100k)')
    tax = st.text_input('masukan harga pajak (skala : £0 - £200)')
with col2 :    
    mpg = st.text_input('masukan nilai konsumsi bahan bakar miles/gallon (skala : 40.0 - 75.0)')
    engineSize = st.text_input('masukan ukuran mesin (skala : 1.0-3.0)')


# membuat Tombol Untuk Prediksi
if st.button('Test Prediksi Harga Mobil'):
    prediction_old = mobil_model.predict([[year, mileage, tax, mpg, engineSize]])
    prediction_new = mobil_model.predict([[year, mileage, tax, mpg, engineSize]])
    'Prediksi harga mobil lama: £', prediction_old , 'atau jika dirupiahkan yaitu: Rp', prediction_old * 18908*1e-9 , 'Milyar'
    'Prediksi harga mobil baru: £', prediction_new, 'atau jika dirupiahkan yaitu: Rp', prediction_new * 18908*1e-9, 'Milyar'
# st.success(ket_harga)