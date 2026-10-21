# 01
def get_header(data):
    """
    Ustun nomlarini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        list: ustun nomlari
    """
    return


# 02
def get_rows_count(data):
    """
    Sarlavhadan tashqari nechta mahsulot qatori borligini qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        int: qatorlar soni
    """
    return


# 03
def get_products(data):
    """
    Mahsulot nomlarini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        list: mahsulotlar
    """
    return


# 04
def get_quantities(data):
    """
    Miqdorlarni butun sonlar ro'yxati ko'rinishida qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        list: miqdorlar
    """
    return


# 05
def get_units(data):
    """
    O'lchov birliklarini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        list: birliklar
    """
    return


# 06
def get_prices(data):
    """
    Narxlarni butun sonlar ro'yxati ko'rinishida qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        list: narxlar
    """
    return


# 07
def get_first_product(data):
    """
    Ro'yxatdagi birinchi mahsulot nomini qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        str: mahsulot nomi
    """
    return


# 08
def get_last_product(data):
    """
    Ro'yxatdagi oxirgi mahsulot nomini qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        str: mahsulot nomi
    """
    return


# 09
def get_product_price(data, nom):
    """
    Mahsulot nomi berilgan. Uning narxini qaytaring. Mahsulot topilmasa, -1 qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn
        nom (str): mahsulot nomi

    Qaytaradi:
        int: narx
    """
    return


# 10
def count_unit(data, birlik):
    """
    O'lchov birligi berilgan. Shu birlikda o'lchanadigan mahsulotlar sonini qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn
        birlik (str): o'lchov birligi

    Qaytaradi:
        int: mahsulotlar soni
    """
    return


# 11
def get_expensive(prices):
    """
    Narxlar ro'yxati berilgan (get_prices() natijasi). Eng qimmat mahsulotning indeksini qaytaring.

    Argumentlar:
        prices (list): narxlar ro'yxati

    Qaytaradi:
        int: indeks
    """
    return


# 12
def get_cheapest_product(data):
    """
    Eng arzon mahsulot nomini qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        str: mahsulot nomi
    """
    return


# 13
def get_totals(data):
    """
    Har bir mahsulot uchun to'lanadigan summani (miqdor × narx) ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        list: summalar
    """
    return


# 14
def get_total_sum(data):
    """
    Allamurodning butun bozorlik ro'yxati uchun jami xarajatni qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        int: jami summa
    """
    return


# 15
def get_most_spent_product(data):
    """
    Eng ko'p pul sarflanadigan mahsulot nomini qaytaring (miqdor × narx bo'yicha).

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        str: mahsulot nomi
    """
    return


# 16
def get_products_by_unit(data, birlik):
    """
    O'lchov birligi berilgan. Shu birlikdagi mahsulotlar nomlarini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn
        birlik (str): o'lchov birligi

    Qaytaradi:
        list: mahsulotlar
    """
    return


# 17
def get_products_above(data, narx):
    """
    Narx berilgan. Narxi shu summadan qimmat bo'lgan mahsulotlar nomlarini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn
        narx (int): chegara narx

    Qaytaradi:
        list: mahsulotlar
    """
    return


# 18
def get_average_price(data):
    """
    Mahsulotlarning o'rtacha narxini 2 xona aniqlikda yaxlitlab qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn

    Qaytaradi:
        float: o'rtacha narx
    """
    return


# 19
def get_budget_left(data, byudjet):
    """
    Allamurodning oylik bozorlik byudjeti berilgan. Barcha mahsulotlar olingandan keyin qancha pul qolishini qaytaring (manfiy bo'lsa, byudjet yetmaydi).

    Argumentlar:
        data (str): data.csv faylidagi matn
        byudjet (int): byudjet

    Qaytaradi:
        int: qoldiq
    """
    return


# 20
def get_receipt_line(data, nom):
    """
    Mahsulot nomi berilgan. "<Mahsulot>: <miqdor> <birlik> x <narx> = <summa> so'm" ko'rinishidagi chek qatorini qaytaring. Mahsulot topilmasa, "Topilmadi" qaytaring.

    Argumentlar:
        data (str): data.csv faylidagi matn
        nom (str): mahsulot nomi

    Qaytaradi:
        str: chek qatori
    """
    return


# Fayldan ma'lumotni o'qish
f = open("data.csv", encoding="utf-8")
data = f.read()
f.close()
