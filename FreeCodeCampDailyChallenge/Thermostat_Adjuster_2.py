def adjust_thermostat(current_f, target_c):

        f = (target_c * 1.8) + 32
        result = ""
        if f == current_f:
            result ="Hold"
        elif f > current_f:
            result = f"Heat: {round(f - current_f, 1)} degrees Fahrenheit"
        else:
            result = f"Cool: {round(current_f - f, 1)} degrees Fahrenheit"

        return result