import veri_getir as vt


rows = vt.find("yks","acik-deniz-sondaj-teknolojisi","bolum")

print("\n\n")

istek_üniler=['ESKİŞEHİR OSMANGAZİ ÜNİVERSİTESİ','İNÖNÜ ÜNİVERSİTESİ']

for i in rows:
    if i[2] in istek_üniler:
        print(i)