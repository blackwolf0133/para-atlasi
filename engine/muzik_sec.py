"""KİM HAKLI? fon müziği: Kevin MacLeod (incompetech.com), CC BY 4.0 — dünyada en çok kullanılan telifsiz katalog.
Meraklı/esprili parçalar; bölüm numarasına göre sırayla döner. Bölümde "muzik": "<ad>" ile elle seçilebilir.
İndirilemezse motor eski sentetik fona düşer."""
import os
import re
import urllib.request

PARCALAR = ["Sneaky Snitch", "Monkeys Spinning Monkeys", "Investigations", "Fluffing a Duck", "Scheming Weasel faster"]


def sec(ep):
    if ep.get("muzik"):
        return ep["muzik"]
    m = re.search(r"\d+", str(ep.get("id", "0")))
    return PARCALAR[(int(m.group()) - 1) % len(PARCALAR)] if m else PARCALAR[0]


def kredi(ep):
    return f'Müzik: "{sec(ep)}" Kevin MacLeod (incompetech.com) · CC BY 4.0'


def indir(ep, hedef):
    url = "https://incompetech.com/music/royalty-free/mp3-royaltyfree/" + sec(ep).replace(" ", "%20") + ".mp3"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        open(hedef, "wb").write(urllib.request.urlopen(req, timeout=60).read())
        print("Müzik:", kredi(ep), flush=True)
        return hedef
    except Exception as e:
        print("Müzik indirilemedi, sentetik fon:", e, flush=True)
        return None
