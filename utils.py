def get_all_currency():
    return [
        ("USD", 12650),
        ("EUR", 13700),
        ("RUB", 140),
    ]


def get_currency_by_code(code: str):
    currencies = get_all_currency()
    for currency in currencies:
        if currency[0].lower() == code.lower():
            return currency
    return None