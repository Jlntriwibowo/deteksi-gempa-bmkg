import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    """
tanggal     : 16 Oktober 2022
waktu       : 08:13pip:24 WIB
magnitudo   :4.5
kedalaman   : 10 km
Koordinat   : 8.73 LS - 116.62 BT
Pusat Gempa : Pusat gempa berada di laut 13 km Tenggara Lombok Timur
Dirasakan (Skala MMI): III-IV Lombok Timur, III Lombok Barat, III Mataram, III Lombok Tengah, III Sumbawa Barat
 :return:
    """
#menghindari error menjadi None

    try:
        content = requests.get('https://www.bmkg.go.id')
    except Exception:
        return None

# Mencari tanggal dan waktu class sudah jelas
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        resulttime = soup.find('span',{'class' : 'waktu'})
        resulttime = resulttime.text.split(', ')
        tanggal = resulttime[0]
        waktu = resulttime[1]
# Mencari Magnitudo dll karena unordered list
        resultm = soup.find('div', {'class' : "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        resultm = resultm.findChildren ('li')
        i=0
        magnitudo = None
        kedalaman = None
        Koordinat = None
        Pusat_Gempa = None
        Dirasakan = None
        for res in resultm:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            if i == 2 :
                kedalaman = res.text
            if i == 3 :
                koordinat = res.text
            if i == 4 :
                Pusat_Gempa = res.text
            if i == 5 :
                Dirasakan = res.text
            i=i+1
#mencari hasil
        hasil = dict()
        hasil['tanggal'] = tanggal #'16 Oktober 2022'
        hasil['waktu'] = waktu #'08:13:24 WIB'
        hasil['magnitudo'] = magnitudo #4.5
        hasil['kedalaman'] = kedalaman #'10 km'
        hasil['koordinat'] = koordinat #'8.73 LS - 116.62 BT'
        hasil['pusat gempa'] = Pusat_Gempa #'Pusat gempa berada di laut 13 km Tenggara Lombok Timur'
        hasil['dirasakan'] = Dirasakan
            #'(Skala MMI): III-IV Lombok Timur, III Lombok Barat, III Mataram, III Lombok Tengah, III Sumbawa Barat'
        return hasil
    else :
        return None
#mencetak hasil
def tampilkan_data(result):
    if result is None:
        print('data tidak di temukan')
        return
    print('Gempa terakhir berdasarkan BMKG')
    print(f"1.tanggal : \n           {result['tanggal']}")
    print(f"2. waktu : \n           {result['waktu']}")
    print(f"3. magnitudo : \n           {result['magnitudo']}")
    print(f"4. kedalaman : \n           {result['kedalaman']}")
    print(f"5. koordinat : \n           {result['koordinat']}")
    print(f"6. pusat gempa : \n           {result['pusat gempa']}")
    print(f"7. dirasakan : \n           {result['dirasakan']}")

