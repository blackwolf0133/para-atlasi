# Para Atlası — Bölüm Senaryo Formatı

Dosya: `episodes/NNN_ulke.json`. Sıradaki (paylaşılmamış, en küçük numara) bölüm her gün 21:00'de paylaşılır.
Tarih kanalından teknik fark: tema (zümrüt yeşili + altın), anlatıcı **Kuruş** (sikke kafalı), sahnelerde `quote` söz kartı ve `stamp` pasaport damgası.

## Üst alanlar
`id`, `series` ("PARA ATLASI"), `title` (dikkat çekici, ~35 karakter), `country` {"name": "Japonya", "code": "JP"},
`voice_fx` (yalnızca yedek Piper sesi için: {"pitch":1.0,"noise":0.2,"noise_w":0.3}),
`instagram_caption` (kanca + 2-3 cümle bilgi + yorum sorusu + "Her gün bir ülkenin para bilgeliği için takip et 🌍" + **TAM 5 etiket**, sonuncusu #paraatlası)

Bayrak kodları: JP KR DE RU TR CN US GB FR IT ES BR IN NL SE FI DK NO GR EG MX AT HU PL UA IE ID. Listede olmayan kodda bayrak yerine kod yazısı çıkar (yeni bayrak eklemek için engine/props_para.py → draw_cflag).

## Bölüm yapısı (6-7 sahne, 40-55 sn, ton: bilge + hafif esprili)
1. **Giriş** (Kuruş, `narrator`): ülke + şaşırtıcı kanca, `"emotion":"şaşkın"`
2. **Söz kartı** (`quote`): orijinal söz + okunuş + Türkçesi. `say` kısmında sözü **Türkçe okunuşla** yaz (ses modeli yabancı yazıyı okuyamaz).
3-4. **Açıklama sahneleri:** anlamı ve kullanımı, örnek bir durum, hafif bir espri
5. **Günün dersi** (`"emotion":"sakin"`, rimshot sfx)
6. **Kapanış** (Kuruş): pasaport damgası (`stamp`) + "Yarın: <sonraki ülke>" pop yazısı. Sonraki ülke, takvimdeki sıradaki ülke olmalı.

## Sahne alanları ve nesneler
`say` (okunacak; yıllar ve sayılar rakamla, noktasız: 36500), `text` (altyazı), `bg` (`vault` `city` `bank`), `emotion` (`şaşkın` `sakin` `mutlu`), `voice_delay`, `actors`, `props`.
- actors: tarih kanalındaki alanlar aynı (`pose` `face` `hat` `scale` `flip` `pose2` `face2` `switch` `anim` `holds`)
- props: `quote` `stamp` `cflag` `coin` `coins` `banknote` (symbol) `wallet` (empty) `piggy` `goldbars` `globe` + `pop` `bubble` `bulb` `sfx`
- Zamanlama: `delay` (sn) ya da `f` (konuşmanın oranı)
- Yazı tipleri: Latin, Japonca, Korece, Kiril otomatik. Arapça/İbranice için DejaVu kullanılır (sağdan sola yazım için kartı kontrol et!).

## Doğruluk kuralları
- Söz, anlam ve ülkeyi en az 2 kaynaktan doğrula (sözlük, atasözü derlemesi, ders kaynağı).
- Yaşı/tarihi belli olmayan sözlere "yüzyıllardır" deme; kaynak neyse onu söyle.
- Din, siyaset ve ırkla ilgili şaka yapma. Ülkeleri ve insanları aşağılama.
- Maaş/yatırım tavsiyesi verme; yatırım sözünü sadece söz olarak anlat.

## Haftalık trend raporu (last30days)
Her pazartesi blackwolf0133/cop-adamla-tarih deposundaki "Trend araştırma" iş akışı son 30 günün trendlerini 6 kanal için tarar
(YouTube, Reddit vb.; SCRAPECREATORS anahtarı varsa Instagram ve TikTok da). Yeni bölüm yazmadan önce en yeni raporu oku:

```bash
TAG=$(gh api "repos/blackwolf0133/cop-adamla-tarih/releases?per_page=20" --jq '[.[]|select(.tag_name|startswith("trend-"))][0].tag_name')
ID=$(gh api "repos/blackwolf0133/cop-adamla-tarih/releases/tags/$TAG" --jq '.assets[]|select(.name=="para.md").id')
gh api -H "Accept: application/octet-stream" "repos/blackwolf0133/cop-adamla-tarih/releases/assets/$ID" > /tmp/trend.md
```
Bu kanalın dosyası: **para.md**. Rapordaki tutan kanca kalıplarını, konu açılarını ve formatları kendi kurallarımıza uyarlayarak kullan;
başka içerik üreticilerinin metnini, videosunu ya da hikâyesini kopyalama. Rapor yoksa ya da eskiyse (14 günden eski) bu adımı atla.

---

## 13 Kasım: İLK 3 SANİYE kuralları (ZORUNLU, diğer kurallarla çelişirse bu geçerli)

Veri: 8 kanalda izleyici ortalama 5-13 sn'de kaydırıyor. Instagram videoyu önce küçük bir test grubuna gösteriyor; izlenme süresi, sona kadar izlenme ve DM ile gönderilme iyi değilse yaymıyor. Reels izleyicisi ~1,4 sn'de karar veriyor ve izlemelerin yarısından fazlası ses kapalı başlıyor.

**Motor ne yapıyor (otomatik):** 0. saniyede ekranda büyük kanca yazısı (~3 sn) + ilk 0,8 sn hızlı zoom. Yazı bölümdeki `"kanca_yazi"` alanından gelir; yoksa açıklamanın (caption / instagram_caption) ilk satırından, o da uzunsa ilk cümlesinden. Bu yüzden:
- Her bölüme `"kanca_yazi"` ekle: en fazla 8 kelime, sessizken tek başına merak uyandıran cümle (cevabı vermeden). Seslendirilen ilk cümleyle aynı olmak zorunda değil ama aynı merakı açsın. (Son Mola'da bu alan sahne içindedir ve 2-3 kelimedir; orada mevcut kural geçerli.)
- Açıklamanın ilk satırı da kısa ve merak uyandıran olsun (yedek kanca yazısı olarak kullanılıyor).

**Kanca puanlama (yazdıktan sonra her bölüm için):** İlk seslendirilen cümleyi ve kanca_yazi'yi şu 5 türe göre 1-5 puanla, kendine sor: "Akışta kaydırırken 1,5 sn'de durur muydum?"
1. Ortak dert: izleyicinin yaşadığı ama dile getirmediği bir sıkıntı (Reels'te en güçlüsü)
2. Merak boşluğu: kapanması için izlemek gereken bir soru/boşluk
3. İddialı/ters köşe cümle: doğru ama şaşırtıcı, karşı çıkılası bir iddia
4. Kalıp kırma: beklenmedik bir giriş
5. Görsel şok: ilk karede açıklama isteyen bir görüntü
En yüksek puan 4'ün altındaysa ilk cümleyi yeniden yaz. Selamlama, giriş, "bugün size … anlatacağım", tarih/yer ile başlamak YASAK; en çarpıcı an ilk cümlede. Doğruluk kuralları aynen geçerli (abartı/uydurma yok).

**Gönderilme (DM) sebebi:** Instagram'da yeni kişilere ulaştıran en güçlü sinyal videonun DM ile birine gönderilmesi. Her bölümün SON seslendirilen cümlesi (ya da kapanış kartı alt yazısı), izleyicinin videoyu belirli birine göndermesi için doğal bir sebep versin; TEK cümle, dilenmeden: "Bunu her ay sonu batan arkadaşına gönder.", "Bunu gece yolculuğu seven birine gönder." Açıklamadaki tek çağrı kuralı aynen kalır (bu cümle videonun içinde).
