import unittest
import os
import sys
import numpy as np
from .. import prop, sirifc
from ..util import full

class TestProp(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        n, e = os.path.splitext(__file__)
        self.tmpdir = n + ".d"
        self.propfile = os.path.join(self.tmpdir, 'AOPROPER')
        self.ifcfile = os.path.join(self.tmpdir, 'SIRIFC')

    def test_zdiplen(self):
        _ref = full.triangular.init([
            -1.14582446,
            -0.28457970,   -1.14582446,
             0.00000000,    0.00000000,    -1.14582446,
            -0.00000000,    0.00000000,    -0.00000000,    -1.14582446,
             0.07185549,    0.83874358,    -0.00000000,    -0.00000000, -1.14582446,
             0.00000042,    0.03960604,    -0.00000049,     0.00000023,  0.06644414,     1.13941835,
            -0.03517114,    0.09678743,    -0.00000039,     0.00000018,  0.26304148,     0.26970481,     1.13941835,
            -0.00000043,    0.00000079,     0.04273779,     0.00000000,  0.00000217,     0.00000000,     0.00000000,     1.13941835,
             0.00000020,   -0.00000036,     0.00000000,     0.04273779, -0.00000100,    -0.00000000,     0.00000000,     0.00000000,   1.13941835,
             0.05971628,    0.14458398,    -0.00000151,     0.00000070,  0.04288205,     0.05079193,     0.64117284,     0.00000000,   0.00000000,     1.13941835,
            -0.07377362,   -0.83292247,     0.00003362,    -0.67200176,  0.76434327,     0.00510998,     0.00045345,     0.00000004,  -0.00098917,     0.05241089,    -2.23969756,
            -0.07300170,   -0.81945232,     0.00003256,     0.67188009,  0.74090119,     0.00524496,     0.00124665,     0.00000003,   0.00064587,     0.05278446,    -0.31647999,    -2.20056359,
            ])
        z, = prop.read('ZDIPLEN', filename=self.propfile, unpack=False)
        np.testing.assert_almost_equal(z, _ref)

    def test_zanglon(self):
        _ref = full.init([
          [ 0.00000000,    0.00000000,     0.00000000,     0.00000000,     0.00000000,  0.00000000, -0.00000000,    -0.00000022,    -0.00000047,  0.00000000,  0.00000000,   0.00000000],
          [ 0.00000000,    0.00000000,     0.00000000,     0.00000000,     0.00000000,  0.00000000, -0.00000000,    -0.00000113,    -0.00000246,  0.00000000,  0.00000000,   0.00000000],
          [ 0.00000000,    0.00000000,     0.00000000,    -1.00000000,     0.00000000,  0.00000000,  0.00000000,     0.00000000,    -0.21189133,  0.00000000,  0.00000000,   0.00000000],
          [-0.00000000,   -0.00000000,     1.00000000,    -0.00000000,    -0.00000000,  0.00000000,  0.00000000,     0.21189133,    -0.00000000,  0.00000000,  0.00000000,   0.00000000],
          [ 0.00000000,    0.00000000,     0.00000000,     0.00000000,     0.00000000,  0.00000000,  0.00000000,    -0.00000184,    -0.00000400, -0.00000000, -0.00000000,  -0.00000000],
          [ 0.00000000,    0.00000000,     0.00000022,     0.00000048,     0.00000000,  0.00000000,  0.00000000,     0.00000000,     0.00000000,  0.00000000,  0.00000000,   0.00000000],
          [ 0.00000000,   -0.00000000,     0.00000155,     0.00000338,    -0.00000000,  0.00000000,  0.00000000,     0.00000000,     0.00000000,  0.00000000,  0.00000000,   0.00000000],
          [-0.00000000,   -0.00000000,     0.00000000,    -0.21189133,    -0.00000000,  0.00000000,  0.00000000,     0.00000000,    -1.00000000,  0.00000000,  0.00000000,   0.00000000],
          [ 0.00000000,   -0.00000000,     0.21189133,    -0.00000000,     0.00000000,  0.00000000,  0.00000000,     1.00000000,     0.00000000,  0.00000000,  0.00000000,   0.00000000],
          [-0.00000000,    0.00000000,    -0.00000184,    -0.00000400,    -0.00000000,  0.00000000,  0.00000000,     0.00000000,     0.00000000,  0.00000000,  0.00000000,   0.00000000],
          [-0.00000000,   -0.00000000,     0.39427368,     0.00001972,    -0.00000000,  0.00000000, -0.00000000,     0.03771757,     0.00000152, -0.00000000, -0.00000000,  -0.00000000],
          [-0.00000000,   -0.00000000,    -0.39890626,     0.00001933,     0.00000000,  0.00000000,  0.00000000,    -0.03934100,     0.00000153,  0.00000000,  0.00000000,   0.00000000],
        ])

        z, = prop.read('ZANGLON', filename=self.propfile, unpack=False)
        np.testing.assert_allclose(z, _ref, atol=1e-5)

    def test_main_z_packed(self):
        sys.argv[1:] = ['ZDIPLEN', '-t', self.tmpdir, '--packed']
        prop.main()
        _ref = """-1.14582446
   -0.28457970   -1.14582446
    0.00000000    0.00000000   -1.14582446
   -0.00000000    0.00000000   -0.00000000   -1.14582446
    0.07185549    0.83874358   -0.00000000   -0.00000000   -1.14582446
    0.00000042    0.03960604   -0.00000049    0.00000023    0.06644414    1.13941835
   -0.03517114    0.09678743   -0.00000039    0.00000018    0.26304148    0.26970481    1.13941835
   -0.00000043    0.00000079    0.04273779    0.00000000    0.00000217    0.00000000    0.00000000    1.13941835
    0.00000020   -0.00000036    0.00000000    0.04273779   -0.00000100   -0.00000000    0.00000000    0.00000000    1.13941835
    0.05971628    0.14458398   -0.00000151    0.00000070    0.04288205    0.05079193    0.64117284    0.00000000    0.00000000    1.13941835
   -0.07377362   -0.83292247    0.00003362   -0.67200176    0.76434327    0.00510998    0.00045345    0.00000004   -0.00098917    0.05241089   -2.23969756
   -0.07300170   -0.81945232    0.00003256    0.67188009    0.74090119    0.00524496    0.00124665    0.00000003    0.00064587    0.05278446   -0.31647999   -2.20056359"""

        print_output = sys.stdout.getvalue().strip()
        self.assertEqual(print_output, _ref)

    def test_main_z_unpacked(self):
        sys.argv[1:] = ['ZDIPLEN', '-t', self.tmpdir]
        prop.main()
        _ref = """\
(12, 12) 
              Column   1    Column   2    Column   3    Column   4    Column   5
       1     -1.14582446   -0.28457970    0.00000000   -0.00000000    0.07185549
       2     -0.28457970   -1.14582446    0.00000000    0.00000000    0.83874358
       3      0.00000000    0.00000000   -1.14582446   -0.00000000   -0.00000000
       4     -0.00000000    0.00000000   -0.00000000   -1.14582446   -0.00000000
       5      0.07185549    0.83874358   -0.00000000   -0.00000000   -1.14582446
       6      0.00000042    0.03960604   -0.00000049    0.00000023    0.06644414
       7     -0.03517114    0.09678743   -0.00000039    0.00000018    0.26304148
       8     -0.00000043    0.00000079    0.04273779    0.00000000    0.00000217
       9      0.00000020   -0.00000036    0.00000000    0.04273779   -0.00000100
      10      0.05971628    0.14458398   -0.00000151    0.00000070    0.04288205
      11     -0.07377362   -0.83292247    0.00003362   -0.67200176    0.76434327
      12     -0.07300170   -0.81945232    0.00003256    0.67188009    0.74090119

              Column   6    Column   7    Column   8    Column   9    Column  10
       1      0.00000042   -0.03517114   -0.00000043    0.00000020    0.05971628
       2      0.03960604    0.09678743    0.00000079   -0.00000036    0.14458398
       3     -0.00000049   -0.00000039    0.04273779    0.00000000   -0.00000151
       4      0.00000023    0.00000018    0.00000000    0.04273779    0.00000070
       5      0.06644414    0.26304148    0.00000217   -0.00000100    0.04288205
       6      1.13941835    0.26970481    0.00000000   -0.00000000    0.05079193
       7      0.26970481    1.13941835    0.00000000    0.00000000    0.64117284
       8      0.00000000    0.00000000    1.13941835    0.00000000    0.00000000
       9     -0.00000000    0.00000000    0.00000000    1.13941835    0.00000000
      10      0.05079193    0.64117284    0.00000000    0.00000000    1.13941835
      11      0.00510998    0.00045345    0.00000004   -0.00098917    0.05241089
      12      0.00524496    0.00124665    0.00000003    0.00064587    0.05278446

              Column  11    Column  12
       1     -0.07377362   -0.07300170
       2     -0.83292247   -0.81945232
       3      0.00003362    0.00003256
       4     -0.67200176    0.67188009
       5      0.76434327    0.74090119
       6      0.00510998    0.00524496
       7      0.00045345    0.00124665
       8      0.00000004    0.00000003
       9     -0.00098917    0.00064587
      10      0.05241089    0.05278446
      11     -2.23969756   -0.31647999
      12     -0.31647999   -2.20056359"""


        print_output = sys.stdout.getvalue().strip()
        self.assertEqual(print_output, _ref)

        

if __name__ == "__main__":#pragma no cover
    unittest.main()


