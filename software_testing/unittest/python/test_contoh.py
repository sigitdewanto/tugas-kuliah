import unittest

from contoh import hitung_rata2


class TestContoh(unittest.TestCase):
    def test_input_tidak_valid(self):
        self.assertRaises(Exception, hitung_rata2, None)
        self.assertRaises(Exception, hitung_rata2, False)
        self.assertRaises(Exception, hitung_rata2, 1)
        self.assertRaises(Exception, hitung_rata2, 0.5)
        self.assertRaises(Exception, hitung_rata2, '123')
        self.assertRaises(Exception, hitung_rata2, ['a', 'b'])

    def test_data_kosong(self):
        self.assertRaises(Exception, hitung_rata2, ())
        self.assertRaises(Exception, hitung_rata2, [])
        self.assertRaises(Exception, hitung_rata2, range(0))
        self.assertRaises(Exception, hitung_rata2, xrange(0))

    def test_data_dengan_satu_elemen(self):
        self.assertEquals(-999999999999, hitung_rata2([-999999999999]))
        self.assertEquals(-999999.999999, hitung_rata2([-999999.999999]))
        self.assertEquals(-2.5, hitung_rata2([-2.5]))
        self.assertEquals(-2, hitung_rata2([-2]))
        self.assertEquals(-1, hitung_rata2([-1]))
        self.assertEquals(-0.25, hitung_rata2([-0.25]))
        self.assertEquals(0, hitung_rata2([0]))
        self.assertEquals(0.25, hitung_rata2([0.25]))
        self.assertEquals(1, hitung_rata2([1]))
        self.assertEquals(2, hitung_rata2([2]))
        self.assertEquals(2.5, hitung_rata2([2.5]))
        self.assertEquals(999999.999999, hitung_rata2([999999.999999]))
        self.assertEquals(999999999999, hitung_rata2([999999999999]))

    def test_data_dengan_semua_nilainya_nol(self):
        self.assertEquals(0, hitung_rata2([0]))
        self.assertEquals(0, hitung_rata2([0, 0]))
        self.assertEquals(0, hitung_rata2([0, 0, 0]))
        self.assertEquals(0, hitung_rata2([0, 0, 0, 0]))
        self.assertEquals(0, hitung_rata2([0, 0, 0, 0, 0]))
        self.assertEquals(0, hitung_rata2([0, 0, 0, 0, 0, 0]))

    def test_data_dengan_macam2_nilai(self):
        self.assertEquals(2, hitung_rata2([2, 2, 2, 2, 2, 2]))
        self.assertEquals(1.5, hitung_rata2([1, 2, 1, 2, 1, 2]))
        self.assertEquals(1.5, hitung_rata2([1.0, 2.0, 1.0, 2.0, 1.0, 2.0]))
        self.assertEquals(83.33333333333333, hitung_rata2([70, 90, 80, 85, 95, 80]))
        self.assertAlmostEquals(83.33333, hitung_rata2([70, 90, 80, 85, 95, 80]), places=5)
        self.assertEquals(2, hitung_rata2([2, 2.0, 2, 2.0, 2, 2.0]))
        self.assertEquals(2, hitung_rata2(range(5)))
        self.assertEquals(2, hitung_rata2(xrange(5)))

if __name__ == '__main__':
    unittest.main()
