"""
Program Deteksi Gempa
"""
from Gempa_terkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__' :
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)

    