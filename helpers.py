# IMPORTATION STANDARD

# IMPORTATION THIRD PARTY

# IMPORTATION INTERNAL


def validate_number(input_value: int | float) -> bool:
    try:
        value = int(input_value)
        return True
    except ValueError:
        try:
            value = float(input_value)
            return True
        except ValueError:
            return False
