import argparse

from schedule_config import ScheduleConfig
from schedule import Schedule
from utils import read_file_pickle

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--path', metavar='P', default="saves\\best.pkl",
                        type=str, help='path to save file')
    args = parser.parse_args()

    data_config = read_file_pickle("config\\schedule_info.pkl")
    config = ScheduleConfig(data_config)

    s = Schedule(config)
    s.init_schedule()
    s.load_table(args.path)
    s.evaluate() 
    
    print("Score:{}".format(s.score))

    s.print_to_file("res.txt")
    
    