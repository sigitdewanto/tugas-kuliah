def hitung_rata2(data):
    """
    Menghitung nilai rata-rata dari data yang diberikan. Data yang diberikan harus berupa iterable
    yang berisi nilai integer, long integer, atau float.

    :param data: iterable yang elemen-elemennya merupakan nilai integer, long integer, atau float.
    :return: nilai rata-rata
    :rtype: float
    """
    cacah_data = len(data)
    if cacah_data == 0:
        raise Exception('Data tidak boleh kosong!')

    return float(sum(data)) / cacah_data
