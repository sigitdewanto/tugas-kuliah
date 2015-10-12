#Contoh unit testing untuk fungsi penghitung nilai rata-rata.#

Sebagai referensi bisa dibaca [artikel ini](http://www.drdobbs.com/testing/unit-testing-with-python/240165163).

Fungsi `hitung_rata2` pada file [contoh.py](https://github.com/sigitdewanto/tugas-kuliah/blob/master/software_testing/unittest/python/contoh.py) menerima parameter berupa `iterable` yang elemen-elemennya merupakan nilai numerik, kemudian akan menghitung nilai rata-rata dari data yang diberikan. Jika data yang dimasukkan kosong (`iterable`-nya tidak memiliki elemen), maka fungsi akan melemparkan `Exception`. Jika data yang diberikan valid maka fungsi akan mengembalikan nilai rata-rata dengan tipe `float`.

Pada Python, terdapat modul bawaan bernama `unittest` yang dapat digunakan untuk memudahkan kita dalam melakukan unit testing. Contoh penggunaannya bisa dilihat pada file [test_contoh.py](https://github.com/sigitdewanto/tugas-kuliah/blob/master/software_testing/unittest/python/test_contoh.py ). `test_contoh.py` digunakan untuk melakukan unit test pada fungsi `hitung_rata2`. Kita lihat bahwa di situ kelas `TestContoh` diturunkan dari `unittest.TestCase`. Hal ini dilakukan agar kelas `TestContoh` mewarisi properti dan method dari kelas `TestCase`, sehingga nantinya dapat dijalankan oleh test runner. Setiap method yang berawalan `test_` akan dijalankan oleh test runner sebagai sebuah test.

Kelas `TestCase` juga memiliki method-method untuk melakukan `assertion`. Assertion dilakukan untuk membandingkan antara output aktual yang dihasilkan dengan output yang diharapkan.

* `assertEquals(a, b)` menerima 2 parameter dan akan membandingkan apakah keduanya sama. Jika tidak maka tes dianggap gagal.
* `assertAlmostEquals(a, b, places)` menerima 3 parameter dan membandingkan 2 parameter pertama dengan tingkat ketelitian sesuai parameter ketiga (`places`).
* `assertRaises(exception, callable, param, ...)` akan memanggil `callable` dengan parameter input dari parameter ketiga dan seterusnya, kemudian mengecek apakah `exception` dilemparkan oleh `callable` atau tidak. Jika tidak, maka tes dianggap gagal.