"""Para Atlası 18-24. bölümler (25-35 sn kısa yapı, kanca_yazi, "iki kişi" formatı)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAIL = "Her gün bir ülkenin para bilgeliği için takip et 🌍"
TOTAL = 30

def intro(say, pop1, pop2):
    return {"say": say, "text": say, "voice_delay": 0.4,
            "narrator": {"x": 0.5, "y": 0.97, "scale": 1.6, "pose": "wave", "face": "happy",
              "beats": [{"t": 0.45, "pose": "point", "face": "wink"}, {"f": 0.0, "pose": "hips", "face": "happy"},
                        {"f": 0.35, "pose": "think", "face": "think"}, {"f": 0.65, "pose": "open", "face": "surprised"}]},
            "emotion": "şaşkın",
            "props": [{"type": "pop", "text": pop1, "x": 0.27, "y": 0.15, "size": 120, "f": 0.0, "rot": -10, "until_f": 0.6},
                      {"type": "pop", "text": pop2, "x": 0.5, "y": 0.13, "size": 96, "f": 0.65, "rot": 5}]}

def quote(say, original, roman, tr):
    return {"say": say, "text": say, "bg": "vault", "actors": [],
            "props": [{"type": "quote", "original": original, "roman": roman, "tr": tr, "x": 0.5, "y": 0.5, "delay": 0.2}]}

def outro(country, n, send, nxt_say, nxt_pop):
    s = f"Ülke {n} tamam. Bunu {send} gönder. Yarın {nxt_say}!"
    return {"say": s, "text": s, "voice_delay": 0.3,
            "narrator": {"x": 0.5, "y": 0.97, "scale": 1.5, "pose": "open", "face": "happy",
              "beats": [{"f": 0.4, "pose": "point", "face": "happy"}, {"f": 0.75, "pose": "wave", "face": "wink"}]},
            "props": [{"type": "stamp", "text": country, "x": 0.8, "y": 0.17, "f": 0.12, "rot": -14, "scale": 0.8},
                      {"type": "pop", "text": f"ÜLKE {n} / {TOTAL}", "x": 0.74, "y": 0.7, "size": 70, "f": 0.3, "rot": 5},
                      {"type": "pop", "text": "YARIN: " + nxt_pop + "!", "x": 0.28, "y": 0.15, "size": 84, "f": 0.45, "rot": -6}]}

def A(id, x, **kw):
    d = {"id": id, "x": x, "pose": "stand", "face": "neutral", "scale": 1.15}; d.update(kw); return d

def label(name, x):
    return {"type": "pop", "text": name, "x": x, "y": 0.27, "size": 56, "f": 0.0, "rot": 0}

def two(say, bg, left, right, props, emotion=None):
    d = {"say": say, "text": say, "bg": bg, "actors": [left, right], "props": props}
    if emotion: d["emotion"] = emotion
    return d

L = 0.25; R = 0.74
def lesson(say, prop):
    return {"say": say, "text": say, "bg": "vault", "emotion": "sakin",
            "actors": [A("b", 0.32, pose="point", face="confident", scale=1.3)],
            "props": [prop, {"type": "sfx", "name": "rimshot", "f": 0.85}]}

def cap(hook, info, tags):
    return f"{hook}\n\n{info}\n\n{TAIL}\n\n{tags}"

def big(text, x=0.5, y=0.3, size=84, rot=-4, f=0.35):
    return {"type": "pop", "text": text, "x": x, "y": y, "size": size, "f": f, "rot": rot}

EPS = []

# 018 Yunanistan
EPS.append(("018_yunanistan", {"id": "018", "title": "Maaş Günü Fasulye Torbası", "country": {"name": "Yunanistan", "code": "GR"},
 "kanca": "Yunanlılar parayı fasulyeyle sayar!",
 "caption": cap("Yunanlılar parayı fasulyeyle sayar! 🇬🇷🫘",
  "\"Φασούλι το φασούλι γεμίζει το σακούλι\": \"Fasulye fasulye torba dolar.\" Yunan atasözü (Atina Akademisi atasözü arşivinde çok sayıda varyantı var). Maaş günü ilk iş ayda 500 lira ayıran, yılda 6000 lira biriktirir!",
  "#para #yunanistan #atasözü #maaşgünü #paraatlası"),
 "scenes": [
  intro("Yunanlılar parayı fasulyeyle sayar! Maaş neden hep 10 günde biter? Cevap bir torba fasulyede.", "YUNANİSTAN!", "FASULYE?!"),
  quote("Fasuli to fasuli, yemizi to sakuli. Yani: Fasulye fasulye, torba dolar. Yunanistan'da bilinen bir atasözü.", "Φασούλι το φασούλι γεμίζει το σακούλι", "", "Fasulye fasulye, torba dolar."),
  two("Eleni maaşı alınca harcıyor, kalan olursa biriktiririm diyor. Ay sonunda kalan hep sıfır.", "city",
      A("e", L, pose="shrug", face="sad"), A("n", R, pose="stand", face="neutral", flip=True),
      [label("ELENİ", L), big("KALAN: 0 TL", 0.3, 0.4, 80, -5, 0.5)]),
  two("Nikos maaş günü ilk iş 500 lirayı torbaya atıyor, kalanıyla yaşıyor. Yılda 6000 lira birikiyor.", "bank",
      A("e", L, pose="stand", face="neutral"), A("n", R, pose="cheer", face="happy", flip=True),
      [label("NİKOS", R), big("YILDA 6000 TL", 0.62, 0.4, 72, 5, 0.5), {"type": "piggy", "x": 0.72, "y": 0.83, "scale": 0.7}], emotion="şaşkın"),
  lesson("Günün dersi: Önce torbayı doldur, kalanı harca!", {"type": "coins", "x": 0.74, "y": 0.93, "n": 4}),
  outro("Yunanistan", 18, "maaşı hep erken biten arkadaşına", "İran'a", "İRAN")]}))

# 019 İran
EPS.append(("019_iran", {"id": "019", "title": "Hesabı Kuruşuna, İkramı Eşek Yüküne", "country": {"name": "İran", "code": "IR"},
 "kanca": "Hesabı kuruşuna, cömertliği eşek yüküyle!",
 "caption": cap("İranlılar hesabı kuruşuna yapar, ikramı eşek yüküyle! 🇮🇷🫖",
  "\"Hesâb be dinâr, bakhshesh be kharvâr\": \"Hesap kuruşu kuruşuna, bağış eşek yükü kadar.\" Farsça atasözü; kharvar eski bir ağırlık ölçüsü, kabaca bir eşek yükü. Ayda 600 lira artıranın ikramı da büyük olur!",
  "#para #iran #atasözü #bütçe #paraatlası"),
 "scenes": [
  intro("İranlılar hesabı kuruşuna yapar ama ikramı eşek yüküyle yapar! Nasıl oluyor bu?", "İRAN!", "EŞEK YÜKÜ?!"),
  quote("Hesab be dinar, bahşeş be harvar. Yani: Hesap kuruşu kuruşuna, bağış eşek yükü kadar. Harvar, eşek yükü demek.", "Hesâb be dinâr, bakhshesh be kharvâr", "", "Hesap kuruşu kuruşuna, bağış eşek yükü kadar."),
  two("Ali hesap tutmuyor. Ay sonu cüzdanı boş, arkadaşına ısmarlayacak bir çayı bile yok.", "city",
      A("a", L, pose="shrug", face="sad"), A("r", R, pose="stand", face="neutral", flip=True),
      [label("ALİ", L), big("CÜZDAN: 0 TL", 0.3, 0.4, 76, -5, 0.5)]),
  two("Reza her harcamayı yazıyor. Ayda 600 lira artıyor ve bunu sevdiklerine ikram ediyor.", "bank",
      A("a", L, pose="stand", face="neutral"), A("r", R, pose="cheer", face="happy", flip=True),
      [label("REZA", R), big("AYDA 600 TL", 0.65, 0.4, 76, 5, 0.5)], emotion="şaşkın"),
  lesson("Günün dersi: Cömert olmak için önce hesabı bilmek gerekir!", {"type": "wallet", "x": 0.74, "y": 0.88, "scale": 0.9}),
  outro("İran", 19, "hep ısmarlayıp ay sonu batan arkadaşına", "Meksika'ya", "MEKSİKA")]}))

# 020 Meksika
EPS.append(("020_meksika", {"id": "020", "title": "Borç Verince Giden İki Şey", "country": {"name": "Meksika", "code": "MX"},
 "kanca": "Borç verince hem para hem arkadaş gider?",
 "caption": cap("Arkadaşa borç verince hem para gider hem arkadaş mı? 🇲🇽🌮",
  "\"Cuentas claras, amistades largas\": \"Hesaplar net olursa dostluklar uzun olur.\" Meksika'da çok kullanılan bir halk sözü. Borcun tarihini baştan konuşmak, 2000 liranın yanında dostluğu da korur!",
  "#para #meksika #atasözü #borç #paraatlası"),
 "scenes": [
  intro("Arkadaşa borç verince hem para gider hem arkadaş! Meksikalıların buna karşı kısa bir sözü var.", "MEKSİKA!", "BORÇ?!"),
  quote("Kuentas klaras, amistades largas. Yani: Hesaplar net olursa dostluklar uzun olur. Meksika'da çok bilinen bir söz.", "Cuentas claras, amistades largas", "", "Hesaplar net olursa dostluklar uzun olur."),
  two("Mert arkadaşına 2000 lira verdi ama ne zaman vereceksin diye sormadı. Üç ay sonra birbirlerine bakamıyorlar.", "city",
      A("m", L, pose="shrug", face="sad"), A("d", R, pose="stand", face="neutral", flip=True),
      [label("MERT", L), big("2000 TL", 0.3, 0.4, 90, -5, 0.5)]),
  two("Deniz 2000 lirayı verirken tarihi birlikte yazdı. Cuma günü para geri geldi, çay da ısmarlandı.", "bank",
      A("m", L, pose="stand", face="neutral"), A("d", R, pose="cheer", face="happy", flip=True),
      [label("DENİZ", R), big("CUMA: GERİ", 0.65, 0.4, 76, 5, 0.5)], emotion="şaşkın"),
  lesson("Günün dersi: Net hesap dostluğu bozmaz, korur!", {"type": "piggy", "x": 0.74, "y": 0.83, "scale": 0.9}),
  outro("Meksika", 20, "borç verip sesini çıkaramayan arkadaşına", "Güney Afrika'ya", "GÜNEY AFRİKA")]}))

# 021 Güney Afrika
EPS.append(("021_guney_afrika", {"id": "021", "title": "Yarı Fiyatına Pahalı Ayakkabı", "country": {"name": "Güney Afrika", "code": "ZA"},
 "kanca": "Yarı fiyatına aldığın ayakkabı neden pahalıya patlar?",
 "caption": cap("Yarı fiyatına aldığın ayakkabı neden pahalıya patlar? 🇿🇦👟",
  "\"Goedkoop koop is duurkoop\": \"Ucuza alan pahalıya almış olur.\" Afrikaans dilinde bir atasözü; Güney Afrika'da kullanılan dillerden biri. 300 liralık ayakkabıdan yılda dört çift, 1200 lira eder!",
  "#para #güneyafrika #atasözü #indirim #paraatlası"),
 "scenes": [
  intro("Yarı fiyatına aldığın ayakkabı neden pahalıya patlar? Güney Afrika'da bunun tek kelimelik adı var.", "G. AFRİKA!", "PAHALIYA PATLAR?!"),
  quote("Hutkoop koop is dürkoop. Yani: Ucuza alan, pahalıya almış olur. Bu bir Afrikaans atasözü.", "Goedkoop koop is duurkoop", "", "Ucuza alan, pahalıya almış olur."),
  two("Zola 300 liralık ayakkabıyı kaptı. Üç ayda tabanı gitti. Yılda dört çift, toplam 1200 lira.", "city",
      A("z", L, pose="shock", face="shock"), A("t", R, pose="stand", face="neutral", flip=True),
      [label("ZOLA", L), big("YILDA 1200 TL", 0.35, 0.4, 72, -5, 0.5)]),
  two("Thabo 900 liralık sağlam bir çift aldı. Bir yıl sonra hâlâ yürüyor. Yılda 900 lira.", "bank",
      A("z", L, pose="sad", face="sad"), A("t", R, pose="cheer", face="happy", flip=True),
      [label("THABO", R), big("YILDA 900 TL", 0.65, 0.4, 72, 5, 0.5)], emotion="şaşkın"),
  lesson("Günün dersi: Ucuz olan değil, uzun giden ucuzdur!", {"type": "goldbars", "x": 0.74, "y": 0.93, "scale": 0.95}),
  outro("Güney Afrika", 21, "indirim görünce kendini tutamayan arkadaşına", "Vietnam'a", "VİETNAM")]}))

# 022 Vietnam
EPS.append(("022_vietnam", {"id": "022", "title": "Önce Para, Sonra Çorba", "country": {"name": "Vietnam", "code": "VN"},
 "kanca": "Önce para, sonra çorba!",
 "caption": cap("Vietnamlılar veresiyeye çorbayla cevap verir! 🇻🇳🍜",
  "\"Tiền trao cháo múc\": \"Para uzanınca çorba kepçelenir.\" Vietnamca bir deyim: parayı verir, malı hemen alırsın. Kartla sonra öderim diyen kişi ay sonunda 2400 lira ekstreyle karşılaşabilir!",
  "#para #vietnam #atasözü #kredikartı #paraatlası"),
 "scenes": [
  intro("Vietnamlılar veresiyeye çorbayla cevap verir! Önce para, sonra çorba.", "VİETNAM!", "ÖNCE PARA!"),
  quote("Tiyen çao çaw muk. Yani: Para uzanır, çorba kepçelenir. Vietnam'da çok bilinen bir deyim.", "Tien trao chao muc", "", "Para uzanır, çorba kepçelenir."),
  two("Linh market parasını kartla ödüyor, ay sonu bakarım diyor. Ay sonunda ekstrede 2400 lira çıkıyor.", "city",
      A("l", L, pose="shock", face="shock"), A("m", R, pose="stand", face="neutral", flip=True),
      [label("LİNH", L), big("EKSTRE: 2400 TL", 0.35, 0.4, 66, -5, 0.5)]),
  two("Minh cüzdanına 1500 lira koyuyor. Para uzanır, çorba gelir. Bitince alışveriş de biter.", "bank",
      A("l", L, pose="sad", face="sad"), A("m", R, pose="cheer", face="happy", flip=True),
      [label("MİNH", R), big("CÜZDAN: 1500 TL", 0.65, 0.4, 62, 5, 0.5)], emotion="şaşkın"),
  lesson("Günün dersi: Parayı elinle uzatınca harcamayı hissedersin!", {"type": "wallet", "x": 0.74, "y": 0.88, "scale": 0.9}),
  outro("Vietnam", 22, "sürekli sonra öderim diyen arkadaşına", "Tayland'a", "TAYLAND")]}))

# 023 Tayland
EPS.append(("023_tayland", {"id": "023", "title": "Fil Gibi Tuvalete Gitme", "country": {"name": "Tayland", "code": "TH"},
 "kanca": "Fili görüp onun gibi tuvalete gitme!",
 "caption": cap("Tayland'da fili görüp onun gibi tuvalete gitme diye bir söz var! 🇹🇭🐘",
  "\"เห็นช้างขี้ ขี้ตามช้าง\" (Hen cháang khîi, khîi dtaam cháang): \"Fil tuvalete gitti diye sen de onun gibi gitme.\" Tayland atasözü, başkasına özenip gücünü aşmak anlamında. 40000 liralık telefonu 12 taksitle almak ayda 3333 lira eder!",
  "#para #tayland #atasözü #özenmek #paraatlası"),
 "scenes": [
  intro("Tayland'da fili görüp onun gibi tuvalete gitme diye bir söz var! Ama mesele aslında cüzdan.", "TAYLAND!", "FİL?!"),
  quote("Hen çaang ki, ki taam çaang. Yani: Fil tuvalete gitti diye sen de onun gibi gitme. Başkasına özenip gücünü aşma demek.", "Hen cháang khîi, khîi dtaam cháang", "", "Fil tuvalete gitti diye sen de gitme."),
  two("Pim arkadaşları gibi 40000 liralık telefon aldı. Maaşı 20000 lira ve taksit ayda 3333 lira.", "city",
      A("p", L, pose="shock", face="shock"), A("c", R, pose="stand", face="neutral", flip=True),
      [label("PİM", L), big("AYDA 3333 TL", 0.33, 0.4, 72, -5, 0.5)]),
  two("Chai ise eski telefonla devam ediyor. Ekranı çatlak ama cüzdanı sapasağlam.", "bank",
      A("p", L, pose="sad", face="sad"), A("c", R, pose="cheer", face="happy", flip=True),
      [label("CHAİ", R), big("TAKSİT: 0 TL", 0.65, 0.4, 72, 5, 0.5)], emotion="şaşkın"),
  lesson("Günün dersi: Fil ne yaparsa yapsın, sen kendi gücüne göre git!", {"type": "coins", "x": 0.74, "y": 0.93, "n": 4}),
  outro("Tayland", 23, "hep özenip taksite giren arkadaşına", "Endonezya'ya", "ENDONEZYA")]}))

# 024 Endonezya
EPS.append(("024_endonezya", {"id": "024", "title": "Şemsiye Yağmurdan Önce Alınır", "country": {"name": "Endonezya", "code": "ID"},
 "kanca": "Yağmur başlayınca şemsiye neden hep pahalı?",
 "caption": cap("Yağmur başlayınca şemsiye neden hep pahalı? 🇮🇩☔",
  "\"Sedia payung sebelum hujan\": \"Yağmurdan önce şemsiyeni hazırla.\" Endonezya ve Malay dünyasında çok bilinen bir atasözü. Ayda 400 lira ayıran, beş ayda 2000 liralık acil masrafa hazır olur!",
  "#para #endonezya #atasözü #acilfon #paraatlası"),
 "scenes": [
  intro("Yağmur başlayınca şemsiye neden hep pahalı? Endonezyalıların buna karşı şemsiyeli bir sözü var.", "ENDONEZYA!", "YAĞMUR!"),
  quote("Sediya payung sebelum hucan. Yani: Yağmurdan önce şemsiyeni hazırla. Endonezya'da çok bilinen bir söz.", "Sedia payung sebelum hujan", "", "Yağmurdan önce şemsiyeni hazırla."),
  two("Rina ayda 400 lirayı şemsiye kutusuna atıyor. Beş ayda 2000 lira birikti. Lastik patlayınca ödeyip yoluna devam etti.", "city",
      A("r", L, pose="cheer", face="happy"), A("b", R, pose="stand", face="neutral", flip=True),
      [label("RİNA", L), big("KUTU: 2000 TL", 0.33, 0.4, 70, -5, 0.5)]),
  two("Budi hiç ayırmamış. Aynı lastik 2000 lira çıkınca borç aldı, o ay yemekten kıstı.", "bank",
      A("r", L, pose="stand", face="neutral"), A("b", R, pose="shock", face="shock", flip=True),
      [label("BUDİ", R), big("KUTU: 0 TL", 0.65, 0.4, 72, 5, 0.5)], emotion="şaşkın"),
  lesson("Günün dersi: Şemsiye yağmurdan önce satın alınır!", {"type": "piggy", "x": 0.74, "y": 0.83, "scale": 0.9}),
  outro("Endonezya", 24, "acil masraf gelince ağlayan arkadaşına", "Arjantin'e", "ARJANTİN")]}))

for name, ep in EPS:
    out = {"id": ep["id"], "series": "PARA ATLASI", "title": ep["title"], "country": ep["country"],
           "kanca_yazi": ep["kanca"],
           "voice_fx": {"pitch": 1.0, "noise": 0.2, "noise_w": 0.3}, "instagram_caption": ep["caption"], "scenes": ep["scenes"]}
    with open(os.path.join(ROOT, "episodes", name + ".json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    words = sum(len(s["say"].split()) for s in ep["scenes"])
    print("yazıldı", name, words, "kelime", len(ep["kanca"].split()), "kanca kelime")
