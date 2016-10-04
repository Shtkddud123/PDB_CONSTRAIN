1.What does it do?

Given a pdb file, write out the ATOM and HETATM entries for the supplied chain(s).

PDB_constrain needs three arguments:

1. PDB file to constrain.

2. Chains from the pdb file to constrain.

3. Output file.

2. Requirements: Biopython - should be installed at your machines but in case you want to use it locally, download the latest version http://biopython.org/wiki/Download into the PDB_constrain.py's directory (don't need to build).

3. Example use:

A. Constrain 1A2Y.pdb to chains A and B - write results in constr.pdb
python PDB_constrain.py -f 1A2Y.pdb -c AB -o const.pdb

B. Constrain 1ACY to chain L, write results in const.pdb - this example shows that the constrainer works well with 'insertion' residue numbering as in antibodies where you have 27A, 27B etc.
python PDB_constrain.py -f 1ACY.pdb -c L -o const.pdb
