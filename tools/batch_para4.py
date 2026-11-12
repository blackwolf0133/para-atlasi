"""Para Atlası 13-17. bölümler (İspanya, Hindistan, Hollanda, İsveç, Polonya): "iki kişi" formatı."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAIL = "Her gün bir ülkenin para bilgeliği için takip et 🌍"
TOTAL = 30

def intro(say, pop1, pop2):
    return {"say": say, "text": say, "voice_delay": 1.0,
            "narrator": {"x": 0.5, "y": 0.97, "scale": 1.6, "pose": "wave", "face": "happy",
              "beats": [{"t": 0.45, "pose": "point", "face": "wink"}, {"f": 0.0, "pose": "hips", "face": "happy"},
                        {"f": 0.35, "pose": "think", "face": "think"}, {"f": 0.65, "pose": "open", "face": "surprised"}]},
            "emotion": "şaşkın",
            "props": [{"type": "pop", "text": pop1, "x": 0.27, "y": 0.15, "size": 120, "f": 0.0, "rot": -10, "until_f": 0.6},
                      {"type": "pop", "text": pop2, "x": 0.5, "y": 0.13, "size": 96, "f": 0.65, "rot": 5}]}

def quote(say, original, roman, tr):
    return {"say": say, "text": say, "bg": "vault", "actors": [],
            "props": [{"type": "quote", "original": original, "roman": roman, "tr": tr, "x": 0.5, "y": 0.5, "delay": 0.2}]}

def outro(country, n, nxt_say, nxt_pop):
    s = f"Bir sözü daha pasaportumuza bastık! Ülke {n} bitti. Yarın {nxt_say} gidiyoruz. Takip et, kaçırma!"
    s = s.replace(f"Ülke {n} bitti", "Otuz ülkeden " + ONES[n] + " tamam")
    return {"say": s, "text": s, "voice_delay": 0.5,
            "narrator": {"x": 0.5, "y": 0.97, "scale": 1.5, "pose": "open", "face": "happy",
              "beats": [{"f": 0.4, "pose": "point", "face": "happy"}, {"f": 0.75, "pose": "wave", "face": "wink"}]},
            "props": [{"type": "stamp", "text": country, "x": 0.8, "y": 0.17, "f": 0.12, "rot": -14, "scale": 0.8},
                      {"type": "pop", "text": f"ÜLKE {n} / {TOTAL}", "x": 0.74, "y": 0.7, "size": 70, "f": 0.3, "rot": 5},
                      {"type": "pop", "text": "YARIN: " + nxt_pop + "!", "x": 0.28, "y": 0.15, "size": 84, "f": 0.45, "rot": -6}]}
ONES = {13: "on üçüncüsü", 14: "on dördüncüsü", 15: "on beşincisi", 16: "on altıncısı", 17: "on yedincisi"}

def A(id, x, **kw):
    d = {"id": id, "x": x, "pose": "stand", "face": "neutral", "scale": 1.15}; d.update(kw); return d

def label(name, x):
    return {"type": "pop", "text": name, "x": x, "y": 0.27, "size": 56, "f": 0.0, "rot": 0}

def two(say, bg, left, right, props, emotion=None):
    d = {"say": say, "text": say, "bg": bg, "actors": [left, right], "props": props}
    if emotion: d["emotion"] = emotion
    return d

L = 0.25; R = 0.74
def wrong(id, **kw): return A(id, L, pose=kw.pop("pose", "shrug"), face=kw.pop("face", "sad"), scale=1.15, **kw)
def right(id, **kw): return A(id, R, pose=kw.pop("pose", "cheer"), face=kw.pop("face", "happy"), scale=1.15, flip=True, **kw)

def lesson(say, prop):
    return {"say": say, "text": say, "bg": "vault", "emotion": "sakin",
            "actors": [A("b", 0.32, pose="point", face="confident", scale=1.3)],
            "props": [prop, {"type": "sfx", "name": "rimshot", "f": 0.85}]}

def cap(hook, info, tags):
    return f"{hook}\n\n{info}\n\n{TAIL}\n\n{tags}"

EPS = []

# ------------------------------------------------------------ 013 İspanya
EPS.append(("013_ispanya", {"id": "013", "title": "Ayın Sonunda Bozulan Makine", "country": {"name": "İspanya", "code": "ES"},
 "caption": cap("Çamaşır makinesi hep ayın sonunda bozulur! 🇪🇸🧺",
  "\"Dinero llama dinero\": \"Para parayı çeker.\" Sözlüklerde İspanyolca atasözü olarak geçer. Kenarda parası olan, beklenmedik masrafta daha az öder: 6000 liralık makine peşin 6000, altı taksitle 7200 lira!",
  "#para #ispanya #atasözü #tasarruf #paraatlası"),
 "scenes": [
  intro("Çamaşır makinesi hep ayın sonunda bozulur, değil mi? İspanyolların buna karşı eski bir sözü var.", "İSPANYA!", "BOZULDU!"),
  quote("Dinero yama dinero. Yani: Para parayı çeker. Bu, İspanya'da bilinen bir atasözü.", "Dinero llama dinero", "", "Para parayı çeker."),
  two("Kenan'ın makinesi bozuldu. Yenisi 6000 lira. Kenarda parası yok, mağaza altı taksitle toplam 7200 lira yazdı.", "city",
      wrong("k"), right("s", pose="stand", face="neutral"),
      [label("KENAN", L), {"type": "pop", "text": "7200 TL", "x": 0.3, "y": 0.4, "size": 100, "f": 0.5, "rot": -6}]),
  two("Selin ise her ay biraz kenara koymuş. Makine bozulunca 6000 lirayı peşin ödedi ve işi bitirdi.", "bank",
      A("k", L, pose="stand", face="neutral"), right("s", pose="cheer", face="happy"),
      [label("SELİN", R), {"type": "pop", "text": "6000 TL", "x": 0.7, "y": 0.4, "size": 100, "f": 0.5, "rot": 6}]),
  two("Aradaki fark tam 1200 lira. Kenan bunu bahşiş sanmış. Mağaza da teşekkür etti!", "city",
      A("k", L, pose="shock", face="shock"), A("s", R, pose="hips", face="smug", flip=True),
      [{"type": "pop", "text": "FARK: 1200 TL", "x": 0.5, "y": 0.3, "size": 92, "f": 0.3, "rot": -4}], emotion="şaşkın"),
  lesson("Günün dersi: Kenarda para olan, zor günde daha az öder!", {"type": "piggy", "x": 0.74, "y": 0.83, "scale": 0.9}),
  outro("İspanya", 13, "Hindistan'a", "HİNDİSTAN")]}))

# ------------------------------------------------------------ 014 Hindistan
EPS.append(("014_hindistan", {"id": "014", "title": "Aylık Sadece 500 Lira Tuzağı", "country": {"name": "Hindistan", "code": "IN"},
 "caption": cap("Aylık sadece 500 lira diyen taksit, altı tane olunca ne olur? 🇮🇳🧵",
  "\"Jitni chadar, utne paon phailao\": \"Çarşafın kadar ayağını uzat.\" Hintçede ve Urducada bilinen bir atasözü; bizdeki \"yorganına göre ayağını uzat\" sözünün kuzeni. 6 taksit x 500 lira = ayda 3000 lira!",
  "#para #hindistan #atasözü #taksit #paraatlası"),
 "scenes": [
  intro("Aylık sadece 500 lira diyen taksit, altı tane olunca ne olur? Hintlilerin buna çarşaflı bir cevabı var!", "HİNDİSTAN!", "6 TAKSİT?!"),
  quote("Citni çadar, utne paon faylao. Yani: Çarşafın kadar ayağını uzat. Çadar, üstüne örttüğün çarşaf demek.", "Jitni chadar, utne paon phailao", "", "Çarşafın kadar ayağını uzat."),
  two("Ece her mağazada aylık sadece 500 lira dedi. Tam altı taksit aldı. Altı tane 500 lira, her ay 3000 lira eder.", "city",
      wrong("e", pose="shock", face="shock"), A("d", R, pose="stand", face="neutral", flip=True),
      [label("ECE", L), {"type": "pop", "text": "6 x 500 = 3000", "x": 0.35, "y": 0.4, "size": 80, "f": 0.5, "rot": -5}]),
  two("Deniz önce çarşafına baktı. Aylık en fazla 1000 lirayı taksite ayırabilirim dedi ve iki taksitte durdu.", "bank",
      A("e", L, pose="stand", face="neutral"), right("d", pose="point", face="confident"),
      [label("DENİZ", R), {"type": "pop", "text": "2 x 500 = 1000", "x": 0.65, "y": 0.4, "size": 80, "f": 0.5, "rot": 5}]),
  two("Deniz'in cebinde her ay 2000 lira daha fazla kalıyor. Ece'nin çarşafı kısa kaldı, ayakları dışarıda üşüyor!", "city",
      A("e", L, pose="sad", face="sad"), A("d", R, pose="hips", face="smug", flip=True),
      [{"type": "pop", "text": "AYDA 2000 TL FARK", "x": 0.5, "y": 0.3, "size": 76, "f": 0.3, "rot": -4}], emotion="şaşkın"),
  lesson("Günün dersi: Taksit küçük görünür ama toplamı büyük çıkar. Önce çarşafına bak!", {"type": "wallet", "x": 0.74, "y": 0.88, "scale": 0.9}),
  outro("Hindistan", 14, "Hollanda'ya", "HOLLANDA")]}))

# ------------------------------------------------------------ 015 Hollanda
EPS.append(("015_hollanda", {"id": "015", "title": "Günlük Kahve Tuzağı", "country": {"name": "Hollanda", "code": "NL"},
 "caption": cap("Günde bir kahve gibi görünür, yılda 29200 lira eder! 🇳🇱☕",
  "\"Zuinigheid met vlijt bouwt huizen als kastelen\": \"Tutumluluk ve çalışkanlık, evleri kale gibi yapar.\" Hollanda'da bilinen bir atasözü. Günde 80 liralık kahve yılda 29200, evden 20 liralık termos 7300 lira!",
  "#para #hollanda #atasözü #kahve #paraatlası"),
 "scenes": [
  intro("Günde bir kahve gibi görünür, ama yılda 29200 lira eder! Hollandalıların bunun için kaleli bir sözü var.", "HOLLANDA!", "KAHVE?!"),
  quote("Zöynihheyt met vleyt baut höyzen als kastelen. Yani: Tutumluluk ve çalışkanlık, evleri kale gibi yapar. Bu bir Hollanda atasözü.", "Zuinigheid met vlijt bouwt huizen als kastelen", "", "Tutumluluk ve çalışkanlık, evleri kale gibi yapar."),
  two("Jan her sabah 80 liralık kahveyi alıyor. Ayda 2400 lira, yılda tam 29200 lira.", "city",
      wrong("j", pose="relax", face="happy"), A("a", R, pose="stand", face="neutral", flip=True),
      [label("JAN", L), {"type": "pop", "text": "80 TL x 365", "x": 0.32, "y": 0.4, "size": 76, "f": 0.4, "rot": -5}]),
  two("Anna kahvesini evden termosla getiriyor. Tanesi 20 lira, yılda 7300 lira.", "bank",
      A("j", L, pose="stand", face="neutral"), right("a", pose="cheer", face="happy"),
      [label("ANNA", R), {"type": "pop", "text": "20 TL x 365", "x": 0.68, "y": 0.4, "size": 76, "f": 0.4, "rot": 5}]),
  two("Fark yılda tam 21900 lira! Jan'ın kahvesi sıcak ama cüzdanı buz gibi.", "city",
      A("j", L, pose="shock", face="shock"), A("a", R, pose="hips", face="smug", flip=True),
      [{"type": "pop", "text": "YILDA 21900 TL", "x": 0.5, "y": 0.3, "size": 84, "f": 0.3, "rot": -4}], emotion="şaşkın"),
  lesson("Günün dersi: Küçük günlük harcama, yıl sonunda kale gibi büyür!", {"type": "coins", "x": 0.74, "y": 0.93, "n": 4}),
  outro("Hollanda", 15, "İsveç'e", "İSVEÇ")]}))

# ------------------------------------------------------------ 016 İsveç
EPS.append(("016_isvec", {"id": "016", "title": "Üç Al İki Öde Tuzağı", "country": {"name": "İsveç", "code": "SE"},
 "caption": cap("Üç al iki öde afişini gören İsveçlilerin tek kelimelik bir cevabı var! 🇸🇪🛒",
  "\"Lagom är bäst\": \"Tam kararında olan en iyisidir.\" Lagom, ne az ne çok demek ve çevirisi zor bir İsveç kelimesi. 100 liralık şampuandan üç tane alıp 200 lira ödemek, ihtiyacın bir tane ise 100 lira fazla harcamaktır!",
  "#para #isveç #atasözü #indirim #paraatlası"),
 "scenes": [
  intro("Üç al, iki öde afişini gören İsveçlilerin tek kelimelik bir cevabı var. Hem de çevirisi bile zor bir kelime!", "İSVEÇ!", "3 AL 2 ÖDE?!"),
  quote("Lagom e best. Yani: Tam kararında olan en iyisidir. Lagom, ne az ne çok demek. İsveç'te çok bilinen bir söz.", "Lagom är bäst", "", "Tam kararında olan en iyisidir."),
  two("Lena üç al iki öde afişini görünce üç şampuan aldı. Tanesi 100 lira, toplam 200 lira ödedi ve 100 lira kazandım dedi.", "city",
      wrong("l", pose="cheer", face="happy"), A("e", R, pose="stand", face="neutral", flip=True),
      [label("LENA", L), {"type": "pop", "text": "3 AL 2 ÖDE", "x": 0.3, "y": 0.4, "size": 80, "f": 0.5, "rot": -5}]),
  two("Erik'in ise tek şampuana ihtiyacı vardı. Bir tane aldı, 100 lira ödedi ve yoluna devam etti.", "bank",
      A("l", L, pose="stand", face="neutral"), right("e", pose="point", face="confident"),
      [label("ERİK", R), {"type": "pop", "text": "1 TANE = 100 TL", "x": 0.66, "y": 0.4, "size": 66, "f": 0.5, "rot": 5}]),
  two("Lena 100 lira kazandığını sandı ama cebinden 100 lira fazla çıktı. Üç şampuan var, kafa ise tek!", "city",
      A("l", L, pose="shock", face="shock"), A("e", R, pose="hips", face="smug", flip=True),
      [{"type": "pop", "text": "100 TL FAZLA!", "x": 0.5, "y": 0.3, "size": 84, "f": 0.3, "rot": -4}], emotion="şaşkın"),
  lesson("Günün dersi: İhtiyacın yoksa bedava bile pahalıdır!", {"type": "goldbars", "x": 0.74, "y": 0.93, "scale": 0.95}),
  outro("İsveç", 16, "Polonya'ya", "POLONYA")]}))

# ------------------------------------------------------------ 017 Polonya
EPS.append(("017_polonya", {"id": "017", "title": "Üstü Kalsın Tuzağı", "country": {"name": "Polonya", "code": "PL"},
 "caption": cap("Üstü kalsın demek kolay, peki yılda kaç lira eder? 🇵🇱🐔",
  "\"Grosz do grosza, a będzie kokosza\": \"Kuruş kuruşa eklenir, tavuk olur.\" Polonya atasözü; grosz kuruş, kokosz ise eski dilde tavuk demek. Günde 7 lira bozuk para, yılda 2555 lira eder!",
  "#para #polonya #atasözü #bozukpara #paraatlası"),
 "scenes": [
  intro("Üstü kalsın deyince kimin cebine ne kadar gidiyor? Polonyalıların bozuk paraya tavuklu bir cevabı var!", "POLONYA!", "ÜSTÜ KALSIN?!"),
  quote("Groş do groşa, a bendje kokoşa. Yani: Kuruş kuruşa eklenir, tavuk olur. Groş, kuruş demek. Kokoşa ise eski dilde tavuk.", "Grosz do grosza, a będzie kokosza", "", "Kuruş kuruşa eklenir, tavuk olur."),
  two("Piotr her gün üstü kalsın diyor. Bozuk para ağır geliyor. Günde ortalama 7 lira bırakıyor.", "city",
      wrong("p", pose="relax", face="happy"), A("o", R, pose="stand", face="neutral", flip=True),
      [label("PIOTR", L), {"type": "pop", "text": "ÜSTÜ KALSIN", "x": 0.3, "y": 0.4, "size": 76, "f": 0.5, "rot": -5}]),
  two("Ola ise üstünü alıp akşam kavanoza atıyor. O da günde yine 7 lira.", "bank",
      A("p", L, pose="stand", face="neutral"), right("o", pose="cheer", face="happy"),
      [label("OLA", R), {"type": "piggy", "x": 0.72, "y": 0.83, "scale": 0.75}]),
  two("Bir yıl sonra Piotr'un 2555 lirası bahşiş olmuş. Ola'nın kavanozu ise 2555 lira dolu. Üstü kalsın demek kolay, üstüne üstlük pahalı!", "city",
      A("p", L, pose="shock", face="shock"), A("o", R, pose="hips", face="smug", flip=True),
      [{"type": "pop", "text": "YILDA 2555 TL", "x": 0.5, "y": 0.3, "size": 84, "f": 0.3, "rot": -4}], emotion="şaşkın"),
  lesson("Günün dersi: Bozuk para küçük görünür, ama sayarsan büyür!", {"type": "coins", "x": 0.74, "y": 0.93, "n": 4}),
  outro("Polonya", 17, "Yunanistan'a", "YUNANİSTAN")]}))

for name, ep in EPS:
    ep = {"id": ep["id"], "series": "PARA ATLASI", "title": ep["title"], "country": ep["country"],
          "voice_fx": {"pitch": 1.0, "noise": 0.2, "noise_w": 0.3}, "instagram_caption": ep["caption"], "scenes": ep["scenes"]}
    with open(os.path.join(ROOT, "episodes", name + ".json"), "w", encoding="utf-8") as f:
        json.dump(ep, f, ensure_ascii=False, indent=2)
    print("yazıldı", name)
