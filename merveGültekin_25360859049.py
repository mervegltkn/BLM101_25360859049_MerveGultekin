# input() fonksiyonu kullanıcıdan klavye ile veri almak için kullanılır
isim = input("Adınızı ve Soyadınızı giriniz: ")

# input() ile kullanıcıdan aldığı dersler bilgisi alınır
derslerim = input("Aldığınız dersleri virgülle yazınız: ")

# kullanıcıdan kısa biyografi bilgisi alınır
hakkimda = input("Kısa biyografinizi yazınız: ")

# HTML kodlarını tutmak için string değişkeni oluşturulur
html = "<html>\n"

# HTML sayfasının başlık kısmı eklenir
html += "<head>\n"
html += "<title>Kişisel Sayfam</title>\n"

# style etiketi ile sayfaya basit CSS eklenir
html += "<style>\n"
html += "body { background-color: white; font-family: Arial; color: black; }\n"
html += "h1 { color: black; }\n"
html += "</style>\n"

# head etiketi kapatılır
html += "</head>\n"

# body etiketi açılır
html += "<body>\n"

# h1 etiketi ile kullanıcının ismi başlık olarak yazdırılır
html += "<h1>" + isim + "</h1>\n"

# p etiketi ile biyografi bilgisi paragraf olarak eklenir
html += "<p>" + hakkimda + "</p>\n"

# Dersler için başlık eklenir
html += "<h2>Aldığım Dersler</h2>\n"
html += "<ul>\n"

# split() fonksiyonu girilen dersleri virgüle göre ayırır
ders_listesi = derslerim.split(",")

# for döngüsü ile her ders liste elemanı olarak eklenir
for ders in ders_listesi:
    html += "<li>" + ders + "</li>\n"

# ul etiketi kapatılır
html += "</ul>\n"

# body ve html etiketleri kapatılır
html += "</body>\n"
html += "</html>"

# open() fonksiyonu ile index.html dosyası yazma modu açılır
dosya = open("index.html", "w", encoding="utf-8")

# write() fonksiyonu HTML içeriğini dosyaya yazdırır
dosya.write(html)

# close() fonksiyonu dosyayı kapatır
dosya.close()


print("HTML dosyası başarıyla oluşturuldu.")
