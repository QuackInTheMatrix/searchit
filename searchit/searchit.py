from functions import *
import sys

if __name__=="__main__":
    if(sys.argv[1]=="find"):
        findparam(sys.argv[2])
    else:
        url=sys.argv[1]
        search=asci_encoder(" ".join(sys.argv[2:]))
        browse(url,search)
