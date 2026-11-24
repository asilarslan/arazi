# Tools and guides for arazi.app (Turkish).

UNITS = [
    ("m2", 1.0, {"tr": "Metrekare (m²)"}),
    ("donum", 1_000.0, {"tr": "Dönüm / dekar (1.000 m²)"}),
    ("ha", 10_000.0, {"tr": "Hektar (ha)"}),
    ("evlek", 250.0, {"tr": "Evlek (250 m²)"}),
    ("a", 100.0, {"tr": "Ar (100 m²)"}),
    ("km2", 1_000_000.0, {"tr": "Kilometrekare (km²)"}),
    ("ac", 4_046.8564224, {"tr": "Akre (ac)"}),
    ("ft2", 0.09290304, {"tr": "Fit kare (ft²)"}),
]

TOOL = {
    "tr": dict(path="/donum-hesaplama/", title="Dönüm Hesaplama: Dönüm, Metrekare, Hektar Çevirici (Ücretsiz)",
               desc="Dönümü metrekareye, hektara, evleğe ve akreye anında çevirin. 1 dönüm kaç metrekare, 1 hektar kaç dönüm? En × boy ile arsa alanı hesaplayıcı da burada.",
               h1="Dönüm hesaplama", intro="Herhangi bir birime değer yazın, diğer tüm birimleri hemen görün. Altında, dikdörtgen bir arsanın alanını eninden ve boyundan hesaplayın.",
               rect_h="En × boy ile alan hesaplama", length="Boy", width="En", in_unit="Birim", result="Alan",
               len_units=[("metre", 1), ("adım (~0,75 m)", 0.75)],
               table_h="Hızlı tablo", note="Hesaplamalar tarayıcınızda yapılır.",
               body="""<h2>Sık kullanılan çevirmeler</h2>
<div class="table-scroll"><table>
<tr><th>Birim</th><th>Karşılığı</th></tr>
<tr><td>1 dönüm (dekar)</td><td>1.000 m² · 0,1 hektar · 4 evlek</td></tr>
<tr><td>1 hektar</td><td>10.000 m² · 10 dönüm</td></tr>
<tr><td>1 evlek</td><td>250 m² · ¼ dönüm</td></tr>
<tr><td>1 ar</td><td>100 m²</td></tr>
<tr><td>1 akre</td><td>4.046,86 m² · yaklaşık 4 dönüm</td></tr>
</table></div>
<h2>Dönüm ile dekar aynı mı?</h2>
<p>Bugün kullanılan dönüm, metrik dönümdür ve dekarla aynıdır: 1.000 m². Osmanlı döneminden kalan “eski dönüm” ise yaklaşık 919 m² idi; eski belgelerde bu ölçüye rastlayabilirsiniz. Tapuda alan metrekare olarak yazar.</p>
<p>Alanı bilmiyor musunuz? <a href="/rehber/arsa-olcumu-nasil-yapilir/">Arsa ölçümü rehberimize</a> bakın ya da Arazi Ölçme uygulamasıyla uydu haritasında köşelere dokunarak ölçün.</p>""",
               faq=[("1 dönüm kaç metrekare?", "1.000 metrekare."), ("1 hektar kaç dönüm?", "10 dönüm."),
                    ("1 dönüm kaç evlek?", "4 evlek; 1 evlek 250 m²'dir."), ("1 akre kaç dönüm?", "Yaklaşık 4,05 dönüm.")]),
}

TAKS_HTML = """<div class="tool" data-taks>
<h3>Arsa bilgileri</h3>
<div class="rgrid"><label>Arsa alanı (m²)<input type="text" inputmode="decimal" data-area placeholder="örn. 500"></label>
<label>TAKS<input type="text" inputmode="decimal" data-t placeholder="örn. 0,30"></label>
<label>KAKS (emsal)<input type="text" inputmode="decimal" data-k placeholder="örn. 1,20"></label></div>
<div class="res" data-tout hidden>
<div><b data-base>—</b><span>En fazla taban alanı</span></div>
<div><b data-total>—</b><span>Toplam inşaat alanı (emsal)</span></div>
<div><b data-floors>—</b><span>Taban alanı tam kullanılırsa kat sayısı</span></div>
</div>
<p class="tnote">Hesaplama tarayıcınızda yapılır. Kesin değerler için belediyeden imar durum belgesi alın.</p>
</div>"""

EXTRA_TOOLS = [dict(
    lang="tr", path="/taks-kaks-hesaplama/", nav="TAKS/KAKS hesaplama", html=TAKS_HTML,
    title="TAKS KAKS Hesaplama: Arsaya Kaç Metrekare Ev Yapılır? (Ücretsiz)",
    desc="Arsa alanı, TAKS ve KAKS (emsal) değerini girin; en fazla taban alanını, toplam inşaat alanını ve kat sayısını anında hesaplayın.",
    h1="TAKS ve KAKS hesaplama",
    intro="Arsanıza en fazla ne büyüklükte bina yapılabileceğini görün: arsa alanını ve imar durumundaki TAKS ve KAKS değerlerini yazın.",
    body="""<h2>TAKS nedir?</h2>
<p><b>Taban Alanı Kat Sayısı</b>, binanın zemine oturan alanının arsa alanına oranıdır. TAKS 0,30 ise 500 m²'lik arsada taban alanı en fazla 150 m² olabilir.</p>
<h2>KAKS (emsal) nedir?</h2>
<p><b>Kat Alanları Kat Sayısı</b>, yani emsal, tüm katların toplam alanının arsa alanına oranıdır. KAKS 1,20 ise 500 m²'lik arsada toplam inşaat alanı 600 m² olabilir. Bu örnekte 150 m² tabanla 4 kat yapılabilir.</p>
<h2>Nereden öğrenilir?</h2>
<p>TAKS, KAKS, kat adedi ve çekme mesafeleri parselin <b>imar durum belgesinde</b> yazar; belediyeden ya da e-Devlet üzerinden bazı belediyelerin imar sorgulama ekranlarından öğrenebilirsiniz. Bazı alanlar (örneğin belirli koşullarda balkon, otopark) emsale dahil edilmeyebilir; ayrıntı için mimarınıza danışın.</p>
<p>Çekme mesafelerinin yapılaşma alanını nasıl küçülttüğünü görmek için Arazi Ölçme'deki Arsa Analizi'nin Yerleşim sekmesini kullanabilirsiniz.</p>""",
    faq=[("TAKS ile KAKS arasındaki fark nedir?", "TAKS yalnızca zemine oturan taban alanını, KAKS (emsal) tüm katların toplam alanını sınırlar."),
         ("Emsal 1 ne demek?", "Toplam inşaat alanı arsa alanı kadar olabilir: 500 m²'lik arsada 500 m²."),
         ("Hesap kesin mi?", "Hayır, ön fikir verir. Kesin hak için imar durum belgesi ve mimari proje gerekir.")],
)]

GUIDES = [
    dict(lang="tr", path="/rehber/arsa-olcumu-nasil-yapilir/", shot="measure", alts={"en": "https://fieldareameasure.com/guides/how-to-measure-land-area/"},
         title="Arsa ve Tarla Ölçümü Nasıl Yapılır? Telefondan Resmî Ölçüme 4 Yol",
         desc="Tarla, bahçe veya arsa alanını ölçmenin yolları: uydu haritasında köşe işaretleme, GPS ile dolaşma, şerit metre ve üçgenler, harita mühendisi ölçümü.",
         h1="Arsa ve tarla ölçümü nasıl yapılır?",
         intro="Bir arazinin alanını özel bir alet olmadan öğrenebilirsiniz. En hızlısından en kesinine dört yöntem:",
         body="""<ol class="checks">
<li><b>Uydu haritasında köşeleri işaretleyin</b>Yukarıdan görülebilen tarla ve arsalar için en hızlı yol. Ölçüm uygulamasında araziyi bulun, her köşeye dokunun, alanı ve çevreyi okuyun. Doğruluk, görüntüye ve köşeleri ne kadar dikkatli koyduğunuza bağlıdır; genellikle birkaç yüzde içinde kalır.</li>
<li><b>GPS ile sınırı dolaşın</b>Ağaç altındaki ya da yukarıdan seçilemeyen sınırlar için. Telefon GPS'i genellikle birkaç metre hassasiyetlidir; küçük arsalarda bu fark önemlidir.</li>
<li><b>Şerit metre ve üçgenler</b>Küçük bahçeler için: kenarları ölçün, şekli dikdörtgen ve üçgenlere bölüp alanları toplayın.</li>
<li><b>Harita mühendisi ölçümü</b>Tapu, satış, ifraz ve yapı ruhsatı gibi resmî işlemlerde yalnızca lisanslı harita mühendisinin ölçümü geçerlidir.</li>
</ol>
<h2>Daha iyi sonuç için</h2>
<ul><li>Köşeleri koymadan önce iyice yakınlaştırın; köşeyi gerçek sınıra (çit, duvar, ark) koyun, gölgeye değil.</li><li>Kıvrımlı kenarlara ara noktalar ekleyin.</li><li>Sonucu tapudaki alanla karşılaştırın; küçük farklar normaldir.</li></ul>
<p>Alanı dönüme çevirmek için <a href="/donum-hesaplama/">dönüm hesaplayıcıyı</a> kullanın.</p>""",
         faq=[("Telefonla arsa ölçülür mü?", "Evet. Uydu haritasında köşeleri işaretleyerek ya da GPS ile sınırı dolaşarak ölçebilirsiniz."),
              ("Ölçüm tapudan neden farklı?", "Tapu eski ölçümlere, farklı sınırlara ya da yuvarlamaya dayanabilir. Resmî alan için harita mühendisine başvurun.")]),
    dict(lang="tr", path="/rehber/dekar-donum-hektar-farki/", shot="detail",
         title="Dekar, Dönüm, Hektar Farkı: 1 Dönüm Kaç Metrekare?",
         desc="Dönüm ve dekar aynı mı, hektar kaç dönüm, evlek nedir, eski dönüm kaç metrekare? Türkiye'deki arazi ölçü birimleri tek sayfada.",
         h1="Dekar, dönüm ve hektar farkı",
         intro="Türkiye'de arazi alanı metrekare, dönüm (dekar) ve hektarla konuşulur. Hepsinin birbirine göre karşılığı:",
         body="""<ul>
<li><b>1 dönüm = 1 dekar = 1.000 m²</b></li>
<li><b>1 hektar = 10 dönüm = 10.000 m²</b></li>
<li><b>1 evlek = 250 m²</b> (çeyrek dönüm)</li>
<li><b>1 ar = 100 m²</b></li>
<li><b>1 akre ≈ 4.047 m² ≈ 4 dönüm</b> (ABD ve İngiltere'de kullanılır)</li>
</ul>
<h2>Eski dönüm</h2>
<p>Osmanlı döneminde kullanılan dönüm, kenarı 40 standart arşın olan bir kare olarak tanımlanırdı ve yaklaşık 919 m²'ye karşılık gelirdi. Bugün dönüm denince metrik dönüm (1.000 m²) kastedilir; tapuda alan metrekare yazar.</p>
<h2>Hızlı örnekler</h2>
<ul><li>2.500 m² = 2,5 dönüm = 10 evlek</li><li>7,5 dönüm = 7.500 m² = 0,75 hektar</li><li>3 hektar = 30 dönüm</li></ul>
<p>Kendi değerinizi çevirmek için <a href="/donum-hesaplama/">dönüm hesaplayıcıyı</a> kullanın.</p>""",
         faq=[("Dekar ile dönüm aynı mı?", "Evet, ikisi de 1.000 m²'dir."), ("1 hektar kaç dönüm?", "10 dönüm.")]),
    dict(lang="tr", path="/rehber/taks-kaks-emsal-nedir/", shot="site1",
         title="TAKS, KAKS ve Emsal Nedir? Arsaya Kaç Katlı Ev Yapılır?",
         desc="TAKS (taban alanı kat sayısı), KAKS (emsal), çekme mesafeleri ve imar durumu: arsaya ne büyüklükte bina yapılabileceğini örneklerle anlatıyoruz.",
         h1="TAKS, KAKS ve emsal nedir?",
         intro="Arsanın büyüklüğü, üzerine yapabileceğiniz binanın büyüklüğü değildir. İmar planındaki üç değer sınırı belirler: TAKS, KAKS ve çekme mesafeleri.",
         body="""<h2>TAKS: taban alanı</h2>
<p>Binanın zemine oturan alanının arsa alanına oranıdır. 400 m² arsa, TAKS 0,25 → taban alanı en fazla 100 m².</p>
<h2>KAKS (emsal): toplam inşaat alanı</h2>
<p>Tüm katların toplam alanının arsa alanına oranıdır. 400 m² arsa, KAKS 0,75 → toplam en fazla 300 m², yani 100 m² tabanla 3 kat.</p>
<h2>Çekme mesafeleri</h2>
<p>Binanın komşu sınırlara ve yola olan en az uzaklığıdır. Plan aksini söylemiyorsa Planlı Alanlar İmar Yönetmeliği'ne göre ön bahçe genellikle 5 m, yan ve arka bahçe 3 m'dir. Dar arsalarda çekme mesafeleri, TAKS'ın izin verdiği alanı daha da küçültebilir.</p>
<div class="note-box">Değerler parselden parsele değişir. Kesin bilgi için belediyeden imar durum belgesi alın.</div>
<p>Hesap için <a href="/taks-kaks-hesaplama/">TAKS/KAKS hesaplayıcıyı</a> kullanın. Arazi Ölçme'deki Arsa Analizi de çekme mesafelerine göre yapılaşma alanını ve örnek bir yerleşimi gösterir.</p>""",
         faq=[("Emsal nedir?", "KAKS'ın diğer adıdır: toplam inşaat alanının arsa alanına oranı."),
              ("İmar durumu nereden alınır?", "Parselin bağlı olduğu belediyeden; bazı belediyeler çevrim içi imar sorgulama sunar.")]),
    dict(lang="tr", path="/rehber/arsa-alirken-nelere-dikkat-edilmeli/", shot="site3",
         title="Arsa Alırken Nelere Dikkat Edilmeli? 10 Maddelik Kontrol Listesi",
         desc="Arsa almadan önce kontrol edilmesi gerekenler: tapu ve hisse durumu, imar durumu, TAKS/KAKS, yola cephe, eğim, güneş yönü, altyapı ve zemin.",
         h1="Arsa alırken nelere dikkat edilmeli?",
         intro="Arsa alımı, sonradan düzeltilmesi zor bir karardır. Ödeme yapmadan önce bu on maddeyi kontrol edin.",
         body="""<ol class="checks">
<li><b>Tapu ve hisse durumu</b>Tapunun müstakil mi hisseli mi olduğunu, üzerinde haciz, ipotek veya şerh bulunup bulunmadığını kontrol edin.</li>
<li><b>İmar durumu</b>Belediyeden imar durum belgesi alın: konut, ticari, tarla mı? Yapılaşmaya açık mı?</li>
<li><b>TAKS, KAKS ve kat adedi</b>Ne büyüklükte ve kaç katlı bina yapılabileceğini belirler.</li>
<li><b>Gerçek alan</b>Tapudaki alanı kendi ölçümünüzle karşılaştırın; büyük fark varsa harita mühendisine danışın.</li>
<li><b>Yola cephe</b>Parselin imarlı bir yola cephesi olup olmadığını kontrol edin.</li>
<li><b>Güneş yönü</b>Yaşam alanlarının ve bahçenin güneyi görmesi kışın büyük avantajdır.</li>
<li><b>Eğim</b>Eğimli arsada temel, istinat duvarı ve merdiven maliyeti artar; sokaktan girişi düşünün.</li>
<li><b>Altyapı</b>Elektrik, su, kanalizasyon ve doğalgaz bağlantısının olup olmadığını öğrenin.</li>
<li><b>Zemin</b>Zemin etüdü raporu varsa isteyin; dolgu ve dere yatağı risklerine dikkat edin.</li>
<li><b>Çevre ve plan değişiklikleri</b>Yakında planlanan yol, sanayi ya da plan değişikliği olup olmadığını belediyeye sorun.</li>
</ol>
<p>Güneş, yerleşim, eğim ve varış maddelerini Arazi Ölçme'deki Arsa Analizi tek sayfalık bir karnede özetler.</p>""",
         faq=[("Hisseli tapulu arsa alınır mı?", "Alınabilir ama yapılaşma ve satışta diğer hissedarların onayı gerekebilir; bir avukata danışın.")]),
    dict(lang="tr", path="/rehber/evin-cephesi-hangi-yone-bakmali/", shot="site0",
         title="Evin Cephesi Hangi Yöne Bakmalı? Arsada Güneş Yönü Rehberi",
         desc="Türkiye'de evin salonu ve bahçesi hangi yöne bakmalı, güney cephenin avantajları, saçak derinliği ve eğimli arsada güneş. Arsa almadan önce okuyun.",
         h1="Evin cephesi hangi yöne bakmalı?",
         intro="Güneşin arsaya düşüş şekli bahçeden ısınma faturasına kadar her şeyi etkiler. Türkiye kuzey yarımkürede olduğundan kural basittir: güneye bakan cephe en çok güneşi alır.",
         body="""<h2>Güneşin yolu mevsime göre değişir</h2>
<p>Öğle vakti güneş tam güneydedir. Yazın yüksekte, kışın alçaktadır. Bu yüzden güney cephe kışın alçak ve sıcak güneşi alır, yazın ise yüksek güneşe karşı kolayca gölgelenir.</p>
<h2>Güneşli tarafa neler gelmeli?</h2>
<ul><li>Salon, mutfak ve büyük pencereler</li><li>Bahçe ve teras: evi arsanın daha gölgeli kenarına yaklaştırın ki en güneşli kısım bahçeye kalsın</li></ul>
<h2>Saçak: yazın gölge, kışın güneş</h2>
<p>Enleminize göre doğru boyutlanmış bir saçak, yaz güneşini keser ama kış güneşinin pencereye ulaşmasına izin verir. Doğru derinlik pencere yüksekliğine ve pencerenin üstündeki boşluğa bağlıdır.</p>
<h2>Eğime de bakın</h2>
<p>Güneye eğimli arsada aydınlık odalar kolay elde edilir; kuzeye eğimli arsada alçak kısım kışın uzun süre gölgede kalabilir.</p>
<p>Arazi Ölçme'nin Arsa Analizi, ölçtüğünüz arsada yaz ve kış güneşinin yolunu, öğle güneşi yüksekliğini ve önerilen saçak derinliğini gösterir.</p>""",
         faq=[("Kuzey cepheli ev kötü mü?", "Kötü değil ama kışın daha az doğrudan güneş alır; yaşam alanlarını mümkünse güneye yönlendirmek avantajlıdır.")]),
]

HUB = dict(path="/rehber/", title="Arazi ve Arsa Rehberleri: Ölçüm, Dönüm, TAKS/KAKS | Arazi Ölçme",
           desc="Arsa ölçümü, dekar-dönüm-hektar farkı, TAKS ve KAKS, arsa alırken dikkat edilecekler ve güneş yönü üzerine pratik rehberler.",
           h1="Arazi ve arsa rehberleri", intro="Çiftçiler, arsa alıcıları ve ev yapacaklar için pratik bilgiler.")
