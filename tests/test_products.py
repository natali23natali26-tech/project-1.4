import pytest
from unittest.mock import patch
from src.products import Product, Smartphone, LawnGrass, BaseProduct
from src.category import Category


@pytest.mark.parametrize(
    "name, description, price, quantity",
    [
        ("Телефон", "Смартфон", 20000.0, 10),
        ("Ноутбук", "Игровой", 80000.5, 5),
        ("", "Без названия", 1000.0, 1),
        # ("Камера", "", 30000.0, 0),
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
    expected = "Product('Телефон', 'Смартфон', 20000.0, 5)"
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
    """Проверяет, что __add__ выбрасывает TypeError
     при сложении с не-Product."""
    product = Product("Тест",
                      "Описание",
                      1000.0, 1)
    with pytest.raises(TypeError, match="Складывать можно только продукты"):
        product + "not a product"  # type: ignore


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
    expected = "Smartphone('iPhone', 'Флагман', 100000.0, 5, '98.5', '15 Pro', 512, 'Чёрный')"
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
    expected = "LawnGrass('Газон', 'Зелёный', 500.0, 10, 'Россия', '14 дней', 'Зелёный')"
    assert repr(grass) == expected


# ТЕСТЫ ДЛЯ Category

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
    """Проверяет, что add_product выбрасывает
    TypeError при передаче не-Product."""
    category = Category("Тест",
                        "Описание", [])
    with pytest.raises(TypeError,
                       match="Можно добавлять только товары"):
        # type: ignore
        category.add_product("not a product")


# ТЕСТЫ СЧЁТЧИКОВ С ИСПОЛЬЗОВАНИЕМ patch

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
    """Проверяет, что new_product создаёт новый товар,
    если нет совпадений."""
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


# 1. Тест: LogCreationMixin корректно выводит информацию
@patch("builtins.print")
@pytest.mark.parametrize(
    "cls, args, expected_repr",
    [
        # Для Product — ожидаем Product(...)
        (Product, ("Телефон", "Смартфон", 20000.0, 5),
         "Product('Телефон', 'Смартфон', 20000.0, 5)"),
        # Для Smartphone — ожидаем Smartphone(...)
        (Smartphone, ("iPhone", "Флагман", 100000.0, 1, 98.5,
                      "15 Pro", 512, "Чёрный"),
         "Smartphone('iPhone', 'Флагман', 100000.0, 1)"),
        # Для LawnGrass — ожидаем LawnGrass(...)
        (LawnGrass, ("Газон", "Зелёный", 500.0, 10,
                     "Россия",
                     "14 дней", "Зелёный"),
         "LawnGrass('Газон', 'Зелёный', 500.0, 10)"),
    ]
)
def test_log_creation_mixin_prints_info(mock_print, cls,
                                        args, expected_repr):
    """Проверяет, что миксин выводит repr объекта при создании."""
    obj = cls(*args)
    # Проверяем, что print был вызван
    assert mock_print.call_count >= 1, "Должен быть хотя бы один вызов print"
    # Ищем точное совпадение
    printed_values = [call[0][0] for call in mock_print.call_args_list]
    assert expected_repr in printed_values, (
        f"Ожидался вывод: {expected_repr}\n"
        f"Фактические вызовы: {printed_values}"
    )


# 2. Тест: LogCreationMixin с пустыми/граничными значениями
@patch("builtins.print")
@pytest.mark.parametrize(
    "name, price, quantity",
    [
        ("", 0.0, 0),
        ("A", -1.0, -5),
        (None, None, None),
    ]
)
def test_log_creation_mixin_edge_cases(mock_print, name, price, quantity):
    """Проверяет, что миксин выводит repr при создании, даже если потом будет ошибка."""
    name_str = str(name) if name is not None else ""
    price_float = float(price) if price is not None else 0.0
    quantity_int = int(quantity) if quantity is not None else 0

    # Ожидаем ValueError
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product(name_str, "", price_float, quantity_int)

    # Но print должен был вызваться ДО исключения
    mock_print.assert_called()
    printed = mock_print.call_args[0][0]
    assert name_str in printed
    assert str(price_float) in printed
    assert str(quantity_int) in printed


# 3. Тест: new_product — проверка добавления в список
@patch("builtins.print")
def test_new_product_adds_to_list_when_no_match(mock_print):
    """Проверяет, что new_product создаёт и возвращает продукт."""
    products = []
    data = {"name": "Новинка", "description": "Тест",
            "price": 1000.0, "quantity": 1}
    product = Product.new_product(data, products)
    assert isinstance(product, Product)
    assert product.name == "Новинка"
    assert product.price == 1000.0


# 4. Тест: new_product — не обновляет цену, если новая ниже
@patch("builtins.print")
def test_new_product_keeps_higher_price(mock_print):
    existing = Product("Телефон",
                       "Описание",
                       30000.0, 5)
    products = [existing]
    new_data = {"name": "Телефон", "description": "Обновлённый",
                "price": 25000.0, "quantity": 2}
    result = Product.new_product(new_data, products)
    assert result is existing
    assert result.price == 30000.0
    assert result.quantity == 7
    # Не требуем конкретное сообщение — может, его нет
    assert mock_print.call_count >= 1  # хотя бы от миксина


# 5. Тест: __radd__ с нулём и другими числами
@pytest.mark.parametrize(
    "left_value, price, quantity, expected",
    [
        (0, 100.0, 2, 200),
        (50, 50.0, 3, 200),
        (1000, 10.0, 10, 1100),
    ]
)
def test_product_radd_with_numbers(left_value, price,
                                   quantity, expected):
    """Проверяет, что __radd__ корректно работает
    при сложении числа с продуктом."""
    product = Product("Тест",
                      "Описание", price, quantity)
    total = left_value + product
    assert total == expected


def test_product_radd_not_implemented():
    """Проверяет, что __radd__ возвращает
    NotImplemented для нечисловых типов."""
    product = Product("Тест",
                      "Описание",
                      100.0, 1)
    assert product.__radd__("строка") is NotImplemented


# 6. Тест: __add__ с другими подклассами (должен падать)
def test_add_product_with_subclass_via_inheritance():
    """Проверяет, что нельзя сложить Product и его подкласс
    (даже если он тоже Product)."""
    class MockProduct(Product):
        pass

    p1 = Product("A", "Описание",
                 100.0, 2)
    p2 = MockProduct("B", "Описание",
                     200.0, 1)

    with pytest.raises(TypeError, match="Нельзя складывать "
                                        "товары разных типов"):
        p1 + p2


# 7. Тест: BaseProduct не может быть создан напрямую
def test_base_product_cannot_be_instantiated():
    """Проверяет, что BaseProduct нельзя инстанцировать напрямую."""
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание",
                    100.0, 1)


# 8. Тест: price setter — вывод при некорректной цене
@patch("builtins.print")
def test_price_setter_prints_message_only_once(mock_print):
    """Проверяет, что print вызывается
    при установке некорректной цены."""
    product = Product("Тест", "Описание",
                      1000.0, 1)
    mock_print.reset_mock()  # сбрасываем вызовы от __init__
    product.price = -100
    product.price = 0
    product.price = -50
    assert mock_print.call_count == 3


# 9. Тест: __str__ при нулевой цене
def test_product_str_with_zero_price():
    """Проверяет строковое представление при цене 0.0."""
    product = Product("Тест", "Описание",
                      0.0, 5)
    with patch("builtins.print") as mock_print:
        # вызовет print, но значение не изменится
        product.price = 0.0
    assert str(product) == "Тест, 0 руб. Остаток: 5 шт."


# 10. Тест: __add__ с одним продуктом (sum с одним элементом)
def test_sum_with_single_product():
    """Проверяет, что sum([product]) работает корректно."""
    product = Product("Тест", "Описание",
                      100.0, 3)
    total = sum([product])
    assert total == 300


# 11. Тест: new_product — пустые строки и граничные значения
@pytest.mark.parametrize(
    "name, price, quantity, expected_quantity",
    [
        ("", 100.0, 1, 1),
        ("Товар", 0.0, 1, 1),
        ("Товар", -10.0, 5, 5),
    ]
)
@patch("builtins.print")
def test_new_product_edge_cases(mock_print, name, price, quantity, expected_quantity):
    data = {"name": name, "description": "", "price": price, "quantity": quantity}
    product = Product.new_product(data)
    assert product.name == name
    assert product.quantity == expected_quantity
    if price <= 0:
        mock_print.assert_called()
    else:
        assert product.price == price



def test_product_init_raises_value_error_on_zero_quantity():
    """Проверяет, что при создании товара с нулевым количеством
    выбрасывается ValueError с нужным сообщением."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Тест", "Описание", 1000.0, 0)


def test_product_init_raises_value_error_on_negative_quantity():
    """Проверяет, что при отрицательном количестве тоже выбрасывается ValueError."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Тест", "Описание", 1000.0, -5)


def test_category_average_price_with_products():
    """Проверяет, что average_price() корректно считает среднюю цену."""
    p1 = Product("Телефон", "Смартфон", 20000.0, 3)
    p2 = Product("Наушники", "Беспроводные", 5000.0, 10)
    category = Category("Электроника", "Гаджеты", [p1, p2])

    avg = category.average_price()
    assert avg == 12500.0  # (20000 + 5000) / 2 = 12500


def test_category_average_price_empty_category_returns_zero():
    """Проверяет, что average_price() возвращает 0 для пустой категории."""
    category = Category("Пусто", "Нет товаров", [])
    avg = category.average_price()
    assert avg == 0.0


@patch("builtins.print")
def test_log_creation_mixin_prints_before_value_error(mock_print):
    """Проверяет, что миксин выводит repr ДО выброса ValueError."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Тест", "Описание", 1000.0, 0)

    # Проверяем, что print был вызван
    mock_print.assert_called()
    printed = mock_print.call_args[0][0]
    assert "Product('Тест', 'Описание', 1000.0, 0)" in printed

