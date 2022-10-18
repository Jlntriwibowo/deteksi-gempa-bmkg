def ekstraksi_data():
    """
tanggal     : 16 Oktober 2022
waktu       : 08:13:24 WIB
magnitudo   :4.5
kedalaman   : 10 km
Koordinat   : 8.73 LS - 116.62 BT
Pusat Gempa : Pusat gempa berada di laut 13 km Tenggara Lombok Timur
Dirasakan (Skala MMI): III-IV Lombok Timur, III Lombok Barat, III Mataram, III Lombok Tengah, III Sumbawa Barat
 :return:
    """
    hasil = dict()
    hasil['tanggal'] = '16 Oktober 2022'
    hasil['waktu'] = '08:13:24 WIB'
    hasil['magnitudo'] = 4.5
    hasil['kedalaman'] = '10 km'
    hasil['koordinat'] = '8.73 LS - 116.62 BT'
    hasil['pusat gempa'] = 'Pusat gempa berada di laut 13 km Tenggara Lombok Timur'
    hasil['dirasakan'] = \
        '(Skala MMI): III-IV Lombok Timur, III Lombok Barat, III Mataram, III Lombok Tengah, III Sumbawa Barat'
    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"1.tanggal : \n           {result['tanggal']}")
    print(f"2. waktu : \n           {result['waktu']}")
    print(f"3. magnitudo : \n           {result['magnitudo']}")
    print(f"4. kedalaman : \n           {result['kedalaman']}")
    print(f"5. koordinat : \n           {result['koordinat']}")
    print(f"6. pusat gempa : \n           {result['pusat gempa']}")
    print(f"7. dirasakan : \n           {result['dirasakan']}")

