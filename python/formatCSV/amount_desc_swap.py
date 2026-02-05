import os
import glob
import csv
import io

def csv_quote(value):
    buf = io.StringIO()
    csv.writer(buf, quoting=csv.QUOTE_ALL).writerow([value])
    return buf.getvalue().strip()

def main(path=""):

    os.system('cls')

    if path == "":
        # path to csv files
        # path = r"C:\Users\mets1\Documents\website\_data\*-ing.csv"
        path = r"C:\Users\mets1\Documents\website\python\testing\*-ing.csv"
        # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\_data\*-ing.csv"
        # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*-ing.csv"
        print("empty path")

    for fname in glob.glob(path):
        temp = fname[:-4] + "-temp.csv"

        with open(fname, newline='', encoding="utf-8") as fin, \
             open(temp, "w", newline='', encoding="utf-8") as fout:

            reader = csv.reader(fin)

            for i, row in enumerate(reader):

                # Header
                if i == 0:
                    fout.write('"Ingredient",Amount,Unit,"Description"\n')
                    continue

                # Servings row
                if row[0] == "Servings":
                    fout.write(f'"Servings",{row[1]}\n')
                    continue

                # Find unit
                unit_idx = row.index("g")

                ingredient = csv_quote(row[0])
                description = csv_quote(
                    ", ".join(cell.strip() for cell in row[1:unit_idx])
                )

                fout.write(
                    f"{ingredient},0,g,{description}\n"
                )

        os.replace(temp, fname)
        print(fname)

if __name__ == "__main__":
    main()
