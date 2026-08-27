# -*- coding: utf-8 -*-
import re, os, base64, html as _h

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_cache = {}

def _lade(datei):
    if datei not in _cache:
        _cache[datei] = open(os.path.join(ROOT, "projekte", datei), encoding="utf-8").read()
    return _cache[datei]

def _entferne_emoji(s):
    s = re.sub(r'[\U0001F000-\U0001FAFF←-⇿①-➿️⬀-⯿]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'^(?:[\u00b7\u2013\u2014-]|&middot;|&ndash;|\s)+', '', s).strip()

def _norm(s):
    s = _h.unescape(s)
    for a, b in (("\u00b7", " "), ("\u2013", "-"), ("\u2014", "-"), ("\u2019", "'")):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()

def _abschnitt(datei, ueberschrift):
    """Text ab der Überschrift bis zur nächsten h2/h3 gleicher Ebene."""
    c = _lade(datei)
    for tag in ("h2", "h3"):
        for m in re.finditer(rf'<{tag}[^>]*>(.*?)</{tag}>', c, re.S):
            roh = _h.unescape(re.sub(r'<[^>]+>', '', m.group(1)))
            if _norm(ueberschrift) in _norm(_entferne_emoji(roh)):
                rest = c[m.end():]
                ende = re.search(r'<h2[^>]*>', rest)
                return rest[:ende.start()] if ende else rest
    raise KeyError(f"{datei} :: {ueberschrift}")

def tab(datei, ueberschrift, nr=0, titel=None, hinweis=None):
    """Liefert die nr-te Tabelle nach der Überschrift, neu gerahmt."""
    block = _abschnitt(datei, ueberschrift)
    tabellen = re.findall(r'<table[^>]*>(.*?)</table>', block, re.S)
    if nr >= len(tabellen):
        raise IndexError(f"{datei} :: {ueberschrift} :: nur {len(tabellen)} Tabellen")
    inner = tabellen[nr]
    inner = inner.replace('class="st-ok"', 'class="ok"').replace('class="st-warn"', 'class="warn"')
    inner = inner.replace('class="st-no"', 'class="no"')
    inner = re.sub(r'class="prio prio--(\w+)"', r'class="marke marke--\1"', inner)
    inner = inner.replace('class="total-row"', 'class="summe"')
    # Verweise auf Website-Seiten entfernen: der Bericht muss eigenständig lesbar bleiben
    inner = re.sub(r'<a [^>]*href="(?!https?:)[^"]*"[^>]*>(.*?)</a>', r'\1', inner, flags=re.S)
    kopf = f'<h4 class="tab-titel">{titel}</h4>\n' if titel else ""
    fuss = f'<p class="tab-hinweis">{hinweis}</p>\n' if hinweis else ""
    return f'{kopf}<div class="tabellenrahmen"><table>{inner}</table></div>\n{fuss}'

def bild(pfad, alt, unterschrift, breit=False):
    voll = os.path.join(ROOT, pfad)
    ext = "png" if pfad.lower().endswith(".png") else "jpeg"
    with open(voll, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    cls = "beleg beleg--breit" if breit else "beleg"
    return (f'<figure class="{cls}">'
            f'<img src="data:image/{ext};base64,{b64}" alt="{alt}" loading="lazy" />'
            f'<figcaption>{unterschrift}</figcaption></figure>\n')

def bildreihe(*eintraege):
    inner = "".join(bild(*e) for e in eintraege)
    return f'<div class="belegreihe">{inner}</div>\n'
