from sys import float_info, argv


def calculate_inss(salary):
    """
    Command method, in order to calculate INSS from a salary.
    """
    ranges = (
        (0, 1100, 0.075),
        (1100.01, 2203.48, 0.09),
        (2203.49, 3305.22, 0.12),
        (3305.23, 6433.57, 0.14),
    )
    inss = 0

    for inss_range in ranges:
        if salary > inss_range[0]:
            inss += (min(inss_range[1], salary) - inss_range[0]) * inss_range[2]

    return inss


def calculate_irrf(salary):
    """
    Command method, in order to calculate IRRF from a salary.
    """
    ranges = (
        (0, 1903.98, 0),
        (1903.99, 2826.65, 0.075),
        (2826.66, 3751.05, 0.15),
        (3751.06, 4664.68, 0.225),
        (4664.69, float_info.max, 0.275),
    )
    irrf = 0

    for irrf_range in ranges:
        if salary > irrf_range[0]:
            irrf += (min(irrf_range[1], salary) - irrf_range[0]) * irrf_range[2]

    return irrf


if __name__ == "__main__":
    salary_initial = float(argv[1])
    inss = calculate_inss(salary_initial)
    irrf = calculate_irrf(salary_initial)
    salary_final = salary_initial - inss - irrf
    print(f"INSS: R$ {inss}")
    print(f"IRRF: R$ {irrf}")
    print(f"Salário liquido: R${salary_final}")
