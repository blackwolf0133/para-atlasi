"""13 Kasım: sıradaki paylaşılmamış bölümlere kanca_yazi ekler; 100+ kelimelik olanları 25-35 sn'ye kısaltır."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KANCA = {
 "011_cin": "Para hayalete bile değirmen çevirtir!",
 "012_fransa": "Paranın kokusu olmaz diyen imparator",
 "013_ispanya": "Çamaşır makinesi hep ayın sonunda bozulur!",
 "014_hindistan": "Aylık sadece 500 lira, altı taneyse?",
 "015_hollanda": "Günde bir kahve yılda 29200 lira!",
 "016_isvec": "Üç al iki öde gerçekten kazanç mı?",
 "017_polonya": "Üstü kalsın demek yılda kaç lira?",
}
# sahne dizini -> yeni konuşma (yalnızca kısaltılan bölümler)
SHORT = {
 "014_hindistan": {0: "Aylık sadece 500 lira diyen taksit, altı tane olunca ne olur? Hintlilerin çarşaflı bir cevabı var!",
    2: "Ece altı taksit aldı. Aylık 500 lira, altı tane 3000 lira eder.",
    3: "Deniz çarşafına baktı. En fazla 1000 lira dedi, iki taksitte durdu.",
    4: "Deniz'in cebinde her ay 2000 lira fazla kalıyor. Ece'nin çarşafı kısa kaldı!",
    5: "Günün dersi: Taksit küçük görünür, toplamı büyük çıkar!",
    6: "Ülke 14 tamam. Bunu her ay taksitle boğulan arkadaşına gönder. Yarın Hollanda!"},
 "016_isvec": {0: "Üç al iki öde afişini gören İsveçlilerin tek kelimelik bir cevabı var!",
    2: "Lena üç şampuan aldı, 200 lira ödedi, 100 lira kazandım dedi.",
    3: "Erik'e tek şampuan lazımdı. Bir tane aldı, 100 lira ödedi.",
    4: "Lena 100 lira kazandığını sandı ama cebinden 100 lira fazla çıktı!",
    5: "Günün dersi: İhtiyacın yoksa bedava bile pahalıdır!",
    6: "Ülke 16 tamam. Bunu her afişe koşan arkadaşına gönder. Yarın Polonya!"},
 "017_polonya": {0: "Üstü kalsın deyince cebinden ne kadar gidiyor? Polonyalıların tavuklu bir cevabı var!",
    2: "Piotr her gün üstü kalsın diyor. Günde ortalama 7 lira bırakıyor.",
    3: "Ola üstünü alıp kavanoza atıyor. O da günde 7 lira.",
    4: "Bir yıl sonra Piotr'un 2555 lirası uçmuş. Ola'nın kavanozu 2555 lira dolu!",
    5: "Günün dersi: Bozuk para küçük görünür, sayarsan büyür!",
    6: "Ülke 17 tamam. Bunu her yerde üstü kalsın diyen arkadaşına gönder. Yarın Yunanistan!"},
}
for name, k in KANCA.items():
    for fn in os.listdir(os.path.join(ROOT, "episodes")):
        if fn.startswith(name):
            p = os.path.join(ROOT, "episodes", fn)
            d = json.load(open(p, encoding="utf-8"))
            d["kanca_yazi"] = k
            for i, s in SHORT.get(name, {}).items():
                d["scenes"][i]["say"] = s; d["scenes"][i]["text"] = s
            json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print(fn, sum(len(s["say"].split()) for s in d["scenes"]))
