"""
Tanım   :Excel'de bulunan birden çok kişinin telefon numarası çekilip onlara birer
         dakika arayla mesaj gönderebilmek üzere tasarlandı. 
Uyarı   :Her telefon numarası için whatsapp sekmesini kapatmalısınız ki ötekine geçebilsin :(
"""

import pywhatkit as kit
import pandas as pd

excel_file = "C:/Users/Home-N/Desktop/denek.xls"

df = pd.read_excel(excel_file)

# Excel dosyamızda ilk iki sütun Ad ve Numara başlıklarıyla kullanılıyor
print(df["Numara"])

# Bu kodu denediğim sıralarda saat 18:45 ti. Dögü ile beraber 1'er dakikalık arayla sonraki kişiye geçecek
ct = 45
for n in df["Numara"]:
    kit.sendwhatmsg(str(n), "ikinci toplu mesaj denemesi :) ", 18, ct)
    ct = 1
