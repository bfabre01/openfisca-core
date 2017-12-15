# -*- coding: utf-8 -*-

import numpy as np
from nose.tools import assert_equal

from openfisca_country_template.situation_examples import couple
from openfisca_core.simulations import Simulation
from openfisca_core.periods import period as make_period
from test_countries import tax_benefit_system

period = make_period('2017-12')
HousingOccupancyStatus = tax_benefit_system.get_variable('housing_occupancy_status').possible_values


def test_set_input_enum_string():
    simulation = Simulation(tax_benefit_system = tax_benefit_system, simulation_json = couple)
    status_occupancy = np.asarray(['free_lodger'])
    simulation.household.get_holder('housing_occupancy_status').set_input(period, status_occupancy)
    result = simulation.calculate('housing_occupancy_status', period)
    assert_equal(result, HousingOccupancyStatus.free_lodger)


def test_set_input_enum_int():
    simulation = Simulation(tax_benefit_system = tax_benefit_system, simulation_json = couple)
    status_occupancy = np.asarray([2], dtype = np.int16)
    simulation.household.get_holder('housing_occupancy_status').set_input(period, status_occupancy)
    result = simulation.calculate('housing_occupancy_status', period)
    assert_equal(result, HousingOccupancyStatus.free_lodger)


def test_set_input_enum_item():
    simulation = Simulation(tax_benefit_system = tax_benefit_system, simulation_json = couple)
    status_occupancy = np.asarray([HousingOccupancyStatus.free_lodger])
    simulation.household.get_holder('housing_occupancy_status').set_input(period, status_occupancy)
    result = simulation.calculate('housing_occupancy_status', period)
    assert_equal(result, HousingOccupancyStatus.free_lodger)
