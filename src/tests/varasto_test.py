import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_init_korjaa_tilavuuden_ja_saldon_tyhjaksi_jos_virhe(self):
        self.varasto = Varasto(-1, -1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_init_saldo_oikein_kun_tilavuuden_rajoissa(self):
        self.varasto = Varasto(10, 8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_init_saldo_oikein_kun_ei_tilavuuden_rajoissa(self):
        self.varasto = Varasto(10, 12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisaa_saldoa_jos_virheellinen_lisays(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, -1)#Tähän kuuluu 0

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_saldoa_liikaa(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran_kun_maara_liian_pieni(self):
        self.varasto.lisaa_varastoon(6)

        saatu_maara = self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_palauttaa_oikean_maaran_kun_maara_on_liian_suuri(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test__str__(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(self.varasto.saldo, 6)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

        self.assertAlmostEqual(self.varasto.__str__(), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
