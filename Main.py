"""
Program Deteksi Gempa
"""
import Gempa_terkini

if __name__ == '__main__' :
    print('aplikasi utama')
    result = Gempa_terkini.ekstraksi_data()
    Gempa_terkini.tampilkan_data(result)

import Perkiraan_Cuaca

if __name__ == '__main__' :
    print('Aplikasi Cuaca di Temanggung')
    result = Perkiraan_Cuaca.ekstraksi_data()
    Perkiraan_Cuaca.tampilkan_data(result)
