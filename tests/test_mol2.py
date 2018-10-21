import unittest
import unittest.mock as mock
import os
import sys
from . import daltools
from daltools import mol


class MolTest(unittest.TestCase):

    def setUp(self):
        pwd = os.path.dirname(__file__)
        dalton_bas = os.path.join(pwd, 'test_mol2.d', 'DALTON.BAS')
        self.bas = mol.readin(dalton_bas)
        self.maxDiff = None

    def tearDown(self):
        pass

    def test_pass(self):
        pass

    def test_dist(self):
        self.assertAlmostEqual(
            mol.dist(self.bas[0]["center"][0], self.bas[1]["center"][0]),
            2.2852428069
            )

    def test_num(self):
        self.assertAlmostEqual(mol.nuc(self.bas), 31.2492153162)

    def test_opa(self):
        self.assertListEqual(
            mol.occupied_per_atom(self.bas),
            [[0, 1, 4, 5, 6], [0, 1, 2, 3,4], [0], [0]]
            )

    def test_cpa(self):
        self.assertListEqual(
            mol.contracted_per_atom(self.bas),
            [30, 5, 1, 1]
            )

    def test_cpal(self):
        self.assertListEqual(
            mol.contracted_per_atom_l(self.bas),
            [[4, 9, 10, 7], [2, 3], [1], [1]]
            )

    def test_print_atoms(self):
        output = """\
Atom type 1 charge 6.000000
center 1 [1.74063211e-05, 0.0010502765856, -1.1458244562083]
s-functions
    50557.501 [5.527e-05, -1.2e-05, 1.185e-05, -1.56e-05]
    7524.7856 [0.00043433, -9.4e-05, 9.271e-05, -0.000114]
    1694.3276 [0.00231588, -0.0005028, 0.00049893, -0.0006731]
    472.82279 [0.00987292, -0.0021476, 0.002118, -0.0025323]
    151.71075 [0.03521949, -0.0077942, 0.00777839, -0.0109003]
    53.918746 [0.10419375, -0.0237634, 0.02363282, -0.0277807]
    20.659311 [0.24127411, -0.0600235, 0.06163057, -0.0958713]
    8.383976 [0.38401741, -0.1153985, 0.11896802, -0.1247806]
    3.577015 [0.30823714, -0.1539009, 0.18806208, -0.393246]
    1.547118 [0.06830554, -0.0145946, -0.0540304, 0.67960039]
    0.613013 [0.00077821, 0.38958492, -0.9814137, 1.197869]
    0.246068 [0.00099049, 0.53972907, -0.1096758, -1.897952]
    0.099087 [-8.93e-05, 0.18840601, 0.88473559, -0.0044614]
    0.03468 [4.714e-05, 0.02585753, 0.29649833, 1.0142148]
p-functions
    83.333155 [0.00122406, -0.0011444, 0.00146694]
    19.557611 [0.00943894, -0.0089796, 0.01445532]
    6.080365 [0.04177441, -0.0378456, 0.04663731]
    2.179317 [0.13183304, -0.1292708, 0.23665375]
    0.86515 [0.27891188, -0.3784022, 0.60887342]
    0.361944 [0.36686633, -0.2692137, -0.3917793]
    0.15474 [0.27905913, 0.29175424, -0.8700229]
    0.065429 [0.13804807, 0.5436698, 0.42005046]
    0.0229 [0.03419495, 0.26283081, 0.57994967]
d-functions
    1.9 [0.09873123, -0.1455013]
    0.665 [0.45296608, -0.5076809]
    0.23275 [0.4362457, -0.101563]
    0.081463 [0.27192502, 0.9251922]
f-functions
    1.25 [0.31136503]
    0.5 [0.5159673]
    0.2 [0.37742313]
Atom type 2 charge 8.000000
center 1 [0.0, 0.0010582718101, 1.1394183506149]
s-functions
    130.70932 [0.15432897, 0.0]
    23.808861 [0.53532814, 0.0]
    6.4436083 [0.44463454, 0.0]
    5.0331513 [0.0, -0.09996723]
    1.1695961 [0.0, 0.39951283]
    0.380389 [0.0, 0.70011547]
p-functions
    5.0331513 [0.15591627]
    1.1695961 [0.60768372]
    0.380389 [0.39195739]
Atom type 3 charge 1.000000
center 1 [-7.11056897e-05, 1.7705033753955, -2.2396975555016]
center 2 [-6.98661118e-05, -1.7998043816988, -2.2005635940297]
s-functions
    3.4252509 [0.15432897]
    0.6239137 [0.53532814]
    0.1688554 [0.44463454]
"""
        with mock.patch('daltools.mol.print') as mock_print:
            mol.printbasis(self.bas)
        mock_print.assert_called_once_with(output)


        

if __name__ == "__main__":#pragma no cover
    unittest.main()
