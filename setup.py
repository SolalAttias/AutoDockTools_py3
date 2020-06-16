# ##################################################################################################
#  Disclaimer                                                                                      #
#  This file is a python3 translation of AutoDockTools (v.1.5.7)                                   #
#  Modifications made by Valdes-Tresanco MS (https://github.com/Valdes-Tresanco-MS)                #
#  Tested by Valdes-Tresanco-MS and Valdes-Tresanco ME                                             #
#  There is no guarantee that it works like the original distribution,                             #
#  but feel free to tell us if you get any difference to correct the code.                         #
#                                                                                                  #
#  Please use this cite the original reference.                                                    #
#  If you think my work helps you, just keep this note intact on your program.                     #
#                                                                                                  #
#  Modification date: 15/06/20, 8:19 p. m.                                                         #
#                                                                                                  #
# ##################################################################################################

from setuptools import setup

setup(
    name='AutoDockTools_py3',
    version='1.5.7',
    packages=['MolKit', 'MolKit.data', 'MolKit.pdb2pqr', 'MolKit.pdb2pqr.src', 'MolKit.pdb2pqr.propka',
              'MolKit.pdb2pqr.pdb2pka', 'MolKit.pdb2pqr.pdb2pka.substruct', 'MolKit.pdb2pqr.pdb2pka.ligandclean',
              'MolKit.pdb2pqr.extensions', 'PyBabel', '_bhtree', 'mglutil', 'mglutil.math', 'mglutil.util',
              'AutoDockTools', 'AutoDockTools.Utilities24'],
    url='https://github.com/Valdes-Tresanco-MS/AutoDockTools_py3',
    license='MGLTools LICENSE',
    author='PhD Student MS Valdes-Trasanco and PhD Student ME Valdes-Tresanco ',
    author_email='bioinfobrothers@gmail.com',
    description='Translation of ADT to python3.7'
)
