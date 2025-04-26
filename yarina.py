# -*- coding: utf-8 -*-
import rhinoscriptsyntax as rs
import csv

def export_curve_lengths_to_csv_with_dots():
    curves = rs.GetObjects("Please select the curves to measure", rs.filter.curve)
    if not curves:
        print("No curves were selected.")
        return

    filepath = rs.SaveFileName("Save as CSV", "CSV Files (*.csv)|*.csv||")
    if not filepath:
        return

    total = 0
    data = []

    for curve in curves:
        length = rs.CurveLength(curve)
        total += length
        data.append([round(length, 2)])

        midpoint = rs.CurveMidPoint(curve)
        rs.AddTextDot(str(round(length, 2)), midpoint)

    # Dosyayı binary modda açıyoruz, böylece ekstra satır sorununu çözüyoruz
    with open(filepath, mode='wb') as file:
        writer = csv.writer(file)
        writer.writerow(["Length (units)"])  # Başlık
        for row in data:
            # Sayıları düz şekilde, sadece ondalık nokta ile yaz
            writer.writerow([str(row[0])])
        writer.writerow(["Total", str(round(total, 2))])

    print("{} curves measured.".format(len(curves)))
    print("CSV file saved successfully: {}".format(filepath))

export_curve_lengths_to_csv_with_dots()
