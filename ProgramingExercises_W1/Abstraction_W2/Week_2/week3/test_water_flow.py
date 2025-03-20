import pytest
from water_flow import pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, kPa_to_psi


# Test for pressure loss from fittings
def test_pressure_loss_from_fittings():
    assert abs(pressure_loss_from_fittings(0.00, 3) - 0.000) < 0.001
    assert abs(pressure_loss_from_fittings(1.65, 0) - 0.000) < 0.001
    assert abs(pressure_loss_from_fittings(1.65, 2) - -0.109) < 0.001
    assert abs(pressure_loss_from_fittings(1.75, 2) - -0.122) < 0.001
    assert abs(pressure_loss_from_fittings(1.75, 5) - -0.306) < 0.001


# Test for Reynolds number
def test_reynolds_number():
    assert abs(reynolds_number(0.048692, 0.00) - 0) < 1
    assert abs(reynolds_number(0.048692, 1.65) - 80069) < 1
    assert abs(reynolds_number(0.048692, 1.75) - 84922) < 1
    assert abs(reynolds_number(0.286870, 1.65) - 471729) < 1
    assert abs(reynolds_number(0.286870, 1.75) - 500318) < 1


def test_pressure_loss_from_pipe_reduction():
    # Test for zero values to ensure ValueError is raised
    with pytest.raises(ValueError):
        pressure_loss_from_pipe_reduction(0.28687, 0.00, 0, 1)
    
    # Test for valid values
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) - -163.744) < 0.001
    assert abs(pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) - -184.182) < 0.001


# Test for kPa to psi conversion
def test_kPa_to_psi():
    assert abs(kPa_to_psi(0.000) - 0.000) < 0.001
    assert abs(kPa_to_psi(158.7) - 23.0175) < 0.01  # Adjusted expected value


if __name__ == "__main__":
    pytest.main()
