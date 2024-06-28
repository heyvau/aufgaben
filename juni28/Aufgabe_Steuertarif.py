# Die deutsche Einkommensteuer wird nach § 32a
# aus dem Einkommensteuergesetz (EStG) berechnet:

# § 32a Einkommensteuertarif

# (1) 1 Die tarifliche Einkommensteuer bemisst sich 
# nach dem auf volle Euro abgerundeten zu versteuernden Einkommen. 

# 2 Sie beträgt im Veranlagungszeitraum 2023 vorbehaltlich 
# der §§ 32b, 32d, 34, 34a, 34b und 34c jeweils in Euro für zu versteuernde Einkommen

# 1.
#     bis 10 908 Euro (Grundfreibetrag):
#     0;
# 2.
#     von 10 909 Euro bis 15 999 Euro:
#     (979,18 · y + 1 400) · y;
# 3.
#     von 16 000 Euro bis 62 809 Euro:
#     (192,59 · z + 2 397) · z + 966,53;
# 4.
#     von 62 810 Euro bis 277 825 Euro:
#     0,42 · x – 9 972,98;
# 5.
#     von 277 826 Euro an:
#     0,45 · x – 18 307,73.

# 3 Die Größe „y“ ist ein Zehntausendstel
# des den Grundfreibetrag übersteigenden Teils
# des auf einen vollen Euro-Betrag abgerundeten zu versteuernden Einkommens.

# 4 Die Größe „z“ ist ein Zehntausendstel des 15 999 Euro übersteigenden Teils
# des auf einen vollen Euro-Betrag abgerundeten zu versteuernden Einkommens.

# 5 Die Größe „x“ ist
# das auf einen vollen Euro-Betrag abgerundete zu versteuernde Einkommen.

# 6 Der sich ergebende Steuerbetrag ist
#  auf den nächsten vollen Euro-Betrag abzurunden.




# Aufgabe:

# Erstellen Sie ein Python-Skript,
# dass den die oben beschriebene Berechnung der Einkommensteuer implementiert.
# Testen Sie Ihren Code daraufhin mit einigen, selbst gewählten, Werten.

max_grundfreibetrag = 10908


def y_berechnung(betrag):
    y = 0.0001 * (betrag - max_grundfreibetrag)
    print(y)
    return y


def z_berechnung(betrag):
    z = 0.0001 * (betrag - 15999)
    return z


def x_berechnung(betrag):
    x = round(betrag)
    return x


def einkommensteuer_berechnung(einkommen):

    einkommensteuer = 0

    abgerundetes_einkommen = round(einkommen)
    y = y_berechnung(abgerundetes_einkommen)
    z = z_berechnung(abgerundetes_einkommen)
    x = x_berechnung(abgerundetes_einkommen)

    if abgerundetes_einkommen in range(10909, 16000):
        einkommensteuer = (979.18 * y + 1400) * y

    elif abgerundetes_einkommen in range(16000, 62810):
        einkommensteuer = (192.59 * z + 2397) * z + 966.53

    elif abgerundetes_einkommen in range(62810, 277826):
        einkommensteuer = 0.42 * x - 9972.98

    elif (abgerundetes_einkommen >= 277826):
        einkommensteuer = 0.45 * x - 18307.73

    return round(einkommensteuer)


mein_einkommen = float(input("Mein Einkommen beträgt: "))

einkommensteuer = einkommensteuer_berechnung(mein_einkommen)

print("Deine Einkommensteuer beträgt dann:", einkommensteuer)
