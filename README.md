# Bozorlik ro'yxati bilan ishlash

`data.csv` faylida Allamurodning oylik bozorlik ro'yxati berilgan: mahsulot nomi, miqdori, o'lchov birligi va bir birlik narxi (so'm).
Barcha funksiyalar `main.py` faylida. Fayl matni `data` o'zgaruvchisiga o'qiladi va funksiyalarga beriladi.

## 01. get_header

Ustun nomlarini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: ["Mahsulot", "Miqdor", "Birlik", "Narx"]
```

---

## 02. get_rows_count

Sarlavhadan tashqari nechta mahsulot qatori borligini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 15
```

---

## 03. get_products

Mahsulot nomlarini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: ["Non", "Sut", "Tuxum", ..., "Banan"]
```

---

## 04. get_quantities

Miqdorlarni butun sonlar ro'yxati ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: [30, 8, 30, ..., 3]
```

---

## 05. get_units

O'lchov birliklarini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: ["dona", "litr", "dona", ..., "kg"]
```

---

## 06. get_prices

Narxlarni butun sonlar ro'yxati ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: [3000, 12000, 1500, ..., 24000]
```

---

## 07. get_first_product

Ro'yxatdagi birinchi mahsulot nomini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: "Non"
```

---

## 08. get_last_product

Ro'yxatdagi oxirgi mahsulot nomini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: "Banan"
```

---

## 09. get_product_price

Mahsulot nomi berilgan. Uning narxini qaytaring. Mahsulot topilmasa, -1 qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni), nom="Sut"
Chiqarish: 12000
```

**Misol 2:**

```Python
Kirish: data (data.csv matni), nom="Qaymoq"
Chiqarish: -1
```

---

## 10. count_unit

O'lchov birligi berilgan. Shu birlikda o'lchanadigan mahsulotlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni), birlik="kg"
Chiqarish: 9
```

**Misol 2:**

```Python
Kirish: data (data.csv matni), birlik="litr"
Chiqarish: 2
```

---

## 11. get_expensive

Narxlar ro'yxati berilgan (`get_prices()` natijasi). Eng qimmat mahsulotning indeksini qaytaring.

**Misol 1:**

```Python
Kirish: prices = get_prices(data)
Chiqarish: 4
```

---

## 12. get_cheapest_product

Eng arzon mahsulot nomini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: "Tuxum"
```

---

## 13. get_totals

Har bir mahsulot uchun to'lanadigan summani (miqdor × narx) ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: [90000, 96000, 45000, ..., 72000]
```

---

## 14. get_total_sum

Allamurodning butun bozorlik ro'yxati uchun jami xarajatni qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 1247000
```

---

## 15. get_most_spent_product

Eng ko'p pul sarflanadigan mahsulot nomini qaytaring (miqdor × narx bo'yicha).

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: "Go'sht"
```

---

## 16. get_products_by_unit

O'lchov birligi berilgan. Shu birlikdagi mahsulotlar nomlarini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni), birlik="litr"
Chiqarish: ["Sut", "Yog'"]
```

**Misol 2:**

```Python
Kirish: data (data.csv matni), birlik="quti"
Chiqarish: ["Choy", "Makaron"]
```

---

## 17. get_products_above

Narx berilgan. Narxi shu summadan qimmat bo'lgan mahsulotlar nomlarini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni), narx=24000
Chiqarish: ["Go'sht", "Choy", "Pishloq"]
```

---

## 18. get_average_price

Mahsulotlarning o'rtacha narxini 2 xona aniqlikda yaxlitlab qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni)
Chiqarish: 22566.67
```

---

## 19. get_budget_left

Allamurodning oylik bozorlik byudjeti berilgan. Barcha mahsulotlar olingandan keyin qancha pul qolishini qaytaring (manfiy bo'lsa, byudjet yetmaydi).

**Misol 1:**

```Python
Kirish: data (data.csv matni), byudjet=1500000
Chiqarish: 253000
```

**Misol 2:**

```Python
Kirish: data (data.csv matni), byudjet=1000000
Chiqarish: -247000
```

---

## 20. get_receipt_line

Mahsulot nomi berilgan. "<Mahsulot>: <miqdor> <birlik> x <narx> = <summa> so'm" ko'rinishidagi chek qatorini qaytaring. Mahsulot topilmasa, "Topilmadi" qaytaring.

**Misol 1:**

```Python
Kirish: data (data.csv matni), nom="Go'sht"
Chiqarish: "Go'sht: 4 kg x 95000 = 380000 so'm"
```

**Misol 2:**

```Python
Kirish: data (data.csv matni), nom="Qaymoq"
Chiqarish: "Topilmadi"
```

