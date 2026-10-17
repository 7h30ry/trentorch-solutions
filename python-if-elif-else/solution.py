def classify_number(x: int | float) -> str:
    """
    Return one of the following strings based on x, checked in
    this exact order using an if/elif/else chain:
      "negative"     if x < 0
      "zero"         if x == 0
      "small"        if 0 < x <= 10
      "large"        if x > 10
    """
    if x < 0:
        return f"negative"
    elif x == 0:
        return f"zero"
    elif 0 < x <= 10:
        return f"small"
    else:
        return f"large"
    pass
