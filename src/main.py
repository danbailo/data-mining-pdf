from core import Pdf,Database
from utils import get_args

if __name__ == "__main__":
    args = get_args()    
    pdf = Pdf(args.file)
    pdf.get_result()
