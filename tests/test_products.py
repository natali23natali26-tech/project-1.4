import pytest
from unittest.mock import patch
from src.products import Product, Smartphone, LawnGrass
from src.category import Category


# === ТЕСТЫ ДЛЯ Product ===

@pytest.mark.parametrize(
    "name, description, price, quantity",
    [
        ("Телефон", "Смартфон", 20000.0, 10),
        ("Ноутбук", "Игровой", 80000.5, 5),
        ("", "Без названия", 1000.0, 1),
        ("Камера", "", 30000.0, 0),
    ]
)
def test_product_initialization(name, description, price, quantity):
    """Проверяет, что объект Product корректно инициализируется."""
    product = Product(name, description, price, quantity)

    assert product.name == name
    assert product.description == description
    assert product.price == price
    assert product.quantity == quantity


@pytest.mark.parametrize(
    "initial_price, invalid_price",
    [
        (1000.0, -500),
        (2000.0, 0),
    ]
)
def test_product_price_setter_invalid_values(initial_price, invalid_price):
    """Проверяет, что сеттер не позволяет установить некорректную цену."""
    product = Product("Тест", "Описание", initial_price, 10)

    with patch("builtins.print") as mock_print:
        product.price = invalid_price
        mock_print.assert_called_once_with(
            "Цена не должна быть нулевая или отрицательная"
        )
        assert product.price == initial_price  # цена не изменилась


def test_product_price_setter_valid_value():
    """Проверяет, что корректная цена устанавливается."""
    product = Product("Тест", "Описание", 1000.0, 10)
    product.price = 1500.0
    assert product.price == 1500.0


def test_product_str_representation():
    """Проверяет строковое представление продукта."""
    product = Product("Телефон", "Смартфон", 20000.5, 5)
    expected = "Телефон, 20000 руб. Остаток: 5 шт."
    assert str(product) == expected


def test_product_repr_representation():
    """Проверяет repr-представление продукта."""
    product = Product("Телефон", "Смартфон", 20000.0, 5)
    expected = "Product(name='Телефон', price=20000.0, quantity=5)"
    assert repr(product) == expected


@pytest.mark.parametrize(
    "price_a, quantity_a, price_b, quantity_b, expected_total",
    [
        (100, 10, 200, 2, 1400),
        (50, 5, 30, 10, 550),
        (1000, 1, 500, 2, 2000),
    ]
)
def test_product_add_method(price_a, quantity_a,
                            price_b, quantity_b,
                            expected_total):
    """Проверяет, что __add__ корректно считает общую стоимость запасов."""
    a = Product("A", "Описание", price_a, quantity_a)
    b = Product("B", "Описание", price_b, quantity_b)

    total = a + b
    assert total == expected_total


def test_product_add_method_type_error():
    """Проверяет, что __add__ выбрасывает T
    ypeError при сложении с не-Product."""
    product = Product("Тест",
                      "Описание",
                      1000.0, 1)
    with pytest.raises(TypeError,
                       match="Складывать можно только продукты"):
        product + "not a product"


def test_product_add_method_different_types_error():
    """Проверяет, что __add__ не позволяет складывать
    разные типы продуктов."""
    class OtherProduct(Product):
        pass

    a = Product("A", "Описание",
                100, 1)
    b = OtherProduct("B", "Описание",
                     200, 1)

    with pytest.raises(TypeError,
                       match="Нельзя складывать товары разных типов"):
        a + b


def test_product_radd_for_sum():
    """Проверяет, что sum() работает с продуктами."""
    products = [
        Product("A", "Описание",
                100, 2),  # 200
        Product("B", "Описание",
                50, 4),   # 200
        Product("C", "Описание",
                30, 10),  # 300
    ]
    total = sum(products)
    assert total == 700


# === ТЕСТЫ ДЛЯ НАСЛЕДНИКОВ ===

@pytest.mark.parametrize(
    "name, description, price, quantity, "
    "efficiency, model, memory, color",
    [
        ("iPhone", "Флагман", 100000.0, 5, 98.5,
         "15 Pro", 512, "Чёрный"),
        ("Samsung", "Android", 80000.0, 3,
         "Snapdragon", "S23", 256, "Белый"),
    ]
)
def test_smartphone_initialization(name, description, price, quantity,
                                   efficiency, model, memory, color):
    """Проверяет инициализацию Smartphone."""
    phone = Smartphone(name, description, price, quantity,
                       efficiency, model, memory, color)

    assert phone.name == name
    assert phone.price == price
    assert phone.quantity == quantity
    assert phone.efficiency == str(efficiency)
    assert phone.model == model
    assert phone.memory == memory
    assert phone.color == color


def test_smartphone_repr():
    """Проверяет repr для Smartphone."""
    phone = Smartphone("iPhone", "Флагман",
                       100000.0, 5,
                       98.5, "15 Pro",
                       512, "Чёрный")
    expected = ("Smartphone(name='iPhone', price=100000.0, "
                "quantity=5, efficiency='98.5', model='15 Pro', "
                "memory=512, color='Чёрный')")
    assert repr(phone) == expected


@pytest.mark.parametrize(
    "name, description, price, quantity, country, "
    "germination_period, color",
    [
        ("Газон", "Зелёный", 500.0, 10, "Россия",
         "14 дней", "Зелёный"),
        ("Трава", "Выносливая", 400.0, 20, "Германия",
         "10 дней", "Тёмно-зелёный"),
    ]
)
def test_lawngrass_initialization(name, description, price, quantity,
                                  country, germination_period, color):
    """Проверяет инициализацию LawnGrass."""
    grass = LawnGrass(name, description, price, quantity,
                      country, germination_period, color)

    assert grass.name == name
    assert grass.price == price
    assert grass.quantity == quantity
    assert grass.country == country
    assert grass.germination_period == germination_period
    assert grass.color == color


def test_lawngrass_repr():
    """Проверяет repr для LawnGrass."""
    grass = LawnGrass("Газон", "Зелёный",
                      500.0, 10,
                      "Россия", "14 дней",
                      "Зелёный")
    expected = ("LawnGrass(name='Газон', price=500.0, quantity=10, "
                "country='Россия', germination_period='14 дней', "
                "color='Зелёный')")
    assert repr(grass) == expected


# === ТЕСТЫ ДЛЯ Category ===

@pytest.mark.parametrize(
    "cat_name, cat_description, product_count_in_list",
    [
        ("Смартфоны", "Умные телефоны", 3),
        ("Телевизоры", "Экраны большого размера", 1),
        ("Пустая категория", "Нет товаров", 0),
    ]
)
def test_category_initialization(cat_name,
                                 cat_description,
                                 product_count_in_list):
    """Проверяет, что объект Category корректно инициализируется."""
    products = [
        Product(f"Товар_{i}", f"Описание_{i}",
                1000.0, 1)
        for i in range(product_count_in_list)
    ]

    category = Category(cat_name, cat_description, products)

    assert category.name == cat_name
    assert category.description == cat_description

    if product_count_in_list == 0:
        assert category.products == ""
    else:
        lines = category.products.strip().split("\n")
        assert len(lines) == product_count_in_list


def test_category_str_representation():
    """Проверяет строковое представление категории."""
    product1 = Product("Телефон", "Смартфон",
                       20000.0, 5)
    product2 = Product("Ноутбук", "Игровой",
                       80000.0, 2)
    category = Category("Электроника",
                        "Цифровые устройства",
                        [product1, product2])

    expected = "Электроника, количество продуктов: 7 шт."
    assert str(category) == expected


def test_category_repr_representation():
    """Проверяет repr-представление категории."""
    products = [Product("A", "Описание",
                        100, 1), Product("B",
                                         "Описание",
                                         200, 1)]
    category = Category("Категория",
                        "Описание", products)
    expected = "Category(name='Категория', products_count=2)"
    assert repr(category) == expected


def test_category_products_property():
    """Проверяет, что геттер products использует str(product)."""
    product1 = Product("Телефон", "Смартфон",
                       20000.5, 5)
    product2 = Product("Ноутбук", "Игровой",
                       80000.0, 1)
    category = Category("Электроника",
                        "Цифровые устройства",
                        [product1, product2])

    expected = (
        "Телефон, 20000 руб. Остаток: 5 шт.\n"
        "Ноутбук, 80000 руб. Остаток: 1 шт."
    )
    assert category.products == expected


def test_category_add_product_type_error():
    """Проверяет, что add_product выбрасывает TypeError
     при передаче не-Product."""
    category = Category("Тест",
                        "Описание",
                        [])
    with pytest.raises(TypeError, match="Можно добавлять только товары"):
        category.add_product("not a product")


# === ТЕСТЫ СЧЁТЧИКОВ С ИСПОЛЬЗОВАНИЕМ patch ===

@patch.multiple(Category, category_count=0, product_count=0)
def test_category_and_product_count_incremented_correctly():
    """Проверяет, что счётчики увеличиваются корректно."""
    assert Category.category_count == 0
    assert Category.product_count == 0

    product1 = Product("P1", "Desc",
                       1000.0, 5)
    product2 = Product("P2", "Desc",
                       2000.0, 3)
    product3 = Product("P3", "Desc",
                       1500.0, 7)

    Category("Кат1", "Описание",
             [product1, product2])
    Category("Кат2", "Описание",
             [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3


# === ТЕСТЫ ДЛЯ new_product ===

def test_new_product_without_list():
    """Проверяет, что new_product создаёт продукт,
    если список не передан."""
    data = {
        "name": "Новый телефон",
        "description": "Флагман",
        "price": 90000.0,
        "quantity": 10
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Новый телефон"
    assert product.price == 90000.0
    assert product.quantity == 10


def test_new_product_with_list_updates_existing():
    """Проверяет, что new_product обновляет существующий товар."""
    existing = Product("Телефон",
                       "Смартфон",
                       20000.0, 5)
    products = [existing]

    new_data = {
        "name": "Телефон",
        "description": "Обновлённый",
        "price": 25000.0,
        "quantity": 3
    }
    result = Product.new_product(new_data, products)
    assert result is existing
    assert result.quantity == 8
    assert result.price == 25000.0


def test_new_product_with_list_creates_new():
    """Проверяет, что new_product создаёт новый товар, если нет совпадений."""
    existing = Product("Телефон", "Смартфон",
                       20000.0, 5)
    products = [existing]

    new_data = {
        "name": "Часы",
        "description": "Умные",
        "price": 15000.0,
        "quantity": 2
    }
    result = Product.new_product(new_data, products)
    assert result.name == "Часы"
    assert result in products
    assert len(products) == 2
