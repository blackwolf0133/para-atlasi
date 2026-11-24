"""Para Atlası 2-5. bölümler (Kore, Almanya, Rusya, Türkiye)."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAIL = "Her gün bir ülkenin para bilgeliği için takip et 🌍"

def intro(say, text, pop1, pop2):
    return {"say": say, "text": text, "voice_delay": 1.0,
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
    return {"say": f"Bir sözü daha pasaportumuza bastık! Yarın {nxt} gidiyoruz. Takip et, kaçırma!",
            "text": f"Bir sözü daha pasaportumuza bastık! Yarın {nxt} gidiyoruz. Takip et, kaçırma!",
            "voice_delay": 0.5,
            "narrator": {"x": 0.5, "y": 0.97, "scale": 1.5, "pose": "open", "face": "happy",
              "beats": [{"f": 0.4, "pose": "point", "face": "happy"}, {"f": 0.75, "pose": "wave", "face": "wink"}]},
            "props": [{"type": "stamp", "text": country, "x": 0.8, "y": 0.17, "f": 0.12, "rot": -14, "scale": 0.8},
                      {"type": "pop", "text": "YARIN: " + pop + "!", "x": 0.28, "y": 0.15, "size": 84, "f": 0.45, "rot": -6}]}

def A(id, x, **kw):
    d = {"id": id, "x": x, "pose": "stand", "face": "neutral", "scale": 1.15}; d.update(kw); return d

EPS = []

# ---------------------------------------------------------------- 002 Kore
EPS.append({"file": "002_kore", "title": "Koreliler Tozdan Dağ Yapar", "country": {"name": "Güney Kore", "code": "KR"},
 "caption": "Koreliler paraya bakınca dağ görür 🏔️🇰🇷\n\n티끌 모아 태산 (Tikkeul moa taesan): \"Toz toz birikir, dağ olur.\" Kore'de küçük küçük para biriktirmeyi anlatmak için kullanılan çok bilinen bir atasözü. Günde 100 lirayı kenara koyarsan bir yılda 36 bin 500 lira eder!\n\nSen günde ne kadar biriktirirsin? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #kore #atasözü #birikim #paraatlası",
 "scenes": [
  intro("Koreliler paraya bakınca ne görür, biliyor musun? Dağ! Hem de tozdan yapılmış bir dağ.", "Koreliler paraya bakınca ne görür, biliyor musun? Dağ! Hem de tozdan yapılmış bir dağ.", "KORE!", "TOZDAN DAĞ?!"),
  quote("Tikıl moa tesan. Yani: Toz toz birikir, dağ olur.", "Tikkeul moa taesan. Yani: Toz toz birikir, dağ olur.", "티끌 모아 태산", "Tikkeul moa taesan", "Toz toz birikir, dağ olur."),
  {"say": "Bu söz, küçük küçük para biriktirmenin gücünü anlatır. Bugün kenara koyduğun azıcık para, yarın dev bir yığına dönüşür.", "text": "Bu söz, küçük küçük para biriktirmenin gücünü anlatır. Bugün kenara koyduğun azıcık para, yarın dev bir yığına dönüşür.",
   "bg": "city", "actors": [A("k", 0.28, pose="point", face="happy", scale=1.2)],
   "props": [{"type": "piggy", "x": 0.7, "y": 0.83, "scale": 0.9}, {"type": "coin", "x": 0.7, "y": 0.2, "to_y": 0.62, "move_dur": 0.8, "delay": 1.0, "scale": 0.8},
             {"type": "coin", "x": 0.66, "y": 0.2, "to_y": 0.62, "move_dur": 0.8, "delay": 2.4, "scale": 0.8},
             {"type": "coin", "x": 0.74, "y": 0.2, "to_y": 0.62, "move_dur": 0.8, "delay": 3.8, "scale": 0.8}]},
  {"say": "Hesap çok basit. Günde sadece 100 lirayı kenara koyarsan, bir yılda 36500 lira biriktirirsin. Bir yıl önce 'bu kadarcık paradan ne olur' demiştin, değil mi?", "text": "Hesap çok basit. Günde sadece 100 lirayı kenara koyarsan, bir yılda 36.500 lira biriktirirsin. Bir yıl önce \"bu kadarcık paradan ne olur\" demiştin, değil mi?",
   "bg": "vault", "emotion": "şaşkın", "actors": [A("k", 0.3, pose="think", face="think", scale=1.2, pose2="shock", face2="shock", switch=0.5)],
   "props": [{"type": "coins", "x": 0.72, "y": 0.93, "n": 4}, {"type": "pop", "text": "36.500 TL!", "x": 0.68, "y": 0.28, "size": 110, "f": 0.45, "rot": 6}]},
  {"say": "Günün dersi: Küçük parayı küçümseme, dağlar zaten tozdan başlar!", "text": "Günün dersi: Küçük parayı küçümseme, dağlar zaten tozdan başlar!", "bg": "vault", "emotion": "sakin",
   "actors": [A("b", 0.32, pose="point", face="confident", scale=1.3)],
   "props": [{"type": "goldbars", "x": 0.74, "y": 0.93, "scale": 0.95}, {"type": "sfx", "name": "rimshot", "f": 0.85}]},
  outro("Güney Kore", "Almanya'ya", "ALMANYA")]})

# ---------------------------------------------------------------- 003 Almanya
EPS.append({"file": "003_almanya", "title": "Almanlar Parayı Gübreye Benzetir", "country": {"name": "Almanya", "code": "DE"},
 "caption": "Almanlar parayı hayvan gübresine benzetmiş 😅🇩🇪\n\nKleinvieh macht auch Mist: \"Küçük hayvan da gübre yapar.\" Yani küçük kazançlar da birikince önemli bir miktar eder. Söz 19. yüzyılın ortalarından beri biliniyor.\n\nSen küçük kazançları ciddiye alır mısın? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #almanya #atasözü #tasarruf #paraatlası",
 "scenes": [
  intro("Almanlar parayı neye benzetir, biliyor musun? Hayvan gübresine! Hem de bunun için çok iyi bir sebepleri var.", "Almanlar parayı neye benzetir, biliyor musun? Hayvan gübresine! Hem de bunun için çok iyi bir sebepleri var.", "ALMANYA!", "GÜBRE?!"),
  quote("Klaynfi mahht auh mist. Yani: Küçük hayvan da gübre yapar.", "Kleinvieh macht auch Mist. Yani: Küçük hayvan da gübre yapar.", "Kleinvieh macht auch Mist", "Kleinvieh macht auch Mist", "Küçük hayvan da gübre yapar."),
  {"say": "Bu söz 19. yüzyılın ortalarından beri kullanılıyor. Almanca'da para ile gübre, eski deyimlerde sık sık yan yana gelir.", "text": "Bu söz 19. yüzyılın ortalarından beri kullanılıyor. Almanca'da para ile gübre, eski deyimlerde sık sık yan yana gelir.",
   "bg": "city", "actors": [A("k", 0.3, pose="open", face="happy", scale=1.2)], "props": [{"type": "coin", "x": 0.7, "y": 0.4, "spin": True, "scale": 1.2}]},
  {"say": "Anlamı şu: Küçük hayvan tek başına az gübre yapar ama sürü olunca ortalık dolar. Küçük kazançlar da böyle birikir.", "text": "Anlamı şu: Küçük hayvan tek başına az gübre yapar ama sürü olunca ortalık dolar. Küçük kazançlar da böyle birikir.",
   "bg": "vault", "actors": [A("k", 0.3, pose="point", face="happy", scale=1.2)],
   "props": [{"type": "coin", "x": 0.6, "y": 0.8, "scale": 0.7, "delay": 0.8, "spin": False}, {"type": "coin", "x": 0.7, "y": 0.8, "scale": 0.7, "delay": 1.8, "spin": False},
             {"type": "coin", "x": 0.8, "y": 0.8, "scale": 0.7, "delay": 2.8, "spin": False}, {"type": "coin", "x": 0.65, "y": 0.65, "scale": 0.7, "delay": 3.8, "spin": False},
             {"type": "coin", "x": 0.75, "y": 0.65, "scale": 0.7, "delay": 4.8, "spin": False}]},
  {"say": "Mesela markette kilo başına birkaç kuruş indirim var diye alışveriş yapan bir Alman, bunu bir yıl boyunca yaparsa şaşırır. Kuruş kuruş birikir.", "text": "Mesela markette kilo başına birkaç kuruş indirim var diye alışveriş yapan bir Alman, bunu bir yıl boyunca yaparsa şaşırır. Kuruş kuruş birikir.",
   "bg": "city", "emotion": "şaşkın", "actors": [A("al", 0.3, pose="hips", face="smug", scale=1.2, pose2="shock", face2="shock", switch=0.6)],
   "props": [{"type": "wallet", "x": 0.72, "y": 0.88, "scale": 0.8}, {"type": "pop", "text": "KURUŞ KURUŞ!", "x": 0.62, "y": 0.28, "size": 92, "f": 0.6, "rot": -5}]},
  {"say": "Günün dersi: Küçük kazancı küçümseyen, büyük kazancı bekler!", "text": "Günün dersi: Küçük kazancı küçümseyen, büyük kazancı bekler!", "bg": "vault", "emotion": "sakin",
   "actors": [A("b", 0.32, pose="point", face="confident", scale=1.3)], "props": [{"type": "piggy", "x": 0.72, "y": 0.83, "scale": 0.9}, {"type": "sfx", "name": "rimshot", "f": 0.85}]},
  outro("Almanya", "Rusya'ya", "RUSYA")]})

# ---------------------------------------------------------------- 004 Rusya
EPS.append({"file": "004_rusya", "title": "Ruslar Paradan Çok Neyi Sever?", "country": {"name": "Rusya", "code": "RU"},
 "caption": "Ruslara göre yüz rublen olmasın ama… 🇷🇺🤝\n\nНе имей сто рублей, а имей сто друзей (Ne imey sto rubley, a imey sto druzey): \"Yüz rublen olmasın, yüz dostun olsun.\" Rusya'nın en bilinen sözlerinden biri; dostluğu paradan üstün tutar.\n\nSence dostluk paradan değerli mi? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #rusya #atasözü #dostluk #paraatlası",
 "scenes": [
  intro("Ruslara göre yüz rublen olmasın! Peki ne olsun? Cevabı paradan çok daha değerli.", "Ruslara göre yüz rublen olmasın! Peki ne olsun? Cevabı paradan çok daha değerli.", "RUSYA!", "YÜZ RUBLE?!"),
  quote("Ne imey sto rubley, a imey sto druzey. Yani: Yüz rublen olmasın, yüz dostun olsun.", "Ne imey sto rubley, a imey sto druzey. Yani: Yüz rublen olmasın, yüz dostun olsun.", "Не имей сто рублей, а имей сто друзей", "Ne imey sto rubley, a imey sto druzey", "Yüz rublen olmasın, yüz dostun olsun."),
  {"say": "Bu söz Rusya'da küçüklükten beri duyulan en bilinen atasözlerinden biridir. Dostluğu paradan üstün tutar.", "text": "Bu söz Rusya'da küçüklükten beri duyulan en bilinen atasözlerinden biridir. Dostluğu paradan üstün tutar.",
   "bg": "city", "actors": [A("a", 0.2, pose="cheer", face="happy"), A("b", 0.4, pose="cheer", face="happy"), A("c", 0.6, pose="cheer", face="happy", flip=True), A("d", 0.8, pose="cheer", face="happy", flip=True)],
   "props": [{"type": "banknote", "x": 0.5, "y": 0.28, "scale": 0.8, "symbol": "₽", "flutter": True}]},
  {"say": "Çünkü paranın bitebileceğini, ama dostun zor gününde yanında durduğunu söylerler. Parasız kalırsan seni bir dost kurtarır.", "text": "Çünkü paranın bitebileceğini, ama dostun zor gününde yanında durduğunu söylerler. Parasız kalırsan seni bir dost kurtarır.",
   "bg": "vault", "actors": [A("uzgun", 0.3, pose="sad", face="sad", scale=1.15), A("dost", 0.7, pose="open", face="happy", flip=True, scale=1.15)],
   "props": [{"type": "wallet", "x": 0.3, "y": 0.62, "scale": 0.65, "empty": True}, {"type": "bubble", "text": "Ben yanındayım!", "x": 0.62, "y": 0.12, "tx": 0.7, "ty": 0.32, "f": 0.55}]},
  {"say": "Ama bir şaka bu söze karşılık hep yapılır: Yüz dostun olsun ama yüzü de aynı akşam yemeğe gelmesin, yoksa yine paraya ihtiyacın olur!", "text": "Ama bir şaka bu söze karşılık hep yapılır: Yüz dostun olsun ama yüzü de aynı akşam yemeğe gelmesin, yoksa yine paraya ihtiyacın olur!",
   "bg": "city", "emotion": "şaşkın", "actors": [A("k", 0.3, pose="hips", face="smug", scale=1.2, pose2="shock", face2="shock", switch=0.55, anim2="shake")],
   "props": [{"type": "pop", "text": "100 KİŞİ!", "x": 0.68, "y": 0.28, "size": 105, "f": 0.6, "rot": 6}]},
  {"say": "Günün dersi: Parayı kazan, ama dostu kaybetme!", "text": "Günün dersi: Parayı kazan, ama dostu kaybetme!", "bg": "vault", "emotion": "sakin",
   "actors": [A("b", 0.32, pose="point", face="confident", scale=1.3)], "props": [{"type": "coins", "x": 0.72, "y": 0.93, "n": 5}, {"type": "sfx", "name": "rimshot", "f": 0.85}]},
  outro("Rusya", "Türkiye'ye", "TÜRKİYE")]})

# ---------------------------------------------------------------- 005 Türkiye
EPS.append({"file": "005_turkiye", "title": "Atalarımız Paraya Ne Demiş?", "country": {"name": "Türkiye", "code": "TR"},
 "caption": "Dedelerimizden kalma en iyi finans tavsiyesi 🇹🇷💰\n\n\"Ak akçe kara gün içindir.\" Çalışıp kazandığın parayı, zor günlerin için ayır demek. Atasözü bize Osmanlı'dan kalma: akçe eskiden kullanılan küçük gümüş paranın adı.\n\nSen kara gün için biriktiriyor musun? Yorumlara yaz 👇\n" + TAIL + "\n\n#para #türkiye #atasözü #birikim #paraatlası",
 "scenes": [
  intro("Dedelerimizin en iyi finans tavsiyesi hangisi biliyor musun? Hepimiz duyduk ama kaç kişi uyguluyor?", "Dedelerimizin en iyi finans tavsiyesi hangisi biliyor musun? Hepimiz duyduk ama kaç kişi uyguluyor?", "TÜRKİYE!", "KARA GÜN?!"),
  quote("Ak akçe kara gün içindir. Yani: Biriktirdiğin para, zor günler için.", "Ak akçe kara gün içindir. Yani: Biriktirdiğin para, zor günler için.", "Ak akçe kara gün içindir", "", "Biriktirdiğin para, zor günler için."),
  {"say": "Akçe, eskiden kullanılan küçük gümüş paranın adıydı. Ak da beyaz demek: Yani temiz, çalışarak kazanılmış para.", "text": "Akçe, eskiden kullanılan küçük gümüş paranın adıydı. Ak da beyaz demek: Yani temiz, çalışarak kazanılmış para.",
   "bg": "city", "actors": [A("k", 0.3, hat="sarik", pose="point", face="happy", scale=1.2)], "props": [{"type": "coin", "x": 0.7, "y": 0.4, "symbol": "A", "scale": 1.3}]},
  {"say": "Atasözü şunu söyler: Sağlığın ve gücün yerindeyken çalışıp kazandığın parayı sakla. Bir gün lazım olacak, o gün seni darlıktan çıkarır.", "text": "Atasözü şunu söyler: Sağlığın ve gücün yerindeyken çalışıp kazandığın parayı sakla. Bir gün lazım olacak, o gün seni darlıktan çıkarır.",
   "bg": "vault", "actors": [A("k", 0.3, hat="sarik", pose="open", face="happy", scale=1.2)],
   "props": [{"type": "piggy", "x": 0.72, "y": 0.83, "scale": 0.9}, {"type": "coin", "x": 0.72, "y": 0.2, "to_y": 0.62, "move_dur": 0.8, "delay": 1.5, "scale": 0.8}]},
  {"say": "Tabii kara günün ne zaman geleceğini kimse bilmez. O yüzden bu atasözü, bir de şunu fısıldar: Akşam yemeğinde son dört baklava yerine ikisi yeter!", "text": "Tabii kara günün ne zaman geleceğini kimse bilmez. O yüzden bu atasözü, bir de şunu fısıldar: Akşam yemeğinde son dört baklava yerine ikisi yeter!",
   "bg": "city", "emotion": "şaşkın", "actors": [A("k", 0.3, hat="sarik", pose="hips", face="smug", scale=1.2, pose2="shock", face2="shock", switch=0.55)],
   "props": [{"type": "pop", "text": "2 YETER!", "x": 0.7, "y": 0.28, "size": 105, "f": 0.6, "rot": 6}]},
  {"say": "Günün dersi: Parayı kazanmak hüner, saklamak ise erdemdir!", "text": "Günün dersi: Parayı kazanmak hüner, saklamak ise erdemdir!", "bg": "vault", "emotion": "sakin",
   "actors": [A("b", 0.32, pose="point", face="confident", scale=1.3)], "props": [{"type": "goldbars", "x": 0.74, "y": 0.93, "scale": 0.95}, {"type": "sfx", "name": "rimshot", "f": 0.85}]},
  outro("Türkiye", "Mısır'a", "MISIR")]})

for i, e in enumerate(EPS, start=2):
    out = {"id": f"{i:03d}", "series": "PARA ATLASI", "title": e["title"], "country": e["country"],
           "voice_fx": {"pitch": 1.0, "noise": 0.2, "noise_w": 0.3}, "instagram_caption": e["caption"], "scenes": e["scenes"]}
    json.dump(out, open(os.path.join(ROOT, "episodes", e["file"] + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    n = out["instagram_caption"].count("#")
    print("yazıldı:", e["file"], len(e["scenes"]), "sahne, etiket:", n)
