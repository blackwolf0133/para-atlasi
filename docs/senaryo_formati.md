# KİM HAKLI? — senaryo formatı (24 Kasım 2026)

Eski @para_atlasi bu kanala dönüştü (kullanıcı kararı). İlham: @otomobil.oretiyorum (17 günde 113k, "Sol şerit,
kim haklı?" 39k ❤ / 1.471 yorum), @glassbox.tr ("yanlış bildiğin" kancası, 100k ❤), @sonrakibolum.tr ve
@karar.seninn (A/B yorum oylaması, canlı çizim). ALINAN sadece format. Onların konuları/metinleri ALINMAZ.

## Format (tek video, 35-45 sn)
1. Kanca (≤ 9 kelime): herkesin başına gelen an + rakam/şok. `kanca_yazi` ekranda ilk 3 sn.
2-4. Tartışma: A tarafı (kırmızı etiket, `"kim": "A"`), B tarafı (mavi, `"kim": "B"`), ortam gerilimi.
5. OYLAMA sahnesi: `"oylama": true, "ek_sure": 2.3` → "Sence kim haklı? … Üç saniye düşün." Ekranda KİM HAKLI? +
   A/B kutuları (`secim`) + 3-2-1.
6. "Cevap: … haklı." 7-8. Kural + KAYNAĞI (kanun/yönetmelik maddesi, kurum). 9. Pratik ipucu. 10. "Bunu … gönder."
Son kart: DOĞRU CEVAP (`dogru`: harf, metin ≤ 9 kelime, kaynak).

## DOĞRULUK (en önemli kural)
Cevap mevzuatta AÇIK olmalı (yönetmelik/kanun maddesi, Bakanlık açıklaması, Yargıtay içtihadı). En az 2 kaynak,
`kaynaklar` alanına URL. "Duruma göre değişir" olan, tartışmalı ya da yakında değişecek konular seçilmez.
Doğru cevap bazen A bazen B olmalı (hep "müşteri haklı" olmasın: örn. "iade süresi geçti, satıcı haklı").

## Konu havuzu
Tüketici (iade, garanti, kargo, fiyat etiketi, restoran), kira (depozito, zam, tahliye, aidat), trafik (geçiş üstünlüğü,
park, kaza tutanağı), iş hayatı (fazla mesai, yıllık izin, ihbar), komşuluk/apartman (gürültü, ortak alan, otopark),
banka/kart (kart aidatı, yetkisiz işlem), ulaşım (uçuş gecikmesi tazminatı), okul/veli…

## JSON
{"id":"006","slug":"…","title":"…","dizi_adi":"≤ 3 kelime","seed":24006,"kanca_yazi":"…",
 "taraflar":{"A":"Müşteri","B":"Kasiyer"},"characters":{"KISALTMA":"English visual description"},
 "secim":{"A":"Taraf: ≤ 6 kelime iddia","B":"…"},"dogru":{"harf":"A","metin":"…","kaynak":"…"},
 "gonder":"Bunu … birine gönder","scenes":[{"text":"…","prompt":"English, concrete, {KISALTMA}","kim":"A"}, …],
 "caption":"Kanca + durum. Emoji.","hashtags":["#kimhaklı","…"],"kaynaklar":["https://…"]}
`text`: sayılar yazıyla, kısa cümleler. `prompt`: İngilizce, somut, Türk günlük hayat ortamı; yazı/tabela metni YOK.
`caption`'a A/B satırı ve kaynak yazma (robot ekler). Müzik: engine/muzik_sec.py (Kevin MacLeod, CC BY 4.0).

## 26 Kasım: DİKKAT ÇEKEN KONU kuralları (kullanıcı isteği: "daha çok dikkat çeken konular")
İlk iki video: 001 market fiyatı (erişim 1), 002 kargo hasarı (103 erişim, 0 yorum). Ders: market/kargo gibi
"haklıyım ama umurumda değil" konuları yorum getirmiyor. İnsanların AİLESİYLE, PARASIYLA, EVİYLE, İŞİYLE kavga ettiği
ve "kesin ben haklıyım" dediği konular öne:
- Aile/para: düğün altınları, miras (kız-erkek kardeş), nişan hediyeleri, borç verilen para, aile evi.
- Ev: kiracı-ev sahibi (badana, depozito, habersiz giriş, aidat/demirbaş), komşu, apartman.
- İş: patron-çalışan (izin parası, ihbar, maaş kesintisi, fazla mesai — yalnızca net kurallı olanlar).
- Trafik: herkesin kavga ettiği net kurallar (dönel kavşak, sağdan gelen, fermuar sistemi…).
- "YANLIŞ BİLDİĞİN" bükümü en güçlüsü: çoğunluğun yanlış bildiği cevap (009 mağazada iade yok, 006 Yargıtay 2024
  değişikliği). Haftada en az iki bölüm böyle olsun; doğru cevap A/B dengeli kalsın.
- Kanca_yazi: kavga cümlesi ya da şok rakam ("Abi diyor ki: Baba evi erkek evladın"). Genel bilgi cümlesi DEĞİL.
