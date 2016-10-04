import os
from Bio.PDB import PDBParser
from Bio.PDB import PDBIO
import Bio.PDB
from optparse import OptionParser

#Single file mode
def constrain(options):
    p = PDBParser()
    chains_to_choose = []
    if (options.file):
        pdb_file = options.file
        structure = p.get_structure("input", pdb_file)
        print "Input file = ", pdb_file
        for chain in options.chains:
                chains_to_choose.append(chain)
        
        Select = Bio.PDB.Select
        class ConstrSelect(Select):
            def accept_chain(self, chain):
                #print dir(residue)
                
                if chain.id in chains_to_choose:
                    return 1
                else:
                    return 0
        
        w = PDBIO()
        w.set_structure(structure)
        w.save(options.output,ConstrSelect())
        
#Parse the options
usage = "USAGE: python PDB_constrain.py -f FILE -c CHAINS -o OUTPUT"
parser = OptionParser(usage=usage)

print os.getcwd()

#Single file mode
parser.add_option("-f","--file",help="File location", dest="file")
parser.add_option("-c","--chains",help="Chains to constrain, e.g. -c ABCD", dest="chains")
parser.add_option("-o","--output",help="Output file", dest="output")

(options, args) = parser.parse_args()

if (options.file and options.chains and options.output):
	constrain(options)
else:
	print "Not enough input arguments supplied"
	print usage
