from scipy.interpolate import lagrange
from numpy import array
from random import randint


def generate_shadows(
    secret: int, minimum_shadows_count: int, total_shadows_count: int, prime: int
) -> list[tuple[int, int]]:
    if minimum_shadows_count > total_shadows_count:
        raise Exception
    polynomial = [secret] + [
        randint(0, prime - 1) for _ in range(minimum_shadows_count - 1)
    ]
    x_coordinates = range(1, total_shadows_count + 1)
    y_coordinates = [evaluate_polynomial(polynomial, x, prime) for x in x_coordinates]
    points = [(x_coordinates[i], y_coordinates[i]) for i in range(total_shadows_count)]
    return points


def evaluate_polynomial(polynomial: list[int], x, prime) -> int:
    value = 0
    polynomial.reverse()
    for i in range(len(polynomial)):
        coefficient = polynomial[i]
        value += coefficient * pow(x, i)
        value %= prime
    return value


assert evaluate_polynomial(polynomial=[5, 9, 13], x=1, prime=17) == 10
assert evaluate_polynomial(polynomial=[5, 9, 13], x=2, prime=17) == 0
assert evaluate_polynomial(polynomial=[5, 9, 13], x=5, prime=17) == 13


def recover_secrets_from(points: list[tuple[int, int]]) -> int:
    x_coordinates = [points[i][0] for i in range(len(points))]
    y_coordinates = [points[i][1] for i in range(len(points))]
    polynomial = lagrange(array(x_coordinates), array(y_coordinates))
    return polynomial(0)


def secret_should_be_shared_and_recovered():
    # GIVEN
    secret = 13
    prime = 17
    minimum_shadows_count = 3
    total_shadows_count = 5

    # WHEN
    all_shadows = generate_shadows(
        secret, minimum_shadows_count, total_shadows_count, prime
    )
    shadows_used_for_recovery = all_shadows[:minimum_shadows_count]

    # THEN
    recovered_secret = recover_secrets_from(shadows_used_for_recovery)
    assert recovered_secret == secret


secret_should_be_shared_and_recovered()
