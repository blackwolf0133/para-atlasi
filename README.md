# Para Atlası 🌍💰

Her gün saat **21:00**'de (Türkiye) farklı bir ülkenin para sözünü çöp adam çizimli, kendi sesinle anlatılan bir Reels videosu olarak Instagram'a otomatik paylaşan sistem (`@para_atlasi`). Altyapısı "Çöp Adamla Tarih" ile aynıdır.

- `episodes/` bölümler · `engine/` çizim ve video motoru · `daily.py` günlük akış · `publisher.py` Instagram paylaşımı
- `docs/senaryo_formati.md` format ve kurallar · `docs/konu_takvimi.md` söz takvimi
- Gizli kasa (Settings → Secrets → Actions): `IG_ACCESS_TOKEN`, `IG_USER_ID`, `VOICE_KEY`
- Bağlantı testi: Actions → Bağlantı testi · Deneme videosu: Actions → Günlük paylaşım → "Sadece videoyu üret"
- Ses: Pocket TTS Turkish (CC BY 4.0), sahibinin kendi ses kaydından klonlanır (`assets/voice/ref.wav.enc` şifreli)
