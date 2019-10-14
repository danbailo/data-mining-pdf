import argparse

def get_args():
	parser=argparse.ArgumentParser()
	parser.add_argument("-f","--file",
		type=str,
		help="Caminho do diretório que está o PDF ou do diretório que contem vaŕios PDFs.",
        required=True
	) 
	return parser.parse_args()