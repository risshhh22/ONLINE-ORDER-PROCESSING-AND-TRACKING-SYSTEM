def validate_qty(q):
    if q <= 0:
        raise ValueError("Invalid quantity")