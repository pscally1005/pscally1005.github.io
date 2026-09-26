# Download csv to /python/testing folder, and move exact gram amounts into Amount

import csv
import glob
import os
import re


EXACT_GRAMS = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*g\s*$", re.IGNORECASE)


def fix_mass_desc(amount, desc, unit):
    match = EXACT_GRAMS.fullmatch(desc)
    if match and unit.lower() == "g":
        return match.group(1), ""

    return amount, desc


def main(path=""):
    os.system("cls")

    if path == "":
        path = r"C:\Users\mets1\Documents\website\python\testing\*-ing.csv"
        print("empty path")

    changed = 0
    for fname in glob.glob(path):
        temp = fname[:-4] + "-temp.csv"

        with open(fname, "r", newline="") as csvfile, open(temp, "w", newline="") as fout:
            reader = csv.reader(csvfile)
            writer = csv.writer(fout, lineterminator="\n")

            for row_number, row in enumerate(reader):
                if row_number != 0 and len(row) >= 4:
                    ingredient = row[0]
                    unit = row[-2]
                    desc = row[-1]
                    amount = ",".join(row[1:-2])
                    amount, desc = fix_mass_desc(amount, desc, unit)
                    row = [ingredient, amount, unit, desc]

                writer.writerow(row)

        os.remove(fname)
        os.rename(temp, fname)
        print(fname)
        changed += 1

    print(str(changed) + " files updated")


if __name__ == "__main__":
    main()
