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
