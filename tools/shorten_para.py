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
 "011_cin": {0: "Para öyle güçlü ki hayalete bile değirmen çevirtir! Çinlilerin ünlü sözü bu.",
    2: "Eskiden değirmen taşını döndürmek çok yorucuydu. Söz diyor ki: Para varsa hayalet bile çalışır.",
    3: "Çin'de çok bilinir, çoğu zaman biraz da eleştiriyle söylenir.",
    4: "Hayalet bile para için çalışıyorsa, pazartesi yorgunluğumuz normal!",
    6: "Ülke 11 tamam. Bunu pazartesi sabahı hayalet gibi işe giden arkadaşına gönder. Yarın Fransa!"},
 "012_fransa": {0: "Paranın kokusu olmaz diyen Fransızların sözü, iki bin yıllık bir Roma hikâyesinden gelir!",
    2: "Roma imparatoru Vespasianus halk tuvaletlerinden vergi almaya başlamış. Oğlu Titus hoşlanmamış.",
    3: "İmparator bir parayı oğlunun burnuna tutup Kokuyor mu diye sormuş. Cevap hayır!",
    4: "Romalılar tuvaletten bile vergi almış. Bizim faturalar çiçek gibi kalır!",
    6: "Ülke 12 tamam. Bunu her faturaya sinirlenen arkadaşına gönder. Yarın İspanya!"},
 "013_ispanya": {2: "Kenan'ın makinesi bozuldu, yenisi 6000 lira. Kenarda parası yok, altı taksitle 7200 lira yazdılar.",
    3: "Selin her ay biraz kenara koymuş, 6000 lirayı peşin ödedi.",
    4: "Fark tam 1200 lira. Kenan bunu bahşiş sanmış, mağaza teşekkür etti!",
    6: "Ülke 13 tamam. Bunu makinesi hep ay sonunda bozulan arkadaşına gönder. Yarın Hindistan!"},
 "015_hollanda": {2: "Jan her sabah 80 liralık kahve alıyor. Yılda tam 29200 lira.",
    3: "Anna kahvesini evden termosla getiriyor. Yılda 7300 lira.",
    4: "Fark yılda 21900 lira! Jan'ın kahvesi sıcak, cüzdanı buz gibi.",
    6: "Ülke 15 tamam. Bunu her sabah kahveye koşan arkadaşına gönder. Yarın İsveç!"},
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
