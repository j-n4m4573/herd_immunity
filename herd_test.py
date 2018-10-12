import pytest
import simulation




def test_create_pop() :

    pop_size = 1000
    vacc_percentage = .25
    virus_name = "Ebola"
    mortality_rate = 0.5
    basic_repro_num = 1
    initial_infected = 1


    sim = simulation.Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)


    population = sim._create_population(initial_infected)

    assert len(population) == pop_size
    vaccinated_people = 0
    for person in population:
            if person.is_vaccinated:
                vaccinated_people += 1
    assert vaccinated_people / len(population) == vacc_percentage
