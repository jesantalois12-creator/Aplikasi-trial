import streamlit as st

# Judul Utama Aplikasi
st.title("🎈 Aplikasi Interaktif Baruku")

# Input Teks untuk Nama Pengguna
nama_pengguna = st.text_input("Siapa nama Anda?", placeholder="Ketik nama Anda di sini...")

# Tombol Klik Interaktif
if st.button("Klik Saya!"):
    if nama_pengguna:
        st.success(f"Halo, {nama_pengguna}! Selamat datang di aplikasi Streamlit pertamaku! 🎉")
    else:
        st.warning("Silakan ketik nama Anda terlebih dahulu di kolom atas! 😮")
