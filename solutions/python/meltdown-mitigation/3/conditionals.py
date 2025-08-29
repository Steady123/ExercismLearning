"""Functions to prevent a nuclear meltdown."""

critical_temp_k = 800
critical_neutrons_1ps = 500
critical_product_temp_neutrons = 500000


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    product_temp_neutrons = temperature * neutrons_emitted
        
    if temperature < critical_temp_k and neutrons_emitted > critical_neutrons_1ps and product_temp_neutrons < critical_product_temp_neutrons:
        result_is_criticality_balanced = True
    else:
        result_is_criticality_balanced = False

    return result_is_criticality_balanced

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    percentage_reactor_eficiency = int((generated_power / theoretical_max_power) * 100)

    if percentage_reactor_eficiency >= 80:
        efficiency = 'green'
    elif percentage_reactor_eficiency >= 60:
        efficiency = 'orange'
    elif percentage_reactor_eficiency >= 30:
        efficiency = 'red'
    else: 
        efficiency = 'black'

    return efficiency


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    reactor_threshold = temperature * neutrons_produced_per_second

    low_threshold = threshold * 0.9
    normal_threshold = threshold * 1.1
    
    if reactor_threshold < low_threshold:
        status_code = 'LOW'
    elif reactor_threshold < normal_threshold:
        status_code = 'NORMAL'
    else:
        status_code = 'DANGER'
    
    return status_code
