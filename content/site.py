# arazi.app — Turkish site for Field Area Measure ("Arazi Ölçme" on Google Play TR). English site: fieldareameasure.com.
# Keep true: measure by tapping corners on a satellite map; area + perimeter; units m², km², ha, akre, ft², yd²
# (dönüm comes from the converter on this site, not from the app); history; PDF report; Site Analysis (Android first).

SITE = "https://arazi.app"
BRAND = "Arazi Ölçme"
APP_ID = "6740893569"
PLAY_ID = "com.asilarslan.fieldarea"
LANGS = ["tr"]
SISTER = {"en": "https://fieldareameasure.com/"}
RATING = {"value": 4.9, "count": 14, "label": "App Store Türkiye'de 4,9 · 14 değerlendirme"}

HOME = {
    "tr": {
        "name": "Türkçe", "locale": "tr_TR", "badge": "tr-tr", "play": "tr", "brand": "Arazi Ölçme",
        "title": "Arazi Ölçme: Tarla ve Arsa Alanını Uydu Haritasında Ölçün (m², Dönüm, Hektar)",
        "desc": "Tarlanızın veya arsanızın köşelerine uydu haritasında dokunun, alanı ve çevreyi saniyeler içinde görün. Ölçümleri kaydedin, PDF rapor alın, arsanızın güneşini ve eğimini analiz edin. iPhone ve Android.",
        "nav": {"tool": "Dönüm hesaplama", "guides": "Rehberler", "get": "Uygulamayı indir"},
        "kicker": "iPhone ve Android için arazi ölçüm uygulaması",
        "h1": "Tarlanızı, arsanızı telefondan ölçün.",
        "sub": "Uydu haritasında köşelere dokunun; alanı ve çevreyi anında metrekare, hektar veya akre olarak görün. Ardından arsanızın güneşini, eğimini ve evin nereye sığacağını inceleyin.",
        "compat": "Ücretsiz denenir · iPhone ve iPad · Android · Türkçe",
        "qr": "Uygulamayı indirmek için telefon kameranızla okutun",
        "hero_alt": "Arazi Ölçme uygulamasında uydu haritası üzerinde tarla ölçümü",
        "stats": [("6", "alan birimi"), ("4", "arsa analizi aracı"), ("PDF", "ölçüm raporu"), ("20", "dil")],
        "kick": {"measure": "Ölçüm", "site": "Arsa analizi", "how": "Nasıl çalışır", "tool": "Ücretsiz araç", "guides": "Rehberler", "faq": "Sık sorulanlar"},
        "measure_h2": "Alan ve çevre saniyeler içinde",
        "measure_lead": "Sınırı yürümeye, şerit metreye gerek yok. Tarlayı haritada bulun, köşelerine dokunun, sonucu okuyun.",
        "measure_points": [
            ("Dokunun ya da nişan alın", "Köşe eklemek için haritaya dokunun ya da artı işaretini hedefe getirip + tuşuna basın. Köşeleri sürükleyerek düzeltin."),
            ("Her kenar ölçülü", "Her kenarın uzunluğu yazılır; alan ve çevre siz çizdikçe güncellenir."),
            ("İstediğiniz birim", "Metrekare, kilometrekare, hektar, akre, fit kare veya yarda kare. Dönüm için sitedeki hesaplayıcıyı kullanın."),
        ],
        "keep_h2": "Her ölçüm saklanır",
        "keep_lead": "Tarlalarınıza ad verin, aramayla bulun, Haritalar'da açıp yol tarifi alın ve PDF rapor olarak paylaşın.",
        "site_h2": "Ev mi yapacaksınız? Arsayı analiz edin.",
        "site_lead": "Arsa Analizi, ölçtüğünüz arsayı almadan ya da proje çizdirmeden önce gereken cevaplara dönüştürür.",
        "site_note": "Arsa Analizi Android'de yayında; iPhone sürümü yolda.",
        "site_tabs": [
            ("Güneş", "Yaz ve kış güneşinin arsanız üzerindeki yolu, öğle güneşi yüksekliği ve yazın gölge yapıp kışın güneşi içeri alan saçak derinliği."),
            ("Yerleşim", "Sokak tarafını seçin, ön ve yan bahçe mesafelerini ve taban alanı oranını girin; yapılaşma alanını örnek bir planla görün."),
            ("Eğim", "Yaklaşık arazi verisi ya da kendi köşe kotlarınızla eğim, eğim yönü ve sokaktan kapıya kaç basamak olduğu."),
            ("Karne", "Tek sayfalık arsa karnesi: güneş, yer, kot, manzara ve varış."),
        ],
        "how_h2": "Nasıl çalışır",
        "steps": [("Yeri bulun", "Haritada arayın ya da konumunuza gidin."), ("Köşeleri işaretleyin", "Tarlanın, arsanın ya da çatının her köşesine dokunun."),
                  ("Kaydedin, paylaşın", "Ad verin, kaydedin, PDF rapor alın ya da arsa analizini açın.")],
        "who_h2": "Kimler için",
        "who": [("Çiftçiler", "Tohum, gübre ve ilaçlama için tarla alanı."), ("Alıcılar ve satıcılar", "Arsayı görmeye gitmeden büyüklüğünü kontrol edin."),
                ("Mimarlar ve müteahhitler", "Ön projede çekme mesafesi, güneş ve eğim."), ("Bahçe ve peyzaj", "Çim, tarh ve çit hesabı.")],
        "tool_h2": "Dönüm, metrekare, hektar çevirmeniz mi gerekiyor?",
        "tool_p": "Ücretsiz dönüm hesaplayıcımız: herhangi bir birime değer yazın, diğerlerini hemen görün.",
        "tool_btn": "Dönüm hesaplayıcıyı aç",
        "guides_h2": "Arazi ve arsa rehberleri",
        "faq_h2": "Sık sorulanlar",
        "faq": [
            ("Ölçüm ne kadar doğru?", "Yerleştirdiğiniz köşeler ve uydu görüntüsü kadar doğrudur; çoğu tarla ve arsada fark birkaç yüzde içinde kalır. Tapu ve resmî işlemler için lisanslı harita mühendisinin ölçümü esastır."),
            ("Ücretsiz mi?", "Ücretsiz deneyebilirsiniz. Haftalık veya yıllık abonelik sınırsız ölçüm, geçmiş ve rapor açar; mağaza ayarlarından istediğiniz zaman iptal edebilirsiniz."),
            ("Uygulama dönüm gösteriyor mu?", "Uygulama metrekare, kilometrekare, hektar, akre, fit kare ve yarda kare gösterir. 1 dönüm 1.000 m² olduğundan metrekareden kolayca çevrilir; sitedeki dönüm hesaplayıcı da bunu yapar."),
            ("GPS ile tarlayı dolaşmam gerekiyor mu?", "Hayır. Konumunuz haritada gösterilir; ölçümü uydu haritasında köşeleri işaretleyerek yaparsınız."),
            ("Android'de var mı?", "Evet. Google Play'de “Arazi Ölçme”, App Store'da “Fields Area Measure” adıyla yer alıyor."),
        ],
        "cta_h2": "Arazinizi bir dakikada ölçün", "cta_p": "iPhone ve Android'de ücretsiz deneyin.",
        "footer_app": "Uygulama", "footer_guides": "Rehberler", "footer_legal": "Yasal", "support": "Destek",
        "privacy": "Gizlilik Politikası", "terms": "Kullanım Koşulları", "copyright": "Arazi Ölçme · Field Area Measure",
        "sticky": "Arazini ücretsiz ölç", "home": "Ana sayfa", "guides_hub": "Rehberler", "related": "İlgili rehberler", "updated": "Güncelleme",
        "inline_cta": "Kendi tarlanızın alanını mı merak ediyorsunuz? Arazi Ölçme'de köşelerine dokunun, sonucu saniyeler içinde görün.",
        "shots_alt": {"measure": "Uydu haritasında tarla ölçümü", "detail": "Kaydedilmiş arsa, alan ve çevre", "list": "Kaydedilmiş ölçümler listesi",
                      "site0": "Arsa üzerinde güneşin yolu", "site1": "Yapılaşma alanı ve örnek yerleşim", "site2": "Eğim ve sokaktan basamak sayısı",
                      "site3": "Arsa karnesi"},
        "back": "Ana sayfaya dön",
    },
}
