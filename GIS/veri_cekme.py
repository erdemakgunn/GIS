import urllib
import urllib.request
import json  # data formatının dönüşümü
import pandas as pd  # analizler için
url = "https://data.ibb.gov.tr/datastore/odata3.0/c611b9a1-8a1a-44a9-816b-eb6dfcd37c42?$format=json"

def ibbVeriToDataframe(urladresi):
    # API bağlantısı
    sorgu = urllib.request.urlopen(urladresi)
    # Veriyi python-json dosya biçimine dönüştürme
    data = json.loads(sorgu.read().decode())
    # Sadece datanın olduğu bölümün alınması
    data = data.get("value")
    # Verinin dataframe formatına dönüştürülmesi
    return pd.DataFrame(data)

# fonksiyonun çalıştırılması
df = ibbVeriToDataframe(url)
# print(df.columns) # Kolon isimleri
df = df.drop(columns="_id")  # ID kolonunun çıkarılması

istasyon_kordinat_isim = df[["Koordinat", "ITFAIYE_BIRIM_ADI"]]
# print(istasyon_kordinat_isim)
