
def check_temperature(temp_str):
    try:
        numero = int(temp_str)
        return (numero)
    except ValueError:
        print(f"{temp_str} is not a valid number")
  