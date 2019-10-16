from core import Bradesco,SulAmerica,Database
from utils import get_args

if __name__ == "__main__":
    args = get_args()    
    # bradesco = Bradesco(args.file)
    # bradesco.get_result()

    sulamerica = SulAmerica(args.file)
    sulamerica.get_result()
