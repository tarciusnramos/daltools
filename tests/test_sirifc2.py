import unittest
import os
import numpy as np
from daltools import sirifc
from util import full


class TestSirIfc(unittest.TestCase):
    def tmpdir(self, name=""):
        n, _ = os.path.splitext(__file__)
        dir_ = n + ".d"
        return os.path.join(dir_, name)

    def setUp(self):
        self.ifc = sirifc.sirifc(self.tmpdir("SIRIFC"))

    def test_wrong_file_header(self):
        with self.assertRaises(RuntimeError):
            wrong = sirifc.sirifc(name=self.tmpdir("AOONEINT"))

    def test_potnuc(self):
        self.assertAlmostEqual(self.ifc.potnuc, 31.249215315972)

    def test_emy(self):
        self.assertAlmostEqual(self.ifc.emy, -142.1249229)

    def test_eactive(self):
        self.assertAlmostEqual(self.ifc.eactive, -1.5308779)

    def test_emcscf(self):
        self.assertAlmostEqual(self.ifc.emcscf, -112.4065855)

    def test_istate(self):
        self.assertEqual(self.ifc.istate, 1)

    def test_ispin(self):
        self.assertEqual(self.ifc.ispin, 1)

    def test_nactel(self):
        self.assertEqual(self.ifc.nactel, 2)

    def test_lsym(self):
        self.assertEqual(self.ifc.lsym, 1)

    def test_nisht(self):
        self.assertEqual(self.ifc.nisht, 7)

    def test_nasht(self):
        self.assertEqual(self.ifc.nasht, 2)

    def test_nocct(self):
        self.assertEqual(self.ifc.nocct, 9)

    def test_norbt(self):
        self.assertEqual(self.ifc.norbt, 12)

    def test_nbast(self):
        self.assertEqual(self.ifc.nbast, 12)

    def test_nsym(self):
        self.assertEqual(self.ifc.nsym, 1)

    def test_pv(self):
        pv = self.ifc.pv
        np.testing.assert_allclose(
            pv.diagonal(), [1.87279201, -0.24404616, 0.12720799], rtol=1e-7
        )

    def test_str(self):
        print(self.ifc)
        self.assertEqual(
            str(self.ifc),
            """\
Nuclear Potential Energy:    31.249215
Electronic energy       :  -142.124923
Active energy           :    -1.530878
MCSCF energy            :  -112.406585
State                   : 1
Spin                    : 1
Active electrons        : 2
Symmetry                : 1
NISHT                   : 7
NASHT                   : 2
NOCCT                   : 9
NORBT                   : 12
NBAST                   : 12
NCONF                   : 3
NWOPT                   : 41
NWOPH                   : 42
NCDETS                  : 4
NCMOT                   : 144
NNASHX                  : 3
NNASHY                  : 6
NNORBT                  : 78
N2ORBT                  : 144
NSYM                    : 1
MULD2H:
    1 2 3 4 5 6 7 8
    2 1 4 3 6 5 8 7
    3 4 1 2 7 8 5 6
    4 3 2 1 8 7 6 5
    5 6 7 8 1 2 3 4
    6 5 8 7 2 1 4 3
    7 8 5 6 3 4 1 2
    8 7 6 5 4 3 2 1
NRHF: 8 0 0 0 0 0 0 0
NFRO: 0 0 0 0 0 0 0 0
NISH: 7 0 0 0 0 0 0 0
NASH: 2 0 0 0 0 0 0 0
NORB: 12 0 0 0 0 0 0 0
NBAS: 12 0 0 0 0 0 0 0
NELMN1                  : 0
NELMX1                  : 0
NELMN3                  : 0
NELMX3                  : 0
MCTYPE                  : 1
NAS1: 0 0 0 0 0 0 0 0
NAS2: 2 0 0 0 0 0 0 0
NAS3: 0 0 0 0 0 0 0 0
CMO
Block 1

 (12, 12)
              Column   1    Column   2    Column   3    Column   4    Column   5
       1     -0.00052655   -0.99258475    0.12214814    0.18679815    0.00050726
       2      0.00738859   -0.03311517   -0.27078723   -0.58099913   -0.00162677
       3     -0.00000007    0.00000055    0.00000534    0.00002006   -0.00000017
       4     -0.00001518    0.00002467    0.00014773   -0.00134426    0.52561387
       5      0.00636791   -0.00093460   -0.15741477    0.20976200   -0.00511942
       6     -0.99427325   -0.00013397    0.21990895   -0.10147797   -0.00148698
       7     -0.02609112    0.00594499   -0.77064663    0.44552834    0.00765835
       8     -0.00000005    0.00000017    0.00000200    0.00000918   -0.00000014
       9     -0.00000173    0.00000505    0.00002683   -0.00006994    0.45788538
      10      0.00572628   -0.00169264    0.17435967    0.18410116    0.00668068
      11     -0.00022996    0.00650904   -0.03114649   -0.26524882    0.29224399
      12     -0.00026323    0.00650866   -0.03092572   -0.26038711   -0.29347313

              Column   6    Column   7    Column   8    Column   9    Column  10
       1     -0.02578485   -0.00032428    0.00000861   -0.00000815   -0.20371523
       2      0.07798424    0.00213300   -0.00003389    0.00004235    1.27275149
       3      0.00000272   -0.00000006   -0.62275388    0.81190278   -0.00006261
       4      0.00604018   -0.19450886   -0.00000012    0.00000024   -0.00975542
       5      0.44723929   -0.00155906    0.00000795   -0.00001269   -0.47781027
       6      0.08986083    0.00015264   -0.00000168    0.00000088    0.02310867
       7     -0.48072600   -0.00078917    0.00000867   -0.00000441   -0.12777795
       8     -0.00000137   -0.00000045   -0.66151094   -0.78064832    0.00001592
       9      0.00790552    0.86370510   -0.00000038   -0.00000035    0.00087975
      10     -0.68018674    0.00461259   -0.00000305    0.00000680    0.20233503
      11     -0.16662676   -0.35915849   -0.00000010   -0.00001613   -0.89048943
      12     -0.16806266    0.36358223   -0.00000016   -0.00001601   -0.89337457

              Column  11    Column  12
       1      0.00463518   -0.10507238
       2     -0.03163605    0.70986991
       3      0.00000107   -0.00000597
       4     -1.16001519   -0.03780446
       5     -0.02585616    1.15782085
       6     -0.00385000    0.11754739
       7      0.02732096   -0.88449806
       8     -0.00000012   -0.00000617
       9      0.31567668    0.00892039
      10     -0.03127431    0.93288698
      11      0.84459895    0.13352446
      12     -0.84199120    0.06941922
DV

    1.87279201
    0.00000000    0.12720799

FOCK
Block 1

 (12, 12)
              Column   1    Column   2    Column   3    Column   4    Column   5
       1    -40.64550108    0.00000000   -0.00000000    0.00000000    0.00000000
       2      0.00000000  -22.22752289    0.00000000   -0.00000000   -0.00000000
       3     -0.00000000    0.00000000   -2.69237493   -0.00000000    0.00000000
       4      0.00000000   -0.00000000   -0.00000000   -1.60081421    0.00000000
       5      0.00000000   -0.00000000    0.00000000    0.00000000   -1.27482825
       8      0.00000041   -0.00000638   -0.00000869   -0.00000786   -0.00000003
       9      0.00000007    0.00000039    0.00000196    0.00000251    0.00000001

              Column   6    Column   7    Column   8    Column   9    Column  10
       1     -0.00000000   -0.00000000    0.00000041    0.00000006   -0.00000033
       2     -0.00000000   -0.00000000   -0.00000635    0.00000037   -0.00000143
       3      0.00000000   -0.00000000   -0.00000853    0.00000182   -0.00000099
       4     -0.00000000   -0.00000000   -0.00000768    0.00000249    0.00000027
       5      0.00000000    0.00000000   -0.00000003    0.00000001    0.00000012
       6     -1.09797005   -0.00000000    0.00000441    0.00000040   -0.00000019
       7     -0.00000000   -0.71770628   -0.00000010   -0.00000000    0.00000017
       8      0.00000444   -0.00000010   -0.93662341   -0.03458114    0.00000017
       9      0.00000048   -0.00000000   -0.03458079   -0.10964085   -0.00000002

              Column  11    Column  12
       1      0.00000015   -0.00000145
       2     -0.00000003    0.00000034
       3      0.00000023   -0.00000162
       4      0.00000002    0.00000055
       5     -0.00000018    0.00000035
       6     -0.00000025    0.00000005
       7     -0.00000028    0.00000073
       8     -0.00000001    0.00000007
       9      0.00000001   -0.00000009
PV

 (3, 3)
              Column   1    Column   2    Column   3
       1      1.87279201    0.00000000    0.00000000
       2      0.00000000   -0.24404616   -0.00000000
       3      0.00000000   -0.00000000    0.12720799

FC
Block 1

  -21.82651510
    0.00021570  -12.33106718
    0.02441259    0.00806484   -2.47001230
   -0.01250084    0.01973183    0.05282073   -1.63316097
   -0.00022867   -0.00006546   -0.00039479   -0.00144512   -1.54503975
    0.01673583    0.00690685    0.08119936    0.11592216    0.00084204   -1.60124205
   -0.00003371   -0.00005472   -0.00091236    0.00000451   -0.17893615   -0.00134958   -1.36495227
    0.00000024   -0.00000370   -0.00000524   -0.00000380   -0.00000002    0.00000342   -0.00000005   -1.03075644
    0.00000009    0.00000072   -0.00000099    0.00000549    0.00000000    0.00000148   -0.00000003   -0.07084901   -0.66897619
   -0.00018894   -0.02159810   -0.01264611    0.12284378    0.00053164    0.08442010   -0.00137244    0.00000075   -0.00000044   -0.11932392
   -0.00008747    0.00002583    0.00370629   -0.00239881    0.12282332   -0.00219059   -0.15937999   -0.00000008    0.00000010    0.00146631   -0.10700224
    0.00303305    0.00639908   -0.09075113    0.02624286    0.00452983    0.04108645   -0.00600675    0.00000289   -0.00000225   -0.07083251    0.00965537   -0.22786191
FV
Block 1

    1.50376456
   -0.00021570    1.21730573
   -0.02441259   -0.00806484    1.12382484
    0.01250084   -0.01973183   -0.05282073    0.83275386
    0.00022867    0.00006546    0.00039479    0.00144512    0.90762563
   -0.01673583   -0.00690685   -0.08119936   -0.11592216   -0.00084204    1.05225702
    0.00003371    0.00005472    0.00091236   -0.00000451    0.17893615    0.00134958    1.00609914
   -0.00000003    0.00000052    0.00000097   -0.00000004    0.00000000   -0.00000121    0.00000001    0.60732461
   -0.00000006   -0.00000053    0.00000190   -0.00000425    0.00000000   -0.00000128    0.00000003    0.06214772    0.93083752
    0.00018878    0.02159739    0.01264562   -0.12284365   -0.00053158   -0.08442019    0.00137253   -0.00000170   -0.00000536    0.74496590
    0.00008754   -0.00002585   -0.00370618    0.00239882   -0.12282341    0.00219046    0.15937985    0.00000008   -0.00000012   -0.00146631    0.85736994
   -0.00303377   -0.00639892    0.09075032   -0.02624258   -0.00452965   -0.04108642    0.00600712   -0.00000260    0.00000565    0.07083251   -0.00965537    1.14634522
""",
        )


if __name__ == "__main__":  # pragma no cover
    unittest.main()
