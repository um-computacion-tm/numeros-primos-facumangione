def is_prime(value):
    divisor=value-1
    while divisor>1:
        if value%divisor==0:
            return False
        divisor=divisor-1
    return True
    