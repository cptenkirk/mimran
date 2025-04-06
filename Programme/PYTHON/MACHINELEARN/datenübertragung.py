import csv

def text2csv(txtdat, csvdat, csv_trennzeichen=';'):
    """Textdatei in csv umwandeln"""
    with open(txtdat, 'r', encoding='utf-8') as infile, open(csvdat, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile, delimiter=csv_trennzeichen)
        for zeile in infile:
            werte = zeile.strip().split()
            csv_writer.writerow(werte)

text2csv('daten.txt', 'daten.csv', csv_trennzeichen=';')




""" import csv """
import os

def text2csv_with_filename_header(txtdat, csvdat, trennzeichen='\t', csv_trennzeichen=';'):
    """Textdatei in csv umwandeln und den Dateinamen ohne Erweiterung als Überschrift verwenden"""
    # Extrahiere den Dateinamen ohne Pfad und ohne Erweiterung
    dateiname_ohne_erweiterung = os.path.splitext(os.path.basename(txtdat))[0]

    with open(txtdat, 'r', encoding='utf-8') as infile:
        # Lese alle Zeilen und splitte sie in Werte
        zeilen = [zeile.strip().split(trennzeichen) for zeile in infile]

    # Transponiere die Liste von Zeilen, um Spalten zu erhalten
    spalten = list(zip(*zeilen))

    with open(csvdat, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile, delimiter=csv_trennzeichen)
        
        # Schreibe den Dateinamen ohne Erweiterung als erste Zeile
        csv_writer.writerow([dateiname_ohne_erweiterung])
        
        for spalte in spalten:
            # Verwende den ersten Eintrag der Spalte als Überschrift
            header = spalte[0]
            werte = spalte[1:]
            csv_writer.writerow([header] + list(werte))

# Beispielaufruf
text2csv_with_filename_header('daten.txt', 'daten.csv', trennzeichen='\t', csv_trennzeichen=';')
