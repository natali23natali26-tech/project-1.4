class Product:
    """
    Класс, представляющий товар.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Цена товара в рублях (может включать копейки).
        quantity (int): Количество товара в наличии (в штуках).
    """

    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return (
            f"Product(name='{self.name}', "
            f"price={self.price}, "
            f"quantity={self.quantity})"
        )
