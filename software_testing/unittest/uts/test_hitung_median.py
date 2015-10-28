import unittest

from statistik import hitung_median


class TestHitungMedian(unittest.TestCase):
    def test_input_tidak_valid(self):
        self.assertRaises(Exception, hitung_median, None)
        self.assertRaises(Exception, hitung_median, False)
        self.assertRaises(Exception, hitung_median, 1)
        self.assertRaises(Exception, hitung_median, 0.5)
        self.assertRaises(Exception, hitung_median, '123')
        self.assertRaises(Exception, hitung_median, ['a', 'b'])
        self.assertRaises(Exception, hitung_median, ['1', 1])

    def test_data_kosong(self):
        self.assertRaises(Exception, hitung_median, ())
        self.assertRaises(Exception, hitung_median, [])
        self.assertRaises(Exception, hitung_median, range(0))

    def test_data_dengan_satu_elemen(self):
        self.assertEquals(0, hitung_median([0]))
        self.assertEquals(1, hitung_median([1]))
        self.assertEquals(-1, hitung_median([-1]))
        self.assertEquals(0.0, hitung_median([0.0]))
        self.assertEquals(1.0, hitung_median([1.0]))
        self.assertEquals(-1.0, hitung_median([-1.0]))

    def test_data_dengan_dua_elemen(self):
        self.assertEquals(0.5, hitung_median([0, 1]))
        self.assertEquals(8.5, hitung_median([8, 9]))
        self.assertEquals(4.5, hitung_median([-1, 10]))
        self.assertEquals(0.5, hitung_median([0.0, 1.0]))
        self.assertEquals(8.5, hitung_median([8.0, 9.0]))
        self.assertEquals(4.5, hitung_median([-1.0, 10.0]))

    def test_data_dengan_cacah_ganjil(self):
        self.assertEquals(1, hitung_median([0, 1, 8]))
        self.assertEquals(8, hitung_median([8, 9, 7]))
        self.assertEquals(-1, hitung_median([-1, 10, -10]))
        self.assertEquals(0.0, hitung_median([0.0, 1.0, -8]))
        self.assertEquals(8.0, hitung_median([8.0, 9.0, 7]))
        self.assertEquals(-1.0, hitung_median([-1.0, 10.0, -10]))

    def test_data_dengan_cacah_genap(self):
        self.assertEquals(1.5, hitung_median([0, 1, 8, 2]))
        self.assertEquals(7.5, hitung_median([8, 9, 7, 5]))
        self.assertEquals(2.0, hitung_median([-1, 10, -10, 5]))
        self.assertEquals(0.5, hitung_median([0.0, 1.0, -8, 3]))
        self.assertEquals(8.5, hitung_median([8.0, 9.0, 7, 99]))
        self.assertEquals(4.5, hitung_median([-1.0, 10.0, -10, 100, -100, 50.0]))

if __name__ == '__main__':
    unittest.main()
