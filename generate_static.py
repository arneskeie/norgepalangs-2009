#!/usr/bin/env python3
"""Generate all static HTML pages for the norgepalangs restoration."""
import os, xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.abspath(__file__))
PHP_ROOT = os.path.join(ROOT, '..', '01-original-php')

NAV_ITEMS = ["Hjem", "OmOss", "Reiserute", "Utstyr", "Turlogg",
             "Reisebrev", "Galleri", "Gjestebok", "Sponsorer"]

NAV_HREFS = {
    "Hjem":      "index.html",
    "OmOss":     "omoss.html",
    "Reiserute": "reiserute.html",
    "Utstyr":    "utstyr.html",
    "Turlogg":   "turlogg.html",
    "Reisebrev": "reisebrev.html",
    "Galleri":   "galleri.html",
    "Gjestebok": "gjestebok.html",
    "Sponsorer": "sponsorer.html",
}

JS_FUNCS = """\
<script type="text/javascript">
function MM_swapImgRestore(){var i,x,a=document.MM_sr;for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++)x.src=x.oSrc;}
function MM_findObj(n,d){var p,i,x;if(!d)d=document;if((p=n.indexOf("?"))>0&&parent.frames.length){d=parent.frames[n.substring(p+1)].document;n=n.substring(0,p);}if(!(x=d[n])&&d.all)x=d.all[n];for(i=0;!x&&i<d.forms.length;i++)x=d.forms[i][n];for(i=0;!x&&d.layers&&i<d.layers.length;i++)x=MM_findObj(n,d.layers[i].document);if(!x&&d.getElementById)x=d.getElementById(n);return x;}
function MM_swapImage(){var i,j=0,x,a=MM_swapImage.arguments;document.MM_sr=new Array;for(i=0;i<(a.length-2);i+=3)if((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x;if(!x.oSrc)x.oSrc=x.src;x.src=a[i+2];}}
</script>"""

HEADER_HTML = """\
<div id="header" style="position:relative;">
  <object type="application/x-shockwave-flash" data="Headermovie/Header.swf" width="900" height="121">
    <param name="movie" value="Headermovie/Header.swf"/>
    <param name="quality" value="high"/>
    <param name="bgcolor" value="#222222"/>
  </object>
  <a href="INDEXHREF" style="position:absolute;top:0;left:0;width:100%;height:100%;z-index:10;" aria-label="Hjem"></a>
</div>"""

FOOTER_HTML = """\
<div id="footer">
<span class="footertekst">
  WEBMASTER &amp; REDAKT&#216;R: <a href="http://folk.ntnu.no/arnesigm" target="_blank">ARNE S. SKEIE</a> &nbsp;&nbsp;|&nbsp;&nbsp;
  ANSVARLIG REDAKT&#216;R &amp; TURG&#197;ER: <a href="omoss.html">MARIUS MONTAROU</a> &nbsp;&nbsp;|&nbsp;&nbsp;
  NORGEp&#229;LANGS &copy; Copyright 2008/2009<br/>
  Henvendelser, foresp&#248;rsler og annet kan rettes p&#229; mail til Marius p&#229; montarou@stud.ntnu.no
</span>
<br/>
&nbsp;<br/>&nbsp;
</div>"""

SPONSORLISTE_HTML = """\
<div id="Sponsorliste">
  <div class="Sponsortoppen"><img src="images/diverse/sponsortopp.png" alt="topp" width="124" height="22" border="0"/></div>
  <div id="Sponsorbody">
    <a href="http://www.xxl.no/" target="_blank"><img src="images/sponsors/XXL.jpg" alt="XXL" border="0"/></a><br/><br/>
    <a href="http://www.janus.no/" target="_blank"><img src="images/sponsors/Janus.jpg" alt="Janus" border="0"/></a><br/><br/>
    <a href="http://www.sportsbua.no/" target="_blank"><img src="images/sponsors/sportsbua.jpg" alt="Sportsbua" border="0"/></a><br/><br/>
    <a href="http://www.helsport.no/" target="_blank"><img src="images/sponsors/Helsport.jpg" alt="Helsport" border="0"/></a><br/><br/>
    <a href="http://www.cappelendamm.no/" target="_blank"><img src="images/sponsors/Cappelen.jpg" alt="Cappelen" border="0"/></a><br/><br/>
    <a href="http://www.alfasko.no/" target="_blank"><img src="images/sponsors/Alfasko.jpg" alt="Alfasko" border="0"/></a><br/><br/>
    <a href="http://www.asnes.com/" target="_blank"><img src="images/sponsors/Asnes.jpg" alt="&#197;snes" border="0"/></a><br/><br/>
    <a href="http://www.fjellpulken.no/" target="_blank"><img src="images/sponsors/Fjellpulken.jpg" alt="Fjellpulken" border="0"/></a><br/><br/>
    <a href="http://www.rottefella.no/" target="_blank"><img src="images/sponsors/rottefella.jpg" alt="Rottefella" border="0"/></a><br/><br/>
    <a href="http://www.amfibi.no/" target="_blank"><img src="images/sponsors/amfibi.jpg" alt="Amfibi" border="0"/></a><br/><br/>
    <a href="http://www.adidas.com/Eyewear/" target="_blank"><img src="images/sponsors/adidaseyewear.jpg" alt="Adidas" border="0"/></a><br/><br/>
    <a href="http://www.mx-sport.no/medlemmer/telemark/" target="_blank"><img src="images/sponsors/mxsport.jpg" alt="MX Sport" border="0"/></a><br/><br/>
    <a href="http://www.skaidihotel.no/" target="_blank"><img src="images/sponsors/Skaidi.jpg" alt="Skaidi" border="0"/></a><br/><br/>
    <a href="http://www.breidablikk.no/" target="_blank"><img src="images/sponsors/Breidablikk.jpg" alt="Breidablikk" border="0"/></a><br/><br/>
    <a href="http://www.lundhogdacamping.no/" target="_blank"><img src="images/sponsors/Lundhogda.jpg" alt="Lundhogda" border="0"/></a><br/><br/>
    <a href="http://www.femundfjellstue.no/" target="_blank"><img src="images/sponsors/Femund.jpg" alt="Femund Fjellstue" border="0"/></a><br/><br/>
    <a href="http://www.umbuktafjellstue.no/" target="_blank"><img src="images/sponsors/Umbukta.jpg" alt="Umbukta Fjellstue" border="0"/></a><br/><br/>
    <a href="http://rlb.no/seng/info/2924" target="_blank"><img src="images/sponsors/Jule.jpg" alt="Jule Ferie &amp; Fritid" border="0"/></a><br/><br/>
    <a href="http://www.dokkacamping.no/" target="_blank"><img src="images/sponsors/Dokkacamping.jpg" alt="Dokka Camping" border="0"/></a><br/><br/>
    <a href="http://www.sgh.no/" target="_blank"><img src="images/sponsors/sgh.jpg" alt="Gudbrandsdal Hotell" border="0"/></a><br/><br/>
  </div>
  <div class="Sponsortoppen"><img src="images/diverse/sponsorbunn.png" alt="bunn" width="124" height="22" border="0"/></div>
</div>"""


def nav_html(active, prefix=""):
    lines = []
    for item in NAV_ITEMS:
        href = prefix + NAV_HREFS[item]
        img = prefix + "images/menylinje/" + item + (".jpg" if item != active else "Rollover.jpg")
        rollover = prefix + "images/menylinje/" + item + "Rollover.jpg"
        lines.append(
            f'<a href="{href}" onmouseout="MM_swapImgRestore()" '
            f'onmouseover="MM_swapImage(\'{item}\',\'\',\'{rollover}\',1)">'
            f'<img src="{img}" alt="{item}" name="{item}" border="0"/></a>'
        )
    return "\n  ".join(lines)


def page(title, active, body, css_prefix="", nav_prefix=""):
    return f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="shortcut icon" href="{css_prefix}NPL Favicon.ico" />
<link rel="stylesheet" href="{css_prefix}nplstylesheet-utf8.css" type="text/css" />
<title>Norge P&#229; Langs med Montarou - {title}</title>
<script>window.RufflePlayer = window.RufflePlayer || {{}}; window.RufflePlayer.config = {{ autoplay: "on", unmuteOverlay: "hidden" }};</script>
<script src="https://unpkg.com/@ruffle-rs/ruffle"></script>
<script src="{css_prefix}equalcolumns.js" type="text/javascript"></script>
{JS_FUNCS}
</head>
<body>
{HEADER_HTML.replace('images/', css_prefix + 'images/').replace('Headermovie/', css_prefix + 'Headermovie/').replace('INDEXHREF', css_prefix + 'index.html')}
<br/><br/>
<div id="headermeny">
  {nav_html(active, nav_prefix)}
</div>
<div id="mainimage">
<br/><br/>
{body}
<div style="clear:both;"></div>
</div>
{FOOTER_HTML.replace('images/', css_prefix + 'images/')}
</body>
</html>"""


# ── HJEM ─────────────────────────────────────────────────────────────────────
HJEM_SISTENYTTSIDEBAR = """\
<div id="Sistenyttindeks">
  <div class="skillebilde"><img src="images/diverse/rammetopp.png" alt="topp" width="210" height="16" border="0"/></div>
  <div class="bakgrunnsideramme">
    <span class="overskrifthvit">SISTE NYTT...</span><br/>
    <hr/>
    <span class="ingresstekstboldm&#248;rkgr&#229;">Turlogg:</span><br/>
    <span class="vanligtekstmellomgr&#229;"><a href="turlogg.html">Andre dag p&#229; sykkel</a></span><br/>
    <span class="infotekst">19. Mai 2009, 13:00</span><br/><br/>
    <span class="vanligtekstmellomgr&#229;"><a href="turlogg.html">Avgang etappe 14!</a></span><br/>
    <span class="infotekst">18. Mai 2009, 12:00</span><br/><br/>
    <span class="vanligtekstmellomgr&#229;"><a href="turlogg.html">Bilder (igjen)</a></span><br/>
    <span class="infotekst">14. Mai 2009, 18:00</span><br/><br/>
    <span class="vanligtekstmellomgr&#229;"><a href="turlogg.html">Tilbakefall p&#229; Geilosyken</a></span><br/>
    <span class="infotekst">14. Mai 2009, 16:00</span><br/><br/>
    <hr/>
    <span class="ingresstekstboldm&#248;rkgr&#229;">Reisebrev:<br/></span>
    <a href="reisebrev.html#Etappe6">
    <table cellspacing="1"><tr>
      <td><img src="images/Reisebrev/Reisebrev0600.jpg" alt="Reisebrev" border="0"/></td>
      <td>Etappe 6: <br/>Hegra - Gressli<br/><span class="infotekst">10. November</span></td>
    </tr></table></a>
    <br/><hr/>
    <span class="ingresstekstboldm&#248;rkgr&#229;">Fotogalleri:</span>
    <a href="galleri.html#Etappe15">
    <table cellspacing="1"><tr>
      <td><img src="Galleri/Etappe15/Etappe15.jpg" alt="Etappe15" border="0"/></td>
      <td>Etappe 15:<br/>Ljosland - Lindesnes<br/><span class="infotekst">16. Mai</span></td>
    </tr></table></a>
    <br/><hr/>
    <span class="ingresstekstboldm&#248;rkgr&#229;">Videogalleri:</span><br/>
    <span class="vanligtekstmellomgr&#229;"><a href="galleri.html#video">Klipp fra oppvarmingsturen i Finland, mer kommer etter hvert...</a></span><br/>
    <span class="infotekst">05. Februar</span>
    <br/>&nbsp;<br/><hr/>
    <span class="ingresstekstboldm&#248;rkgr&#229;">Posisjon:</span><br/>
    <span class="vanligtekstmellomgr&#229;"><a href="reiserute.html#posisjon">Regelmessig oppdatering av hvor vi befinner oss.</a></span><br/>
  </div>
  <div class="skillebilde"><img src="images/diverse/rammebunn.png" alt="bunn" width="210" height="16" border="0"/></div>
  <br/>
  <div class="skillebilde"><img src="images/diverse/rammetopp.png" alt="topp" width="210" height="16" border="0"/></div>
  <div class="bakgrunnsideramme">
    <span class="overskrifthvit">LENKER</span><hr/>
    <p class="vanligtekstmellomgr&#229;">Rasmus og Eike sin friluftsblogg<br/><a href="http://www.norgepaakryssogtvers.net" target="_blank">www.norgepaakryssogtvers.net</a></p>
    <p class="vanligtekstmellomgr&#229;">Jens Nilsens telemarksklubb!<br/><a href="http://www.halddetoppen.no" target="_blank">www.halddetoppen.no</a></p>
    <p class="vanligtekstmellomgr&#229;">Magasin for naturopplevelse<br/><a href="http://www.friluftsliv.no/ekspedisjoner" target="_blank">www.friluftsliv.no</a></p>
    <br/><hr/>
    <span class="ingresstekstboldm&#248;rkgr&#229;"><strong>NPL-Ekspedisjoner<br/> vi har m&#248;tt:</strong></span>
    <p class="vanligtekstmellomgr&#229;">Oddvar og Anne<br/><a href="http://www.repstad.net" target="_blank">www.repstad.net</a></p>
    <p class="vanligtekstmellomgr&#229;">Frederik<br/><a href="http://www.frederikpaatur.blogspot.com" target="_blank">www.frederikpaatur.blogspot.com</a></p>
    <p class="vanligtekstmellomgr&#229;">Tom og Simon<br/><a href="http://www.keeperifokus.no" target="_blank">www.keeperifokus.no</a></p>
    <p class="vanligtekstmellomgr&#229;">Tonice og Arnt Helge<br/><a href="http://www.tureroveralt.no" target="_blank">www.tureroveralt.no</a></p><br/>
  </div>
  <div class="skillebilde"><img src="images/diverse/rammebunn.png" alt="bunn" width="210" height="16" border="0"/></div>
  <br/>
  <div class="skillebilde"><img src="images/diverse/rammetopp.png" alt="topp" width="210" height="16" border="0"/></div>
  <div class="bakgrunnsideramme">
    <span class="overskrifthvit">PRESSE</span><hr/><br/>
    <a href="http://www.arcticfemme.com/index.php?option=com_content&amp;view=article&amp;id=76" target="_blank"><img src="images/diverse/arcticfemme.jpg" alt="arctic femme" name="arcticfemme" width="168" height="30" border="0"/></a><br/><br/>
    <a href="http://www.saltenposten.no/nyheter/article191213.ece" target="_blank"><img src="images/diverse/saltenposten.jpg" alt="saltenposten" name="saltenposten" width="168" height="37" border="0"/></a><br/><br/>
    <a href="http://www.nordlys.no/nyheter/article3875706.ece" target="_blank"><img src="images/diverse/nordlys.png" alt="nordlys.no" name="nordlys.no" width="168" height="58" border="0"/></a><br/><br/>
    <a href="http://www.eventyrblogg.com/default.asp?Newsid=267&amp;side=nyheter" target="_blank"><img src="images/diverse/gamme.png" alt="gamme.no" name="gamme.no" width="168" height="58" border="0"/></a>
  </div>
  <div class="skillebilde"><img src="images/diverse/rammebunn.png" alt="bunn" width="210" height="16" border="0"/></div>
</div>"""

HJEM_BODY = f"""\
<div id="main" class="vanligtekst">
{HJEM_SISTENYTTSIDEBAR}
{SPONSORLISTE_HTML}

<p class="ingresstekst"><img src="images/diverse/Velkommen.jpg" alt="Velkommen"/><br/>
Da er det endelig avgjort at det blir langtur! Norge skal krysses fra nord til s&#248;r det kommende &#229;ret!
H&#248;sten 2008 setter to glade vandrere ut fra Nordkapp i h&#229;p om &#229; n&#229; helskinnet gjennom v&#229;r
langsg&#229;ende rute nedover Norges land. Ruta vil inneholde vidder, skoger og fjell kledd i nesten alle &#229;rstidene.
Tidsperspektivet er ca seks m&#229;neder, tre f&#248;r jul og tre etter.</p>

<p>Hvorfor sp&#248;r mange. Et stort sp&#248;rsm&#229;l for noen, helt naturlig for andre. Er det en flukt fra hverdagen?
En asketisk &#248;velse? En test eller en utfordring? En s&#248;ken etter noe annet? En annerledes hverdag?
Antageligvis litt av alle disse tingene, men fremfor alt handler det om &#229; leve ute i og med naturen over tid.
Ren glede over &#229; v&#230;re ute og bryne seg p&#229; naturens meny av utfordringer; holde varmen, bli mett,
finne en god leirplass, eller f&#229; liv i b&#229;let.</p>

<p>Jeg legger p&#229; ingen m&#229;te skjul p&#229; at &#229; legge vekk klokka, mobilen og universitetet er noe av poenget &#229;
komme n&#230;rmere noe vi stadig beveger oss bort fra i hverdagen. Hva dette noe er h&#229;per jeg &#229; finne ut.
Det vil i s&#229; fall bli publisert her!</p>

<p>Viktig er det ogs&#229; &#229; nevne at dette ikke er et rekordsfors&#248;k. Snarere tvert imot. Her er veien m&#229;let.
Det &#229; kunne se mot horisonten vitende om at bak den er en ny horisont, og bak den enda en, og tenke at
&#171;over den skal vi&#187; blir et eventyr. Vi legger bort vekkerklokka, timeplanen og de andre heftelsene som h&#248;rer
sivilisasjonen til og lar bekymringene dreie seg om &#229; holde varmen, finne brensel, f&#229; &#248;rret i gryta og t&#248;rke sokker.</p>

<p>P&#229; denne siden vil vi pr&#248;ve &#229; holde deg oppdatert p&#229; hva som skjer, s&#229; du kan f&#229; med deg alt som g&#229;r galt og glatt underveis.</p>

<p>F&#248;r Norge p&#229; langs 08/09 skal jeg p&#229; en m&#229;neds kanotur i Nord-Finland. Det blir en glimrende innledning til livet i villmarken!
Bilder fra denne turen vil ogs&#229; bli lagt ut p&#229; denne siden.</p>

<img src="images/diverse/SignaturLiten.jpg" alt="Marius" width="190" height="46" align="right"/>
<div id="clearfooter"></div>
</div>"""

# ── OMOSS ────────────────────────────────────────────────────────────────────

def read_omtale(name):
    path = os.path.join(PHP_ROOT, f"Omtale{name}.php")
    if not os.path.exists(path):
        return f"<p>(Profil ikke tilgjengelig)</p>"
    with open(path, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("iso-8859-1")
    return text

OMTALE_PEOPLE = ["Montarou", "Truls", "Emil", "Vegard", "Jarle",
                  "Andreas", "Sverre", "Rasmus", "Anders", "Karin"]

def build_omoss():
    sidebar_items = []
    for p in OMTALE_PEOPLE:
        sidebar_items.append(f"""<tr><td>
  <div id="OmOssbolk">
    <a name="{p}"></a>
    <a href="omoss.html#{p}" onclick="showProfile('{p}'); return false;"
       onmouseover="MM_swapImage('{p}','','images/omtalebilder/{p}.jpg',1)"
       onmouseout="MM_swapImgRestore()">
      <img id="thumb_{p}" src="images/omtalebilder/{p}svartkvitt.jpg" alt="{p}" name="{p}" width="70" height="70" border="0"/></a>
    <br/><strong>{p}</strong>
  </div>
</td></tr>""")

    profile_divs = []
    for p in OMTALE_PEOPLE:
        bio = read_omtale(p)
        display = "block" if p == "Montarou" else "none"
        profile_divs.append(f"""<div id="profile_{p}" style="display:{display};">
<table><tr>
  <td><img src="images/omtalebilder/profilbildevertikal{p}.jpg" class="profilbilde" alt="{p}"/></td>
  <td valign="top" width="500">{bio}</td>
</tr></table>
</div>""")

    js = """<script type="text/javascript">
var people = """ + str(OMTALE_PEOPLE).replace("'", '"') + """;
function showProfile(name) {
  people.forEach(function(p) {
    document.getElementById('profile_' + p).style.display = (p === name) ? 'block' : 'none';
    document.getElementById('thumb_' + p).src = (p === name)
      ? 'images/omtalebilder/' + p + '.jpg'
      : 'images/omtalebilder/' + p + 'svartkvitt.jpg';
  });
}
</script>"""

    body = f"""\
<div id="main" class="vanligtekst">
{js}
<div id="OmOssWrap">
<table>{''.join(sidebar_items)}</table>
</div>
<p>{''.join(profile_divs)}</p>
<div id="clearfooter"></div>
</div>"""
    return body


# ── REISERUTE ────────────────────────────────────────────────────────────────
REISERUTE_BODY = f"""\
<div id="main" class="vanligtekst">
{SPONSORLISTE_HTML}

<p class="ingresstekst">Turen starter fra Nordkapp 1. september og f&#248;lger en variert rute s&#248;rover,
fordelt p&#229; ca 15 etapper. Vi planlegger &#229; n&#229; Mo i Rana f&#248;r vi unner oss en pust i bakken ved
juletider. Turen fortsetter videre mot Lindesnes p&#229; v&#229;rparten.</p>
</br>

<div id="Reiserutediv">
  <object type="application/x-shockwave-flash" data="Reiserutemovie/Reiserute.swf" width="400" height="698">
    <param name="movie" value="Reiserutemovie/Reiserute.swf"/>
    <param name="quality" value="high"/>
    <param name="bgcolor" value="#000000"/>
  </object>
  <p>&nbsp;</p>
  <div id="spotkart">
    <a name="posisjon"></a><p>Regelmessig oppdatering av posisjon:</p>
    <iframe width="300" height="500" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
    src="https://maps.google.com/maps/ms?hl=no&amp;ie=UTF8&amp;source=embed&amp;msa=0&amp;msid=112603399891671341524.0004640612cf1279b0078&amp;ll=61.48076,9.272461&amp;spn=10.525632,13.183594&amp;z=5&amp;output=embed">
    </iframe><br/>
    <small><a href="https://maps.google.com/maps/ms?hl=no&amp;ie=UTF8&amp;source=embed&amp;msa=0&amp;msid=112603399891671341524.0004640612cf1279b0078&amp;ll=61.48076,9.272461&amp;spn=10.525632,13.183594&amp;z=5" style="color:#0000FF;text-align:left" target="_blank">Vis st&#248;rre kart</a></small>
  </div>
</div>

<span class="ingresstekst"><strong>H&#248;st-etapper:</strong></span></br>
<hr/>
<p><strong>1. Nordkapp - Skaidi</strong><br/>8 dager, hvorav 1 hvile, 125 km<br/>Her blir det pr&#248;ving og feiling, og ikke minst tilvenning av kroppen til belastningen.</p>
<p><strong>2. Skaidi - Kautokeino (Via Masi)</strong><br/>12 dager, hvorav 2 hvile, 220 km<br/>Her m&#229; vi sette opp farten litt, komme skikkelig i gang med kilometerslukingen.</p>
<p><strong>3. Kautokeino - Abisko/Narvik</strong><br/>12 dager, hvorav 1 hvile, 250 km<br/>Skikkelig lang etappe. Vi g&#229;r innom Finland og Sverige p&#229; veien.</p>
<p><strong>4. Narvik - Fauske/Sulitjelma</strong><br/>14 dager, hvorav 2 hviledager, 230 km<br/>Ved Fauske venter resten av kartene ned til Mer&#229;ker, samt et lass med Drytech-poser.</p>
<p><strong>5. Sulitjelma - L&#248;nsdal</strong><br/>8 dager, hvorav 1 hvile, 90 km<br/>Deilig etappe!</p>
<p><div id="Reiserutenotabene"><em>Som tidligere antatt er Saltfjellet slukt av vinteren tidlig i november. Vi har av erfaring (over Skjomenfjellene) l&#230;rt at det ikke har noen hensikt &#229; jobbe mot naturen. For &#229; kunne fortsette til fots dro vi s&#248;rover til Hegra og gikk den siste h&#248;stetappen til Gressli. N&#229;r vi begynner p&#229; igjen med ski under beina i februar, vil vi starte n&#248;yaktig der vi slapp i Nord-Norge, n&#230;rmere bestemt L&#248;nsdal.</em></div></p>
<p><strong>6. Hegra - Gressli</strong><br/>6 dager, hvorav 1 hviledag, 80 km<br/>Vi drar s&#248;rover for &#229; kunne fortsette ferden til fots. Meget naturskj&#248;nn og fin etappe.</p>
<p>&nbsp;</p>
<span class="ingresstekst"><strong>V&#229;r-etapper:</strong></span></br>
<hr/>
<p><strong>7. L&#248;nsdal - Umbukta</strong><br/>10 dager hvorav 2 hvile, 220 km<br/>Fra Kjem&#229;vatnet videre til Saltfjellstua gjennom steindalen.</p>
<p><strong>8. Umbukta - Nordli</strong><br/>7 dager, hvorav 1 hvile, 140 km<br/>Ned Susendalen gjennom B&#248;rgefjell.</p>
<p><strong>9. S&#248;rli - Mer&#229;ker (Hegra)</strong><br/>10 dager, hvorav 2 hvile, 180 km<br/>Mot Gressm&#248;en, kanskje innom Holden.</p>
<p><strong>10. Tydal (Gressli) - Elg&#229;</strong><br/>7 dager, hvorav 1 hvile, 120 km<br/>Fra Tydal mot Kj&#248;lihytta, videre vest for eller over Aursunden.</p>
<p><strong>11. Elg&#229; - Ringebu (del I)</strong><br/>8 dager, hvorav 1 hvile, 140 km<br/>S&#248;r-vestover mot Otnes nord for S&#248;lensj&#248;en.</p>
<p><strong>11. Ringebu - Fagernes (del II)</strong><br/>4 dager, 90 km<br/>Fra Ringebu mot Fagerh&#248;i.</p>
<p><strong>12. Fagernes - Geilo</strong><br/>5 dager, 120 km<br/>Fra Fagernes mot Tisleia.</p>
<p><strong>13. Ustaoset - Haukeliseter</strong><br/>8 dager, hvorav 1 hvile<br/>Rutebeskrivelse: Ustaoset - Tuva - Heins&#230;ter - Rauhellern - Sandhaug - Litlos - Hellevassbu - Haukeliseter.</p>
<p><strong>14. Haukeliseter - Ljosland</strong><br/>10 dager, forh&#229;pentligvis 2 hviledager, 170 km<br/>Rutebeskrivelse: Haukeliseter - Holmavasshytta - via Sloaros - Bossbu - Svartenut - &#216;yuvsbu - Gaukhei - Ljosland.</p>
<p><strong>15. Ljosland - Lindesnes</strong><br/>5/6 dager - sjarm&#248;retappen, 140 km<br/>Med kano fra Ljosland fjellstue, langs Monn, mot &#216;seral og &#216;revatnet. G&#229;r til fots fra hhv Vigeland eller Mandal ut til fyret p&#229; Lindesnes.</p>
<div id="clearfooter"></div>
</div>"""


# ── TURLOGG ───────────────────────────────────────────────────────────────────
TURLOGG_BODY = """\
<div id="main" class="vanligtekst">
<br/>
<p class="vanligtekst">Vi jobber med &#229; gjenopprette innholdet.</p>
<br/>
<div id="Turloggvenstre">
<p><span class="turloggoverskriftoransj">Andre dag p&#229; sykkel</span><br/>
<span class="infotekst">19. Mai 2009, 13:00</span></p>
<p><span class="turloggoverskriftoransj">Bilder (igjen)</span><br/>
<span class="infotekst">14. Mai 2009, 18:00</span></p>
<p><span class="turloggoverskriftoransj">Skisesongen over for i &#229;r</span><br/>
<span class="infotekst">5. Mai 2009, 12:00</span></p>
</div>
<div id="Turloggh&#248;yre">
<p><span class="turloggoverskriftoransj">Avgang etappe 14!</span><br/>
<span class="infotekst">18. Mai 2009, 12:00</span></p>
<p><span class="turloggoverskriftoransj">Tilbakefall p&#229; Geilosyken</span><br/>
<span class="infotekst">14. Mai 2009, 16:00</span></p>
<p><span class="turloggoverskriftoransj">Siste dag p&#229; etappe 13</span><br/>
<span class="infotekst">4. Mai 2009, 15:00</span></p>
</div>
<div id="clear"></div>
</div>"""


# ── GJESTEBOK ────────────────────────────────────────────────────────────────
GJESTEBOK_BODY = """\
<div id="main" class="vanligtekst">
<br/>
<div id="Gjesteboka">
<p class="vanligtekst">Vi jobber med &#229; gjenopprette innholdet.</p>
</div>
<div id="clear"></div>
</div>"""


# ── REISEBREV INDEX ───────────────────────────────────────────────────────────
def make_reisebrev_index():
    entries = [
        ("1", "Nordkapp - Skaidi", "Mandag 08. September 2008", "Montarou",
         "venstre", "Reisebrev0101.jpg", "267", "200",
         "De f&#248;rste skrittene er tatt og s&#229; er eventyret i gang. "
         "Overgangen fra &#229; skulle gj&#248;re det til &#229; gj&#248;re det, &#229; faktisk v&#230;re i gang, "
         "er som en prikk p&#229; tidslinjen; du vet ikke at du er der f&#248;r du ser tilbake og finner "
         "deg selv p&#229; andre siden av det kritiske punktet."),
        ("2", "Skaidi - Kautokeino", "Mandag 22. September 2008", "Montarou",
         "h&#248;yre", "Reisebrev0201.jpg", "183", "200",
         "Vi g&#229;r og g&#229;r, toppene forsvinner bak oss og det er rart at det vi ser bak oss &#8211; et "
         "endel&#248;st landskap s&#229; langt &#248;yet kan se &#8211; har vi g&#229;tt gjennom skritt for skritt."),
        ("3", "Kautokeino - Narvik", "Onsdag 08. Oktober 2008", "Montarou",
         "venstre", "Reisebrev0301.jpg", "196", "200",
         "Det er ingen tvil. Vinteren kommer enten vi liker det eller ei. Enkelte netter ligger sn&#248;en "
         "tung p&#229; teltet, og at vannposen f&#229;r et centimeters tykt lag is i l&#248;pet av natten begynner &#229; bli vanlig."),
        ("4", "Abisko/Narvik - Fauske (Sulitjelma)", "L&#248;rdag 25. Oktober 2008", "Montarou",
         "h&#248;yre", "Reisebrev0401.jpg", "207", "200",
         "Det handler om kontraster. En uavbrutt rekke av kontraster. De gir seg oftest til kjenne gjennom "
         "behov/tilfredsstillelse eller kanskje rettere sagt ubehag/behag."),
        ("5", "Fauske (Sulitjelma) - L&#248;nsdal", "S&#248;ndag 02. November 2008", "Montarou",
         "venstre", "Reisebrev0501.jpg", "247", "200",
         "Femte etappe er over og vi er like ved polarsirkelen. Det har v&#230;rt en deilig uke med ekstra mat, "
         "bra v&#230;r, sympatiske dagsetapper og godt selskap."),
        ("6", "Hegra - Gressli", "Mandag 10. November 2008", "Montarou",
         "h&#248;yre", "Reisebrev0601.jpg", "207", "200",
         "Oktober har blitt til november. Enda en m&#229;ned har passert og gjort sinnet rikere og midjen smalere. "
         "Vi har blitt n&#248;dt til &#229; flytte prosjektet s&#248;rover som tidligere antatt."),
    ]
    parts = []
    for num, title, date, author, side, img, w, h, excerpt in entries:
        if side == "venstre":
            flex_dir = "row"
            img_html = f'<a href="reisebrev{num}.html"><img src="images/Reisebrev/{img}" class="reisebrevbildevenstre" border="0" width="{w}" height="{h}"/></a>'
            link_align = "right"
        else:
            flex_dir = "row-reverse"
            img_html = f'<a href="reisebrev{num}.html"><img src="images/Reisebrev/{img}" class="reisebrevbildeh&#248;yre" border="0" width="{w}" height="{h}"/></a>'
            link_align = "left"
        parts.append(f"""\
<div id="reisebrev" style="flex-direction:{flex_dir};">
{img_html}
<div>
<a name="Etappe{num}"></a><span class="ingresstekstbold"><a href="reisebrev{num}.html">Etappe {num}: {title}</a></span><br/>
<span class="infotekst">{date} av: {author}</span><br/>
<p>{excerpt}</p>
<p style="text-align:{link_align};"><a href="reisebrev{num}.html" class="ingresstekst">les mer... &gt;&gt;</a></p>
</div>
</div>""")

    return f"""\
<div id="main" class="vanligtekst">
{SPONSORLISTE_HTML}
{''.join(parts)}
</div>"""


def read_reisebrev(num):
    path = os.path.join(PHP_ROOT, f"Reisebrev{num}.php")
    with open(path, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("iso-8859-1")
    # Fix internal links
    text = text.replace("index.php?side=Reisebrev", "reisebrev.html")
    return text


# ── GALLERI ───────────────────────────────────────────────────────────────────
GALLERI_BODY = """\
<div id="main" class="vanligtekst">

<a href="galleri.html"><span class="gallerivalgactive">fotogalleri</span></a>
&nbsp;&nbsp;&nbsp;
<a href="videogalleri.html"><span class="gallerivalgpassive">videogalleri</span></a>

<hr width="860" align="left"/>
<br/><br/>

<div id="fototable">
<div id="norgekart">
<img src="images/kartfotogalleri/norgekart.png" alt="norgekart" border="0"/>
</div>

<div id="oppvarming">
<table cellspacing="10"><tr>
  <td align="center" width="120">
    <a href="Galleri/Oppvarmingstur/index.html">
      <img src="Galleri/Oppvarmingstur/Oppvarmingstur.gif" alt="Oppvarmingstur" border="0"/><br/>
      Oppvarmingstur<br/>i Finland<br/>
      <div class="infotekst">(55 bilder)</div>
    </a>
  </td>
</tr></table>
</div>

<div id="fotowrap">
<table cellspacing="10">
<tr>
<td align="center" width="120"><a href="Galleri/Etappe1/index.html">
  <img src="Galleri/Etappe1/Etappe1.gif" alt="Etappe1" border="0"/><br/>Etappe 1:<br/>Nordkapp - Skaidi<br/><div class="infotekst">(38 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe1.png" alt="Etappe1" border="0"/></span></a></td>
<td align="center" width="120"><a href="Galleri/Etappe2/index.html">
  <img src="Galleri/Etappe2/Etappe2.gif" alt="Etappe2" border="0"/><br/>Etappe 2:<br/>Skaidi - Kautokeino<br/><div class="infotekst">(79 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe2.png" alt="Etappe2" border="0"/></span></a></td>
<td align="center" width="120"><a href="Galleri/Etappe3/index.html">
  <img src="Galleri/Etappe3/Etappe3.gif" alt="Etappe3" border="0"/><br/>Etappe 3:<br/>Kautokeino - Abisko<br/><div class="infotekst">(59 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe3.png" alt="Etappe3" border="0"/></span></a></td>
</tr>
<tr>
<td align="center"><a href="Galleri/Etappe4/index.html">
  <img src="Galleri/Etappe4/Etappe4.gif" alt="Etappe4" border="0"/><br/>Etappe 4:<br/>Narvik - Fauske<br/><div class="infotekst">(98 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe4.png" alt="Etappe4" border="0"/></span></a></td>
<td align="center"><a href="Galleri/Etappe5/index.html">
  <img src="Galleri/Etappe5/Etappe5.gif" alt="Etappe5" border="0"/><br/>Etappe 5:<br/>Fauske - L&#248;nsdal<br/><div class="infotekst">(94 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe5.png" alt="Etappe5" border="0"/></span></a></td>
<td align="center"><a href="Galleri/Etappe6/index.html">
  <img src="Galleri/Etappe6/Etappe6.gif" alt="Etappe6" border="0"/><br/>Etappe 6:<br/>Hegra - Gressli<br/><div class="infotekst">(88 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe6.png" alt="Etappe6" border="0"/></span></a></td>
</tr>
<tr>
<td align="center"><a name="Etappe7" href="Galleri/Etappe7/index.html">
  <img src="Galleri/Etappe7/Etappe7.gif" alt="Etappe7" border="0"/><br/>Etappe 7:<br/>L&#248;nsdal - Umbukta<br/><div class="infotekst">(48 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe7.png" alt="Etappe7" border="0"/></span></a></td>
<td align="center"><a name="Etappe8" href="Galleri/Etappe8/index.html">
  <img src="Galleri/Etappe8/Etappe8.gif" alt="Etappe8" border="0"/><br/>Etappe 8:<br/>Umbukta - Nordli<br/><div class="infotekst">(44 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe8.png" alt="Etappe8" border="0"/></span></a></td>
<td align="center"><a name="Etappe9" href="Galleri/Etappe9/index.html">
  <img src="Galleri/Etappe9/Etappe9.gif" alt="Etappe9" border="0"/><br/>Etappe 9:<br/>S&#248;rli - Mer&#229;ker<br/><div class="infotekst">(49 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe9.png" alt="Etappe9" border="0"/></span></a></td>
</tr>
<tr>
<td align="center"><a name="Etappe10" href="Galleri/Etappe10/index.html">
  <img src="Galleri/Etappe10/Etappe10.gif" alt="Etappe10" border="0"/><br/>Etappe 10:<br/>Tydal - Elg&#229;<br/><div class="infotekst">(71 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe10.png" alt="Etappe10" border="0"/></span></a></td>
<td align="center"><a name="Etappe11" href="Galleri/Etappe11/index.html">
  <img src="Galleri/Etappe11/Etappe11.gif" alt="Etappe11" border="0"/><br/>Etappe 11:<br/>Elg&#229; - Fagernes<br/><div class="infotekst">(56 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe11.png" alt="Etappe11" border="0"/></span></a></td>
<td align="center"><a name="Etappe12" href="Galleri/Etappe12/index.html">
  <img src="Galleri/Etappe12/Etappe12.gif" alt="Etappe12" border="0"/><br/>Etappe 12:<br/>Fagernes - Geilo<br/><div class="infotekst">(30 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe12.png" alt="Etappe12" border="0"/></span></a></td>
</tr>
<tr>
<td align="center"><a name="Etappe13" href="Galleri/Etappe13/index.html">
  <img src="Galleri/Etappe13/Etappe13.gif" alt="Etappe13" border="0"/><br/>Etappe 13:<br/>Ustaoset - Haukeliseter<br/><div class="infotekst">(75 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe13.png" alt="Etappe13" border="0"/></span></a></td>
<td align="center"><a name="Etappe14" href="Galleri/Etappe14/index.html">
  <img src="Galleri/Etappe14/Etappe14.jpg" alt="Etappe14" border="0"/><br/>Etappe 14:<br/>Haukeliseter - Ljosland<br/><div class="infotekst">(25 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe14.png" alt="Etappe14" border="0"/></span></a></td>
<td align="center"><a name="Etappe15" href="Galleri/Etappe15/index.html">
  <img src="Galleri/Etappe15/Etappe15.jpg" alt="Etappe15" border="0"/><br/>Etappe 15:<br/>Ljosland - Lindesnes<br/><div class="infotekst">(37 bilder)</div>
  <span><img src="images/kartfotogalleri/Etappe15.png" alt="Etappe15" border="0"/></span></a></td>
</tr>
</table>
</div>
</div>
<div id="clear"></div>
</div>"""


# ── VIDEO GALLERI ─────────────────────────────────────────────────────────────
VIDEOS = [
    ("vid1", "5An_8LozHB0", "Fjernsynskj&#248;kkenet, Episode 1", "Idag: hjemmelaget br&#248;d"),
    ("vid2", "ez5pVtzbmIg", "Ronny og stor&#248;rreten", "Kilos&#248;rret p&#229; kroken"),
    ("vid3", "WmM8az1Ql14", "Fjernsynskj&#248;kkenet, Episode 2", "Idag: pannekaker og camp-utsikt"),
    ("vid4", "K7v6iB05Ofw", "Kampen med Storgjedda", "Montarou drar i land et smakfullt udyr"),
    ("vid5", "lkf7TvXuDIU", "Nestenkanovelt", "Farlig n&#230;r katastrofe"),
    ("vid6", "3JrKnijl7wA", "Status dag 7", "Truls presenterer ukesrapport"),
]

def build_videogalleri():
    sidebar = "\n".join(
        f'<tr><td><div id="videotablebolk"><a href="videogalleri.html#{vid}" onclick="showVideo(\'{ytid}\'); return false;"><strong>{title}</strong><br/>{desc}</a></div></td></tr>'
        for vid, ytid, title, desc in VIDEOS
    )
    first_ytid = VIDEOS[0][1]
    js = f"""<script type="text/javascript">
function showVideo(ytid) {{
  document.getElementById('yt-frame').src = 'https://www.youtube.com/embed/' + ytid;
}}
</script>"""
    return f"""\
<div id="main" class="vanligtekst">
<a href="galleri.html"><span class="gallerivalgpassive">fotogalleri</span></a>
&nbsp;&nbsp;&nbsp;
<a href="videogalleri.html"><span class="gallerivalgactive">videogalleri</span></a>
<hr width="860" align="left"/>
<br/><br/>
{js}
<div id="videotablewrap">
<div id="videotable">
<table>
{sidebar}
</table>
</div>
</div>
<div id="videogalleri">
<iframe id="yt-frame" width="560" height="315"
  src="https://www.youtube.com/embed/{first_ytid}"
  frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen></iframe>
</div>
<div id="clear"></div>
</div>"""


# ── SPONSORER ─────────────────────────────────────────────────────────────────
def read_php_body(name):
    path = os.path.join(PHP_ROOT, f"{name}.php")
    with open(path, "rb") as f:
        raw = f.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("iso-8859-1")


_SPONSORLISTE_PHP_BLOCK = '<div id="Sponsorliste">\r\n\t\t<?php include("Sponsorliste.html"); ?>\r\n\t</div>'


def build_sponsorer():
    body = read_php_body("Sponsorer")
    body = body.replace(_SPONSORLISTE_PHP_BLOCK, SPONSORLISTE_HTML)
    return body


def build_utstyr():
    body = read_php_body("Utstyr")
    body = body.replace(_SPONSORLISTE_PHP_BLOCK, SPONSORLISTE_HTML)
    return body


# ── GALLERY PAGES ────────────────────────────────────────────────────────────
GALLERIES = {
    "Etappe1":  ("Etappe 1: Nordkapp - Skaidi", "../../"),
    "Etappe2":  ("Etappe 2: Skaidi - Kautokeino", "../../"),
    "Etappe3":  ("Etappe 3: Kautokeino - Abisko", "../../"),
    "Etappe4":  ("Etappe 4: Narvik - Fauske", "../../"),
    "Etappe5":  ("Etappe 5: Fauske - Lønsdal", "../../"),
    "Etappe6":  ("Etappe 6: Hegra - Gressli", "../../"),
    "Etappe7":  ("Etappe 7: Lønsdal - Umbukta", "../../"),
    "Etappe8":  ("Etappe 8: Umbukta - Nordli", "../../"),
    "Etappe9":  ("Etappe 9: Sørli - Meråker", "../../"),
    "Etappe10": ("Etappe 10: Tydal - Elgå", "../../"),
    "Etappe11": ("Etappe 11: Elgå - Fagernes", "../../"),
    "Etappe12": ("Etappe 12: Fagernes - Geilo", "../../"),
    "Etappe13": ("Etappe 13: Ustaoset - Haukeliseter", "../../"),
    "Etappe14": ("Etappe 14: Haukeliseter - Ljosland", "../../"),
    "Etappe15": ("Etappe 15: Ljosland - Lindesnes", "../../"),
    "Oppvarmingstur": ("Oppvarmingstur i Finland", "../../"),
}

LIGHTBOX_JS = """\
<script type="text/javascript">
var images = [];
var current = 0;
function openLightbox(idx) {
  current = idx;
  document.getElementById('lb-img').src = images[idx].src;
  document.getElementById('lb-cap').textContent = images[idx].cap || '';
  document.getElementById('lb-counter').textContent = (idx+1) + ' / ' + images.length;
  document.getElementById('lightbox').style.display = 'flex';
}
function closeLightbox() { document.getElementById('lightbox').style.display = 'none'; }
function lbPrev() { openLightbox((current - 1 + images.length) % images.length); }
function lbNext() { openLightbox((current + 1) % images.length); }
document.addEventListener('keydown', function(e) {
  if (document.getElementById('lightbox').style.display === 'flex') {
    if (e.key === 'ArrowLeft') lbPrev();
    else if (e.key === 'ArrowRight') lbNext();
    else if (e.key === 'Escape') closeLightbox();
  }
});
</script>"""

LIGHTBOX_CSS = """\
<style>
#lightbox {
  display: none; position: fixed; top: 0; left: 0;
  width: 100%; height: 100%; background: rgba(0,0,0,0.92);
  z-index: 9999; align-items: center; justify-content: center; flex-direction: column;
}
#lb-inner { position: relative; max-width: 95vw; max-height: 90vh; text-align: center; }
#lb-img { max-width: 90vw; max-height: 80vh; border: 3px solid #fff; }
#lb-cap { color: #ccc; font-family: Arial,sans-serif; font-size: 14px; margin-top: 8px; }
#lb-counter { color: #666; font-family: Arial,sans-serif; font-size: 12px; margin-top: 4px; }
.lb-btn {
  position: absolute; top: 50%; transform: translateY(-50%);
  background: rgba(0,0,0,0.5); color: #fff; border: none; font-size: 28px;
  cursor: pointer; padding: 8px 16px; z-index: 10000;
}
#lb-prev { left: -60px; }
#lb-next { right: -60px; }
#lb-close {
  position: fixed; top: 20px; right: 30px; font-size: 36px; color: #fff;
  cursor: pointer; background: none; border: none; z-index: 10001;
}
.thumb-grid { display: flex; flex-wrap: wrap; gap: 4px; padding: 20px; justify-content: center; max-width: 800px; margin: 0 auto; }
.thumb-grid img { cursor: pointer; border: 2px solid #333; max-width: 100px; max-height: 100px; width: auto; height: auto; }
.thumb-grid img:hover { border-color: #ffb20a; }
</style>"""

def parse_gallery_xml(gal_name):
    xml_path = os.path.join(ROOT, "Galleri", gal_name, "gallery.xml")
    if not os.path.exists(xml_path):
        return []
    tree = ET.parse(xml_path)
    root = tree.getroot()
    items = []
    for img in root.findall("image"):
        fn = img.findtext("filename", "").strip()
        cap = img.findtext("caption", "").strip()
        if fn:
            items.append((fn, cap))
    return items

def build_gallery_page(gal_name):
    title, prefix = GALLERIES[gal_name]
    items = parse_gallery_xml(gal_name)

    thumb_html_parts = []
    js_images = []
    for i, (fn, cap) in enumerate(items):
        src = f"images/{fn}"
        thumb = f"thumbs/{fn}"
        safe_cap = cap.replace("'", "\\'").replace('"', '&quot;')
        thumb_html_parts.append(
            f'<img src="{thumb}" alt="{safe_cap}" '
            f'onclick="openLightbox({i})" title="{safe_cap}"/>'
        )
        js_images.append(f'{{src:"{src}",cap:"{safe_cap}"}}')

    nav_lines = []
    nav_names = ["Hjem","OmOss","Reiserute","Utstyr","Turlogg","Reisebrev","Galleri","Gjestebok","Sponsorer"]
    nav_hrefs_gallery = {
        "Hjem": prefix + "index.html",
        "OmOss": prefix + "omoss.html",
        "Reiserute": prefix + "reiserute.html",
        "Utstyr": prefix + "utstyr.html",
        "Turlogg": prefix + "turlogg.html",
        "Reisebrev": prefix + "reisebrev.html",
        "Galleri": prefix + "galleri.html",
        "Gjestebok": prefix + "gjestebok.html",
        "Sponsorer": prefix + "sponsorer.html",
    }
    for item in nav_names:
        href = nav_hrefs_gallery[item]
        img_src = prefix + "images/menylinje/" + item + ".jpg"
        rollover = prefix + "images/menylinje/" + item + "Rollover.jpg"
        nav_lines.append(
            f'<a href="{href}" onmouseout="MM_swapImgRestore()" '
            f'onmouseover="MM_swapImage(\'{item}\',\'\',\'{rollover}\',1)">'
            f'<img src="{img_src}" alt="{item}" name="{item}" border="0"/></a>'
        )

    header_replaced = HEADER_HTML.replace('images/', prefix + 'images/').replace('Headermovie/', prefix + 'Headermovie/').replace('INDEXHREF', prefix + 'index.html')
    footer_replaced = FOOTER_HTML.replace('images/', prefix + 'images/')

    return f"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="shortcut icon" href="{prefix}NPL Favicon.ico" />
<link rel="stylesheet" href="{prefix}nplstylesheet-utf8.css" type="text/css" />
<title>{title}</title>
<script>window.RufflePlayer = window.RufflePlayer || {{}}; window.RufflePlayer.config = {{ autoplay: "on", unmuteOverlay: "hidden" }};</script>
<script src="https://unpkg.com/@ruffle-rs/ruffle"></script>
<script src="{prefix}equalcolumns.js" type="text/javascript"></script>
{JS_FUNCS}
{LIGHTBOX_CSS}
</head>
<body>
{header_replaced}
<br/><br/>
<div id="headermeny">
  {'  '.join(nav_lines)}
</div>
<div id="mainimage">
<br/>
<p style="text-align:center;">
  <a href="{prefix}galleri.html" style="color:#ffb20a;font-size:14px;">&laquo; Tilbake til galleri</a>
  &nbsp;&nbsp;&nbsp;
  <span style="color:#fff;font-size:18px;font-weight:bold;">{title}</span>
</p>

<div id="lightbox">
  <button id="lb-close" onclick="closeLightbox()">&#215;</button>
  <div id="lb-inner">
    <button class="lb-btn" id="lb-prev" onclick="lbPrev()">&#8249;</button>
    <img id="lb-img" src="" alt=""/>
    <button class="lb-btn" id="lb-next" onclick="lbNext()">&#8250;</button>
  </div>
  <div id="lb-cap"></div>
  <div id="lb-counter"></div>
</div>

<div class="thumb-grid">
{''.join(thumb_html_parts)}
</div>

{LIGHTBOX_JS}
<script>images = [{','.join(js_images)}];</script>
</div>
{footer_replaced}
</body>
</html>"""


# ── WRITE ALL FILES ───────────────────────────────────────────────────────────
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {os.path.relpath(path, ROOT)}")

def main():
    print("Generating static site...")

    write(os.path.join(ROOT, "index.html"),
          page("Hjem", "Hjem", HJEM_BODY))

    write(os.path.join(ROOT, "omoss.html"),
          page("Om Oss", "OmOss", build_omoss()))

    write(os.path.join(ROOT, "reiserute.html"),
          page("Reiserute", "Reiserute", REISERUTE_BODY))

    write(os.path.join(ROOT, "utstyr.html"),
          page("Utstyr", "Utstyr", build_utstyr()))

    write(os.path.join(ROOT, "turlogg.html"),
          page("Turlogg", "Turlogg", TURLOGG_BODY))

    write(os.path.join(ROOT, "gjestebok.html"),
          page("Gjestebok", "Gjestebok", GJESTEBOK_BODY))

    write(os.path.join(ROOT, "reisebrev.html"),
          page("Reisebrev", "Reisebrev", make_reisebrev_index()))

    for n in range(1, 7):
        body = read_reisebrev(n)
        # Fix Sponsorliste include if present
        body = body.replace('<?php include("Sponsorliste.html"); ?>', SPONSORLISTE_HTML)
        write(os.path.join(ROOT, f"reisebrev{n}.html"),
              page(f"Reisebrev {n}", "Reisebrev", body))

    write(os.path.join(ROOT, "galleri.html"),
          page("Galleri", "Galleri", GALLERI_BODY))

    write(os.path.join(ROOT, "videogalleri.html"),
          page("Videogalleri", "Galleri", build_videogalleri()))

    write(os.path.join(ROOT, "sponsorer.html"),
          page("Sponsorer", "Sponsorer", build_sponsorer()))

    print("\nGenerating gallery pages...")
    for gal_name in GALLERIES:
        html = build_gallery_page(gal_name)
        out = os.path.join(ROOT, "Galleri", gal_name, "index.html")
        write(out, html)

    print("\nDone. Run: bash start-server.sh")

if __name__ == "__main__":
    main()
