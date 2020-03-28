from schedule_config import ScheduleConfig
from schedule import Schedule
from utils import read_file_pickle

if __name__ == "__main__":
    data_config = read_file_pickle("schedule_info.pkl")
    config = ScheduleConfig(data_config)

    s = Schedule(config)
    s.init_schedule()

    s.print_to_file("res.txt")