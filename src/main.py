import sys
from core import Pdf

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("USAGE")
        exit(-1)

    file = sys.argv[1]

    pdf = Pdf(file)
    pdf.get_result()
