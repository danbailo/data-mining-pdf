import argparse

def get_args():
	parser=argparse.ArgumentParser()
	parser.add_argument("-f","--file",
		type=str,
		help="Caminho do PDF ou do diretório que contem o(s) PDF(s).",
        required=True
	) 
	return parser.parse_args()