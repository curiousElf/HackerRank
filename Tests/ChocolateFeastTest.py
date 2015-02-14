__author__ = 'DINUN'
import unittest
from ChocolateFeast import ChocolateFeast


class ChocolateFeastTest(unittest.TestCase):

    def test_no_extra_chocolates(self):
        """This test will check for a case where there are no extra chocolates recieved
        """
        _inpc = ChocolateFeast(10,5,5)
        self.assertEquals(2,_inpc.get_total_chocolates())

    def test_extra_chocolates_single(self):
        """This test checks for a case where there are extra chocs but the extra chocs are small enough
        to not give mroe chocolates
        """
        _inpc = ChocolateFeast(12,4,4)
        self.assertEquals(3,_inpc.get_total_chocolates())

    def test_extra_chocolates_multiple(self):
        """This test checks for a case where the number of chocolates given will be large enough to cause
        more free chocolates
        """
        _inpc = ChocolateFeast(6,2,2)
        self.assertEquals(5,_inpc.get_total_chocolates())

    def test_hr_input2(self):
        self.assertEquals(ChocolateFeast(16809,123,11668).get_total_chocolates(),136)
        self.assertEquals(ChocolateFeast(20373,18211,10188).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(92512,413,33040).get_total_chocolates(),224)
        self.assertEquals(ChocolateFeast(2339,4,1337).get_total_chocolates(),584)
        self.assertEquals(ChocolateFeast(96741,945,77194).get_total_chocolates(),102)
        self.assertEquals(ChocolateFeast(53270,182,30238).get_total_chocolates(),292)
        self.assertEquals(ChocolateFeast(47733,230,4840).get_total_chocolates(),207)
        self.assertEquals(ChocolateFeast(60751,346,20578).get_total_chocolates(),175)
        self.assertEquals(ChocolateFeast(19150,99,2945).get_total_chocolates(),193)
        self.assertEquals(ChocolateFeast(94566,514,47583).get_total_chocolates(),183)
        self.assertEquals(ChocolateFeast(17274,5234,12885).get_total_chocolates(),3)
        self.assertEquals(ChocolateFeast(39478,364,23991).get_total_chocolates(),108)
        self.assertEquals(ChocolateFeast(46052,388,43028).get_total_chocolates(),118)
        self.assertEquals(ChocolateFeast(21816,14645,1827).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(98573,74120,44437).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(47151,78,28526).get_total_chocolates(),604)
        self.assertEquals(ChocolateFeast(18991,78,10010).get_total_chocolates(),243)
        self.assertEquals(ChocolateFeast(28583,113,5299).get_total_chocolates(),252)
        self.assertEquals(ChocolateFeast(34587,86,33334).get_total_chocolates(),402)
        self.assertEquals(ChocolateFeast(59272,24946,44416).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(41894,36,640).get_total_chocolates(),1164)
        self.assertEquals(ChocolateFeast(65164,522,23728).get_total_chocolates(),124)
        self.assertEquals(ChocolateFeast(40916,399,30670).get_total_chocolates(),102)
        self.assertEquals(ChocolateFeast(7045,25,6484).get_total_chocolates(),281)
        self.assertEquals(ChocolateFeast(45567,63,7564).get_total_chocolates(),723)
        self.assertEquals(ChocolateFeast(63041,302,50870).get_total_chocolates(),208)
        self.assertEquals(ChocolateFeast(14440,3,275).get_total_chocolates(),4830)
        self.assertEquals(ChocolateFeast(33773,13179,6929).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(71656,325,52375).get_total_chocolates(),220)
        self.assertEquals(ChocolateFeast(1575,1,262).get_total_chocolates(),1581)
        self.assertEquals(ChocolateFeast(2216,8,35).get_total_chocolates(),285)
        self.assertEquals(ChocolateFeast(16974,1248,6090).get_total_chocolates(),13)
        self.assertEquals(ChocolateFeast(74892,314,48340).get_total_chocolates(),238)
        self.assertEquals(ChocolateFeast(45312,848,44198).get_total_chocolates(),53)
        self.assertEquals(ChocolateFeast(96428,81144,43066).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(61264,96,14300).get_total_chocolates(),638)
        self.assertEquals(ChocolateFeast(52734,489,40749).get_total_chocolates(),107)
        self.assertEquals(ChocolateFeast(42751,125,8850).get_total_chocolates(),342)
        self.assertEquals(ChocolateFeast(51803,25,38253).get_total_chocolates(),2072)
        self.assertEquals(ChocolateFeast(15012,6806,2360).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(41447,94,8946).get_total_chocolates(),440)
        self.assertEquals(ChocolateFeast(35849,343,28910).get_total_chocolates(),104)
        self.assertEquals(ChocolateFeast(32715,123,21578).get_total_chocolates(),265)
        self.assertEquals(ChocolateFeast(43344,425,7949).get_total_chocolates(),101)
        self.assertEquals(ChocolateFeast(41986,104,18269).get_total_chocolates(),403)
        self.assertEquals(ChocolateFeast(4893,37,921).get_total_chocolates(),132)
        self.assertEquals(ChocolateFeast(13243,108,10845).get_total_chocolates(),122)
        self.assertEquals(ChocolateFeast(45996,24153,38080).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(48630,366,48388).get_total_chocolates(),132)
        self.assertEquals(ChocolateFeast(66474,560,50488).get_total_chocolates(),118)
        self.assertEquals(ChocolateFeast(90041,613,9878).get_total_chocolates(),146)
        self.assertEquals(ChocolateFeast(5975,32,4059).get_total_chocolates(),186)
        self.assertEquals(ChocolateFeast(24892,157,3783).get_total_chocolates(),158)
        self.assertEquals(ChocolateFeast(85276,579,4163).get_total_chocolates(),147)
        self.assertEquals(ChocolateFeast(51005,503,44415).get_total_chocolates(),101)
        self.assertEquals(ChocolateFeast(56364,40668,53449).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(78089,566,70805).get_total_chocolates(),137)
        self.assertEquals(ChocolateFeast(44843,29,44838).get_total_chocolates(),1546)
        self.assertEquals(ChocolateFeast(31777,12538,1103).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(56037,545,24743).get_total_chocolates(),102)
        self.assertEquals(ChocolateFeast(34612,116,21569).get_total_chocolates(),298)
        self.assertEquals(ChocolateFeast(78806,591,64185).get_total_chocolates(),133)
        self.assertEquals(ChocolateFeast(76790,661,44704).get_total_chocolates(),116)
        self.assertEquals(ChocolateFeast(77417,52,35659).get_total_chocolates(),1488)
        self.assertEquals(ChocolateFeast(59861,219,38856).get_total_chocolates(),273)
        self.assertEquals(ChocolateFeast(10645,94,10622).get_total_chocolates(),113)
        self.assertEquals(ChocolateFeast(4338,39,2556).get_total_chocolates(),111)
        self.assertEquals(ChocolateFeast(78479,513,59943).get_total_chocolates(),152)
        self.assertEquals(ChocolateFeast(12574,11303,6650).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(23333,15178,16444).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(46143,19994,24879).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(7747,59,3587).get_total_chocolates(),131)
        self.assertEquals(ChocolateFeast(72286,334,69906).get_total_chocolates(),216)
        self.assertEquals(ChocolateFeast(99770,758,69806).get_total_chocolates(),131)
        self.assertEquals(ChocolateFeast(85486,331,47153).get_total_chocolates(),258)
        self.assertEquals(ChocolateFeast(85006,78153,30358).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(6614,3887,5753).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(98046,331,68600).get_total_chocolates(),296)
        self.assertEquals(ChocolateFeast(27454,24335,17798).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(90430,14,37004).get_total_chocolates(),6459)
        self.assertEquals(ChocolateFeast(92285,9,56341).get_total_chocolates(),10253)
        self.assertEquals(ChocolateFeast(26628,209,4335).get_total_chocolates(),127)
        self.assertEquals(ChocolateFeast(87158,54024,8721).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(7319,5432,6940).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(83253,31055,76601).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(59908,556,23522).get_total_chocolates(),107)
        self.assertEquals(ChocolateFeast(52587,277,50630).get_total_chocolates(),189)
        self.assertEquals(ChocolateFeast(51942,234,27353).get_total_chocolates(),221)
        self.assertEquals(ChocolateFeast(38224,9603,22293).get_total_chocolates(),3)
        self.assertEquals(ChocolateFeast(39749,326,38757).get_total_chocolates(),121)
        self.assertEquals(ChocolateFeast(94372,326,44544).get_total_chocolates(),289)
        self.assertEquals(ChocolateFeast(31149,292,4735).get_total_chocolates(),106)
        self.assertEquals(ChocolateFeast(60695,347,28355).get_total_chocolates(),174)
        self.assertEquals(ChocolateFeast(29297,91,15445).get_total_chocolates(),321)
        self.assertEquals(ChocolateFeast(60608,543,17689).get_total_chocolates(),111)
        self.assertEquals(ChocolateFeast(22268,28,7954).get_total_chocolates(),795)
        self.assertEquals(ChocolateFeast(7628,56,5078).get_total_chocolates(),136)
        self.assertEquals(ChocolateFeast(17404,9882,3646).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(26377,11981,13848).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(60217,144,24).get_total_chocolates(),436)
        self.assertEquals(ChocolateFeast(41835,89,34999).get_total_chocolates(),470)
        self.assertEquals(ChocolateFeast(77879,179,31082).get_total_chocolates(),435)
        self.assertEquals(ChocolateFeast(6776,51,5473).get_total_chocolates(),132)
        self.assertEquals(ChocolateFeast(64418,127,54187).get_total_chocolates(),507)
        self.assertEquals(ChocolateFeast(88748,825,25437).get_total_chocolates(),107)
        self.assertEquals(ChocolateFeast(69332,29,21687).get_total_chocolates(),2390)
        self.assertEquals(ChocolateFeast(38654,37809,27752).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(84880,757,76541).get_total_chocolates(),112)
        self.assertEquals(ChocolateFeast(28441,7705,4276).get_total_chocolates(),3)
        self.assertEquals(ChocolateFeast(78037,667,61963).get_total_chocolates(),116)
        self.assertEquals(ChocolateFeast(34387,325,2593).get_total_chocolates(),105)
        self.assertEquals(ChocolateFeast(24774,53,23837).get_total_chocolates(),467)
        self.assertEquals(ChocolateFeast(58803,431,8270).get_total_chocolates(),136)
        self.assertEquals(ChocolateFeast(74284,609,6760).get_total_chocolates(),121)
        self.assertEquals(ChocolateFeast(11884,51,6499).get_total_chocolates(),233)
        self.assertEquals(ChocolateFeast(24769,7,13138).get_total_chocolates(),3538)
        self.assertEquals(ChocolateFeast(7723,72,917).get_total_chocolates(),107)
        self.assertEquals(ChocolateFeast(36919,262,36431).get_total_chocolates(),140)
        self.assertEquals(ChocolateFeast(55480,496,18054).get_total_chocolates(),111)
        self.assertEquals(ChocolateFeast(83218,572,270).get_total_chocolates(),145)
        self.assertEquals(ChocolateFeast(11896,106,8061).get_total_chocolates(),112)
        self.assertEquals(ChocolateFeast(92868,119,61630).get_total_chocolates(),780)
        self.assertEquals(ChocolateFeast(67029,42406,65482).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(16151,5659,13619).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(54305,395,17271).get_total_chocolates(),137)
        self.assertEquals(ChocolateFeast(74054,72920,65545).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(45753,196,28551).get_total_chocolates(),233)
        self.assertEquals(ChocolateFeast(4145,3019,2607).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(80026,8,43540).get_total_chocolates(),10003)
        self.assertEquals(ChocolateFeast(42342,176,13286).get_total_chocolates(),240)
        self.assertEquals(ChocolateFeast(8281,23,5518).get_total_chocolates(),360)
        self.assertEquals(ChocolateFeast(94516,341,48463).get_total_chocolates(),277)
        self.assertEquals(ChocolateFeast(36675,89,10736).get_total_chocolates(),412)
        self.assertEquals(ChocolateFeast(88109,31038,13905).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(45222,23238,5933).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(78900,66292,45302).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(6970,67,2422).get_total_chocolates(),104)
        self.assertEquals(ChocolateFeast(75850,72918,69563).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(8833,88,8220).get_total_chocolates(),100)
        self.assertEquals(ChocolateFeast(89054,50341,12699).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(26996,142,7001).get_total_chocolates(),190)
        self.assertEquals(ChocolateFeast(21774,73,13594).get_total_chocolates(),298)
        self.assertEquals(ChocolateFeast(95131,235,94956).get_total_chocolates(),404)
        self.assertEquals(ChocolateFeast(17489,154,13015).get_total_chocolates(),113)
        self.assertEquals(ChocolateFeast(83036,625,41851).get_total_chocolates(),132)
        self.assertEquals(ChocolateFeast(92256,33304,78345).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(68740,68,34109).get_total_chocolates(),1010)
        self.assertEquals(ChocolateFeast(56741,44464,44937).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(76527,406,24956).get_total_chocolates(),188)
        self.assertEquals(ChocolateFeast(40312,150,34596).get_total_chocolates(),268)
        self.assertEquals(ChocolateFeast(69422,39,38093).get_total_chocolates(),1780)
        self.assertEquals(ChocolateFeast(68456,46948,50268).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(99919,959,59041).get_total_chocolates(),104)
        self.assertEquals(ChocolateFeast(22424,171,15391).get_total_chocolates(),131)
        self.assertEquals(ChocolateFeast(85156,516,5140).get_total_chocolates(),165)
        self.assertEquals(ChocolateFeast(4432,30,4053).get_total_chocolates(),147)
        self.assertEquals(ChocolateFeast(2497,1604,1925).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(62708,601,7268).get_total_chocolates(),104)
        self.assertEquals(ChocolateFeast(55238,8343,8602).get_total_chocolates(),6)
        self.assertEquals(ChocolateFeast(18786,34,16023).get_total_chocolates(),552)
        self.assertEquals(ChocolateFeast(48086,83,22018).get_total_chocolates(),579)
        self.assertEquals(ChocolateFeast(37739,143,22531).get_total_chocolates(),263)
        self.assertEquals(ChocolateFeast(17425,5,9471).get_total_chocolates(),3485)
        self.assertEquals(ChocolateFeast(8275,30,1023).get_total_chocolates(),275)
        self.assertEquals(ChocolateFeast(68263,28,56980).get_total_chocolates(),2437)
        self.assertEquals(ChocolateFeast(62805,8203,47015).get_total_chocolates(),7)
        self.assertEquals(ChocolateFeast(62145,224,8814).get_total_chocolates(),277)
        self.assertEquals(ChocolateFeast(58714,416,17333).get_total_chocolates(),141)
        self.assertEquals(ChocolateFeast(98043,457,91858).get_total_chocolates(),214)
        self.assertEquals(ChocolateFeast(97605,807,28306).get_total_chocolates(),120)
        self.assertEquals(ChocolateFeast(18571,154,16864).get_total_chocolates(),120)
        self.assertEquals(ChocolateFeast(72333,638,12814).get_total_chocolates(),113)
        self.assertEquals(ChocolateFeast(42501,367,15557).get_total_chocolates(),115)
        self.assertEquals(ChocolateFeast(13185,3869,11205).get_total_chocolates(),3)
        self.assertEquals(ChocolateFeast(57235,40867,11374).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(62269,30396,37489).get_total_chocolates(),2)
        self.assertEquals(ChocolateFeast(40087,386,32766).get_total_chocolates(),103)
        self.assertEquals(ChocolateFeast(7543,44,4454).get_total_chocolates(),171)
        self.assertEquals(ChocolateFeast(80973,711,45988).get_total_chocolates(),113)
        self.assertEquals(ChocolateFeast(26849,257,19705).get_total_chocolates(),104)
        self.assertEquals(ChocolateFeast(57397,165,16054).get_total_chocolates(),347)
        self.assertEquals(ChocolateFeast(52662,172,22539).get_total_chocolates(),306)
        self.assertEquals(ChocolateFeast(36141,152,25515).get_total_chocolates(),237)
        self.assertEquals(ChocolateFeast(96333,163,91785).get_total_chocolates(),591)
        self.assertEquals(ChocolateFeast(5327,34,5080).get_total_chocolates(),156)
        self.assertEquals(ChocolateFeast(1528,131,1308).get_total_chocolates(),11)
        self.assertEquals(ChocolateFeast(22118,11,8112).get_total_chocolates(),2010)
        self.assertEquals(ChocolateFeast(30285,52,18617).get_total_chocolates(),582)
        self.assertEquals(ChocolateFeast(22094,4104,4118).get_total_chocolates(),5)
        self.assertEquals(ChocolateFeast(98446,76,73069).get_total_chocolates(),1295)
        self.assertEquals(ChocolateFeast(67107,18429,56091).get_total_chocolates(),3)
        self.assertEquals(ChocolateFeast(19325,175,14156).get_total_chocolates(),110)
        self.assertEquals(ChocolateFeast(51090,343,13666).get_total_chocolates(),148)
        self.assertEquals(ChocolateFeast(54259,39030,44860).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(53328,39959,48103).get_total_chocolates(),1)
        self.assertEquals(ChocolateFeast(33533,245,16064).get_total_chocolates(),136)
        self.assertEquals(ChocolateFeast(50204,261,36997).get_total_chocolates(),192)
        self.assertEquals(ChocolateFeast(4586,14,98).get_total_chocolates(),330)
        self.assertEquals(ChocolateFeast(63548,277,26922).get_total_chocolates(),229)
        self.assertEquals(ChocolateFeast(78711,514,63338).get_total_chocolates(),153)

suite = unittest.TestLoader().loadTestsFromTestCase(ChocolateFeastTest)
unittest.TextTestRunner(verbosity=2).run(suite)