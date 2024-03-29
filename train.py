import argparse

from schedule_config import ScheduleConfig
from schedule import Schedule
from utils import read_file_pickle

POPULATION_SIZE = 128

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--epoch', metavar='N', default=1000, type=int, help='epoch size')
    parser.add_argument('--out_path', metavar='P', default="saves\\best1.pkl",
                        type=str, help='path to save file')
    args = parser.parse_args()

    data_config = read_file_pickle("config\\schedule_info.pkl")
    config = ScheduleConfig(data_config)
    
    population = []

    for _ in range(POPULATION_SIZE):
        s = Schedule(config)
        s.init_schedule()
        population.append(s)        

    for ep in range(args.epoch):
        for p in population:
            p.evaluate() 

        population = sorted(population, key=lambda x: x.score, reverse=True)
        
        print("epoch:{} \t best score:{}".format(ep, population[0].score))
        if population[0].score == 1.0:
            break
        new_population = []
        for i in range(4):
            for p in population[:32]:
                new_p = p.copy()
                new_p.mutation(i)
                new_population.append(new_p)
        
        population = new_population

    population[0].save_result("best.pkl")
    population[0].print_to_file("res.txt")


