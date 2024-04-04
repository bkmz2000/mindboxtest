from pyspark.sql import SparkSession

"""
В PySpark приложении датафреймами (pyspark.sql.DataFrame) заданы продукты, категории и их связи. Каждому продукту может соответствовать несколько категорий или ни одной. А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.

Функция называется double_join__products_no_category. Мне кажется, что она выполняет две разные задачи, чего в коде стоит избегать, поэтому ее название длинное и неудобное. Есть две функции, которые выполняют эти задачи по отдельности, double_join__products_no_category просто возвращает кортеж их результатов.
"""


def double_join(ps, cs, pc):
    joined = ps.join(
        pc,
        ps['id'] == pc['pid'],
        'inner')

    ret = joined.join(
        cs,
        joined['cid'] == cs['id'],
        'inner')

    return ret


def products_no_category(ps, pc):
    return ps.join(
        pc,
        ps['id'] == pc['pid'],
        'left_anti'
    ).select('name')


def double_join__products_no_category(ps, cs, pc):
    return double_join(ps, cs, pc), products_no_category(ps, pc)


spark = SparkSession.builder \
    .appName("mindboxtest") \
    .getOrCreate()


products = spark.createDataFrame(
    [
        (0, 'Laptop'),
        (1, 'Smartphone'),
        (2, 'Headphones'),
        (3, 'Camera'),
        (4, 'Watch'),
        (5, 'Shoes'),
        (6, 'Backpack'),
        (7, 'Sunglasses'),
        (8, 'Perfume'),
        (9, 'Protein')
    ],
    ['id', 'name']
)

categories = spark.createDataFrame(
    [
        (0, 'Electronics'),
        (1, 'Fashion'),
        (2, 'Accessories'),
        (3, 'Health & Fitness'),
        (4, 'Beauty')
    ],
    ['id', 'name']
)

product_category = spark.createDataFrame(
    [
        [1, 1],
        [2, 1],
        [3, 1],
        [4, 1],
        [5, 1],
        [6, 2],
        [7, 2],
        [8, 2],
        [9, 5],
        [10, 4]
    ],
    ['pid', 'cid']
)

double_join__products_no_category(products,
                                  categories,
                                  product_category).show()
