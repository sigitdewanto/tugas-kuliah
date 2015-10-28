import copy


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


def hitung_median(data):
    """
    Menghitung nilai median dari data yang diberikan. Data yang diberikan harus berupa iterable
    yang berisi nilai integer, long integer, atau float.

    :param data: iterable yang elemen-elemennya merupakan nilai integer, long integer, atau float.
    :return: nilai median
    """
    cacah_data = len(data)
    if cacah_data == 0:
        raise Exception('Data tidak boleh kosong!')
    elif cacah_data == 1:
        return data[0]
    elif cacah_data == 2:
        return float(data[0] + data[1]) / 2

    # data disalin agar kita tidak mengubah input
    data_terurut = copy.copy(data)
    data_terurut.sort()

    if cacah_data % 2 == 0:
        return float(data_terurut[(cacah_data / 2) - 1] + data_terurut[cacah_data / 2]) / 2
    else:
        return data_terurut[cacah_data / 2]
