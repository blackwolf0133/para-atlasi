"""Para Atlası 6-12. bölümler (Mısır, Brezilya, ABD, İngiltere, İtalya, Çin, Fransa)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAIL = "Her gün bir ülkenin para bilgeliği için takip et 🌍"

def intro(say, pop1, pop2):
    return {"say": say, "text": say, "voice_delay": 1.0,
            "narrator": {"x": 0.5, "y": 0.97, "scale": 1.6, "pose": "wave", "face": "happy",
              "beats": [{"t": 0.45, "pose": "point", "face": "wink"}, {"f": 0.0, "pose": "hips", "face": "happy"},
                        {"f": 0.35, "pose": "think", "face": "think"}, {"f": 0.65, "pose": "open", "face": "surprised"}]},
            "emotion": "şaşkın",
            "props": [{"type": "pop", "text": pop1, "x": 0.27, "y": 0.15, "size": 120, "f": 0.0, "rot": -10, "until_f": 0.6},
                      {"type": "pop", "text": pop2, "x": 0.5, "y": 0.13, "size": 96, "f": 0.65, "rot": 5}]}

def quote(say, text, original, roman, tr):
    return {"say": say, "text": text, "bg": "vault", "actors": [],
            "props": [{"type": "quote", "original": original, "roman": roman, "tr": tr, "x": 0.5, "y": 0.5, "delay": 0.2}]}

def outro(country, nxt, pop):
    s = f"Bir sözü daha pasaportumuza bastık! Yarın {nxt} gidiyoruz. Takip et, kaçırma!"
    return {"say": s, "text": s, "voice_delay": 0.5,
            "narrator": {"x": 0.5, "y": 0.97, "scale": 1.5, "pose": "open", "face": "happy",
              "beats": [{"f": 0.4, "pose": "point", "face": "happy"}, {"f": 0.75, "pose": "wave", "face": "wink"}]},
            "props": [{"type": "stamp", "text": country, "x": 0.8, "y": 0.17, "f": 0.12, "rot": -14, "scale": 0.8},
                      {"type": "pop", "text": "YARIN: " + pop + "!", "x": 0.28, "y": 0.15, "size": 84, "f": 0.45, "rot": -6}]}

def lesson(say, prop):
    return {"say": say, "text": say, "bg": "vault", "emotion": "sakin",
            "actors": [A("b", 0.32, pose="point", face="confident", scale=1.3)],
            "props": [prop, {"type": "sfx", "name": "rimshot", "f": 0.85}]}

def joke(say, actor, pop, popx=0.68):
    return {"say": say, "text": say, "bg": "city", "emotion": "şaşkın", "actors": [actor],
            "props": [{"type": "pop", "text": pop, "x": popx, "y": 0.28, "size": 100, "f": 0.6, "rot": 6}]}

def scene(say, bg, actors, props, text=None):
    return {"say": say, "text": text or say, "bg": bg, "actors": actors, "props": props}

def A(id, x, **kw):
    d = {"id": id, "x": x, "pose": "stand", "face": "neutral", "scale": 1.15}; d.update(kw); return d

def J(id, x, **kw):  # espri sahnesi karakteri: smug -> shock
    return A(id, x, pose="hips", face="smug", scale=1.2, pose2="shock", face2="shock", switch=0.55, **kw)

GB = {"type": "goldbars", "x": 0.74, "y": 0.93, "scale": 0.95}
PIG = {"type": "piggy", "x": 0.72, "y": 0.83, "scale": 0.9}
COINS = {"type": "coins", "x": 0.72, "y": 0.93, "n": 4}
EPS = []

# ---------------------------------------------------------------- 006 Mısır
EPS.append({"file": "006_misir", "title": "Mısırlılar Beyaz Parayı Neden Saklar?", "country": {"name": "Mısır", "code": "EG"},
 "caption": "Beyaz parayı kara gün için saklayın 🇪🇬🪙\n\nArap dünyasında, Mısır'da da çok bilinen bir söz: \"Beyaz kuruşunu kara günün için sakla.\" Temiz kazandığın parayı zor günler için kenara ayırmayı öğütler. Bizdeki \"ak akçe kara gün içindir\" sözünün kuzeni gibi!\n\nSen kara gün için kenara para ayırır mısın? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #mısır #atasözü #birikim #paraatlası",
 "scenes": [
  intro("Mısırlılar beyaz parayı neden hep kara günler için saklar, biliyor musun? Çünkü bu konuda çok eski bir sözleri var.", "MISIR!", "BEYAZ & KARA"),
  quote("Habbi kırşek il ebyad li yevmek il esved. Yani: Beyaz kuruşunu, kara günün için sakla.",
        "Habbi kırşek il ebyad li yevmek il esved. Yani: Beyaz kuruşunu, kara günün için sakla.",
        "Khabbi qershak el-abyad li-yomak el-aswad", "", "Beyaz kuruşunu kara günün için sakla."),
  scene("Bu söz Arap dünyasında, Mısır'da da çok bilinir. Beyaz kuruş temiz, çalışarak kazanılmış parayı, kara gün de zor günleri anlatır.", "city",
        [A("k", 0.3, hat="nemes", pose="point", face="happy", scale=1.2)], [{"type": "coin", "x": 0.7, "y": 0.4, "symbol": "E", "scale": 1.3}]),
  scene("Yani bugün her parayı harcama, bir kısmını yarının zor günü için kenara ayır. Bir önceki sözümüzün tam kuzeni!", "vault",
        [A("k", 0.3, hat="nemes", pose="open", face="happy", scale=1.2)],
        [PIG, {"type": "coin", "x": 0.72, "y": 0.2, "to_y": 0.62, "move_dur": 0.8, "delay": 1.5, "scale": 0.8}]),
  joke("Düşünsene, firavunlar kara gün için öyle bir biriktirmiş ki, adı piramit olmuş!", J("k", 0.3, hat="nemes"), "PİRAMİT!"),
  lesson("Günün dersi: Güneşli günde gölgelik hazırlayanın, yağmurdan canı yanmaz!", GB),
  outro("Mısır", "Brezilya'ya", "BREZİLYA")]})

# ---------------------------------------------------------------- 007 Brezilya
EPS.append({"file": "007_brezilya", "title": "Brezilyalı Tavuk Kursağını Böyle Doldurur", "country": {"name": "Brezilya", "code": "BR"},
 "caption": "Brezilyalı tavuk bile tasarruf biliyor 🐔🇧🇷\n\n\"De grão em grão, a galinha enche o papo.\" Yani: Tane tane yiyen tavuğun kursağı dolar. Brezilya'da küçük adımlarla büyük sonuca ulaşmayı anlatmak için çok kullanılan bir deyiş.\n\nSen hangi alışkanlığı tane tane biriktirdin? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #brezilya #atasözü #birikim #paraatlası",
 "scenes": [
  intro("Brezilyalılar bir tavuğa bakıp paranın sırrını öğrenmiş. Hem de tek bir tahılla!", "BREZİLYA!", "TAVUK?!"),
  quote("Ci grav eyn grav, a galinya enşi u papu. Yani: Tane tane, tavuk kursağını doldurur.",
        "Ci grav eyn grav, a galinya enşi u papu. Yani: Tane tane, tavuk kursağını doldurur.",
        "De grão em grão, a galinha enche o papo", "", "Tane tane, tavuk kursağını doldurur."),
  scene("Tavuk tek seferde koca bir çuval yemez. Her gün biraz biraz yer ama sonunda karnı da kursağı da dolar.", "city",
        [A("k", 0.28, pose="point", face="happy", scale=1.2)], [{"type": "coin", "x": 0.7, "y": 0.4, "symbol": "R", "scale": 1.2}]),
  scene("Para da öyle! Küçük küçük kenara koyduğun miktarlar, zamanla büyük bir birikime dönüşür. Bizdeki damlaya damlaya göl olur sözüyle aynı akıl.", "vault",
        [A("k", 0.28, pose="open", face="happy", scale=1.2)],
        [PIG, {"type": "coin", "x": 0.7, "y": 0.2, "to_y": 0.62, "move_dur": 0.8, "delay": 1.0, "scale": 0.8},
         {"type": "coin", "x": 0.74, "y": 0.2, "to_y": 0.62, "move_dur": 0.8, "delay": 2.8, "scale": 0.8}]),
  joke("Tavuk bile tane tane biriktirmeyi biliyor. Biz ise kahve fiyatına şaşırıp kafa tavuğu gibi dönüyoruz!", J("k", 0.3), "KOT KOT!"),
  lesson("Günün dersi: Büyük hedefler, küçük adımların toplamıdır!", COINS),
  outro("Brezilya", "Amerika Birleşik Devletleri'ne", "ABD")]})

# ---------------------------------------------------------------- 008 ABD
EPS.append({"file": "008_abd", "title": "Zaman da Paradır, Diyen Adam", "country": {"name": "ABD", "code": "US"},
 "caption": "Zaman da para mı? 🇺🇸⏰\n\n\"Time is money\": Zaman paradır. Bu sözü Benjamin Franklin 1748'de \"Genç Bir Esnafa Öğüt\" yazısında yazdı. Franklin bugün 100 dolarlık banknotun üzerinde!\n\nSence zaman mı daha değerli, para mı? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #abd #franklin #zaman #paraatlası",
 "scenes": [
  intro("Bir yazar çıkmış, 'zaman paradır' demiş. Üstelik 250 yıldan fazla önce. Bugün hâlâ hepimiz bu sözü kullanıyoruz.", "ABD!", "ZAMAN = PARA"),
  quote("Taym iz mani. Yani: Zaman paradır.", "Taym iz mani. Yani: Zaman paradır.", "Time is money", "", "Zaman paradır."),
  scene("Bu sözü Benjamin Franklin söyledi. 1748'de Genç Bir Esnafa Öğüt adlı yazısında, boş geçen zamanın aslında kaybedilmiş kazanç olduğunu anlattı.", "city",
        [A("k", 0.28, pose="point", face="happy", scale=1.2)], [{"type": "banknote", "x": 0.7, "y": 0.4, "scale": 0.9, "symbol": "$", "flutter": True}]),
  scene("Franklin bugün 100 dolarlık banknotun üzerinde. Yani sözünü söyleyen adam, kendi paranın üzerine yerleşmiş!", "bank",
        [A("k", 0.28, pose="open", face="happy", scale=1.2)], [{"type": "banknote", "x": 0.7, "y": 0.45, "scale": 1.0, "symbol": "$100", "flutter": True}]),
  joke("Zaman gerçekten para olsaydı, telefonda kaydırarak geçirdiğimiz saatlerle hepimiz iflas ederdik!", J("k", 0.3), "İFLAS!"),
  lesson("Günün dersi: Parayı kaybedersen geri kazanırsın, zamanı kaybedersen asla!", GB),
  outro("ABD", "İngiltere'ye", "İNGİLTERE")]})

# ---------------------------------------------------------------- 009 İngiltere
EPS.append({"file": "009_ingiltere", "title": "İngilizler Parasını Böyle Kaybeder", "country": {"name": "İngiltere", "code": "GB"},
 "caption": "İngilizlerin harcama uyarısı 🇬🇧🎩\n\n\"A fool and his money are soon parted.\" Yani: Düşünmeden harcayanın parası çabuk gider. Benzer bir biçimi Thomas Tusser'ın 1573 tarihli şiirinde geçiyor.\n\nSon pişman olduğun alışveriş neydi? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #ingiltere #atasözü #harcama #paraatlası",
 "scenes": [
  intro("İngilizler düşünmeden harcayanı uyarmak için çok eski bir söz kullanır. Peki parayı kim, nasıl kaybediyor?", "İNGİLTERE!", "PARA GİDİYOR"),
  quote("A ful end hiz mani ar sun partıd. Yani: Düşünmeden harcayanın parası çabuk gider.",
        "A ful end hiz mani ar sun partıd. Yani: Düşünmeden harcayanın parası çabuk gider.",
        "A fool and his money are soon parted", "", "Düşünmeden harcayanın parası çabuk gider."),
  scene("Benzer bir biçimi, Thomas Tusser'ın 1573 tarihli bir şiirinde geçiyor. Yani söz yaklaşık 450 yıldır dilimizde yaşıyor.", "city",
        [A("k", 0.28, hat="tophat", pose="point", face="happy", scale=1.2)], [{"type": "coin", "x": 0.7, "y": 0.4, "symbol": "£", "scale": 1.3}]),
  scene("Anlamı şu: Parayı düşünmeden harcayan, onu uzun süre elinde tutamaz. Bir şey almadan önce kendine bir sor: Gerçekten ihtiyacım var mı?", "bank",
        [A("k", 0.28, hat="tophat", pose="open", face="happy", scale=1.2)], [{"type": "wallet", "x": 0.72, "y": 0.8, "scale": 0.8, "empty": True}]),
  joke("Mesela yüzde 70 indirimde bir şey alan kişi 'tam 70 lira kazandım' der. Oysa 30 lira harcamış!", J("k", 0.3, hat="tophat"), "30 LİRA!"),
  lesson("Günün dersi: Almadan önce bir dur, düşün, sonra al!", GB),
  outro("İngiltere", "İtalya'ya", "İTALYA")]})

# ---------------------------------------------------------------- 010 İtalya
EPS.append({"file": "010_italya", "title": "İtalyanlar Risk Almayana Ne Der?", "country": {"name": "İtalya", "code": "IT"},
 "caption": "İtalyanlar riske böyle bakıyor 🇮🇹🍝\n\n\"Chi non risica non rosica.\" Yani: Risk almayan, kemirmez; bir şey kazanamaz. İtalya'da cesareti ve girişimi överken çok kullanılan bir söz. Sadece bir söz; yatırım tavsiyesi değil!\n\nSen hayatında hangi riski aldığına sevindin? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #italya #atasözü #risk #paraatlası",
 "scenes": [
  intro("İtalyanlar riske şöyle bakar: Hiç kimse yerinde durarak ileri gitmez. Peki bunu paraya nasıl bağlamışlar?", "İTALYA!", "RİSK?!"),
  quote("Ki non rizika non rozika. Yani: Risk almayan kazanamaz.", "Ki non rizika non rozika. Yani: Risk almayan kazanamaz.",
        "Chi non risica non rosica", "", "Risk almayan kazanamaz."),
  scene("Rosika, kemirmek demek. Yani söz şunu söylüyor: Hiç riske girmeyen, kemirecek bir şey de bulamaz.", "city",
        [A("k", 0.28, pose="point", face="happy", scale=1.2)], [{"type": "coin", "x": 0.7, "y": 0.4, "symbol": "€", "scale": 1.3}]),
  scene("Bu bir yatırım tavsiyesi değil, sadece bir söz! İtalyanlar bunu genelde cesaret göstermek ve yeni bir şey denemek için söyler.", "vault",
        [A("k", 0.28, pose="open", face="happy", scale=1.2)], [{"type": "banknote", "x": 0.7, "y": 0.4, "scale": 0.9, "symbol": "€", "flutter": True}]),
  joke("Ama bir İtalyan için en büyük risk, makarnayı pişirirken suya tuz atmayı unutmak!", J("k", 0.3), "TUZ?!"),
  lesson("Günün dersi: Cesaret hesapsız olmaz, hesap da cesaretsiz!", COINS),
  outro("İtalya", "Çin'e", "ÇİN")]})

# ---------------------------------------------------------------- 011 Çin
EPS.append({"file": "011_cin", "title": "Çinlilere Göre Para Neyi Çevirtir?", "country": {"name": "Çin", "code": "CN"},
 "caption": "Çin'de paranın gücü böyle anlatılır 🇨🇳🪙\n\n有钱能使鬼推磨 (Yǒu qián néng shǐ guǐ tuī mò): \"Parası olan, hayalete bile değirmen çevirtir.\" Çin'de çok bilinen bu söz, paranın ne kadar güçlü olduğunu abartarak anlatır.\n\nSence para gerçekten her kapıyı açar mı? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #çin #atasözü #güç #paraatlası",
 "scenes": [
  intro("Çinlilere göre para öyle güçlü ki, hayaletlere bile iş yaptırabilir. Hem de değirmen çevirtir!", "ÇİN!", "HAYALET?!"),
  quote("Yo çiyen neng şı guey tuey mo. Yani: Parası olan, hayalete bile değirmen çevirtir.",
        "Yo çiyen neng şı guey tuey mo. Yani: Parası olan, hayalete bile değirmen çevirtir.",
        "有钱能使鬼推磨", "Yǒu qián néng shǐ guǐ tuī mò", "Parası olan, hayalete bile değirmen çevirtir."),
  scene("Eskiden değirmen taşını döndürmek çok yorucu bir işti. Söz diyor ki: Para varsa, kimse yorucu işten kaçmaz. Hayalet bile!", "city",
        [A("k", 0.28, pose="push", face="happy", scale=1.2)], [{"type": "coin", "x": 0.7, "y": 0.4, "symbol": "¥", "scale": 1.3}]),
  scene("Bu söz, paranın gücünü abartarak anlatır. Çin'de çok bilinir ve çoğu zaman biraz da eleştiri tonuyla söylenir.", "bank",
        [A("k", 0.28, pose="open", face="happy", scale=1.2)], [{"type": "banknote", "x": 0.7, "y": 0.4, "scale": 0.9, "symbol": "¥", "flutter": True}]),
  joke("Hayalet bile para için çalışıyorsa, pazartesi sabahı yorgun olmamız çok normal!", J("k", 0.3), "PAZARTESİ!"),
  lesson("Günün dersi: Para çok iş yaptırır, ama saygıyı ve dostluğu satın alamaz!", GB),
  outro("Çin", "Fransa'ya", "FRANSA")]})

# ---------------------------------------------------------------- 012 Fransa
EPS.append({"file": "012_fransa", "title": "Paranın Kokusu Olmaz Diyen İmparator", "country": {"name": "Fransa", "code": "FR"},
 "caption": "Paranın kokusu olmaz! 🇫🇷👃\n\n\"L'argent n'a pas d'odeur.\" Fransızcada çok bilinen bu söz, Roma imparatoru Vespasianus'a dayanan bir hikâyeden geliyor: Halk tuvaletlerinden vergi aldığı için oğlu itiraz edince bir parayı burnuna tutmuş.\n\nSence her kazanç aynı değerde mi? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #fransa #atasözü #roma #paraatlası",
 "scenes": [
  intro("Fransızlar paranın kokusuyla ilgili bir söz kullanır. Hikâyesi ise iki bin yıl önceki bir Roma imparatoruna dayanır!", "FRANSA!", "KOKU?!"),
  quote("Larjan na pa dodör. Yani: Paranın kokusu olmaz.", "Larjan na pa dodör. Yani: Paranın kokusu olmaz.",
        "L'argent n'a pas d'odeur", "", "Paranın kokusu olmaz."),
  scene("Hikâyeye göre Roma imparatoru Vespasianus, halk tuvaletlerinden vergi almaya başlamış. Oğlu Titus ise bundan hoşlanmamış.", "city",
        [A("k", 0.28, hat="crown", pose="point", face="happy", scale=1.2)], [{"type": "coin", "x": 0.7, "y": 0.4, "symbol": "€", "scale": 1.3}]),
  scene("İmparator bir parayı oğlunun burnuna tutup 'Kokuyor mu?' diye sormuş. Cevap hayır olunca da sözün çıkış hikâyesi tamamlanmış.", "bank",
        [A("k", 0.28, hat="crown", pose="open", face="happy", scale=1.2)], [{"type": "coin", "x": 0.7, "y": 0.4, "symbol": "€", "scale": 1.3, "spin": True}]),
  joke("Romalılar tuvaletten bile vergi almış. Bizim faturalar bunun yanında çiçek gibi kalır!", J("k", 0.3, hat="crown"), "VERGİ!"),
  lesson("Günün dersi: Para kokmaz ama kazandığın yol kokmasın!", COINS),
  outro("Fransa", "İspanya'ya", "İSPANYA")]})

for i, e in enumerate(EPS, start=6):
    out = {"id": f"{i:03d}", "series": "PARA ATLASI", "title": e["title"], "country": e["country"],
           "voice_fx": {"pitch": 1.0, "noise": 0.2, "noise_w": 0.3}, "instagram_caption": e["caption"], "scenes": e["scenes"]}
    assert out["instagram_caption"].count("#") == 5 and out["instagram_caption"].rstrip().endswith("#paraatlası"), e["file"]
    json.dump(out, open(os.path.join(ROOT, "episodes", e["file"] + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    words = sum(len(s["say"].split()) for s in e["scenes"])
    print("yazıldı:", e["file"], len(e["scenes"]), "sahne,", words, "kelime")
