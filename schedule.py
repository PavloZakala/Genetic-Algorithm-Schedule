import random
import copy

from utils import write_file_pickle, read_file_pickle
from schedule_config import ScheduleConfig

class Schedule:
    
    INIT_SIZE = 500

    def __init__(self, config: ScheduleConfig):
        
        self._config = config

        def_type = self._config.subject_types[0]
        def_sub = config.subjects_dict[def_type][0][0]

        default_tulpe = [
            def_type[0], 
            def_sub,
            config.teachers_dict[def_sub][0],
            config.rooms_idxs[0],
        ]

        self.table = {}
        
        for name in self._config.groups_names:
            self.table[name] = [[default_tulpe for l in self._config.lessons] for k in self._config.days]
        
        self.score = -1000.0

    def __get_item(self):        
        sub_type = random.choice(self._config.subject_types)
        subject = random.choice(self._config.subjects_dict[sub_type])[0]

        teacher = random.choice(self._config.teachers_dict[subject])
        room = random.choice(self._config.rooms_idxs)

        if sub_type[0] == "P":
            teacher2 = random.choice(self._config.teachers_dict[subject])
            room2 = random.choice(self._config.rooms_idxs)
            return [sub_type[0], subject, teacher, room, teacher2, room2]

        return [sub_type[0], subject, teacher, room]

    def init_schedule(self):
        
        for _ in range(self.INIT_SIZE):
            group = random.choice(self._config.groups_names)
            day_idx = random.randint(0, len(self._config.days)-1)
            lesson = random.choice(self._config.lessons)
            
            item = self.__get_item()

            self.table[group][day_idx][lesson - 1] = item   
    
    def evaluate(self):

        score = 0.0
        room_use = [[[] for l in self._config.lessons] for d in self._config.days]
        teacher_use = [[[] for l in self._config.lessons] for d in self._config.days]

        room_score = 0
        teacher_score = 0
        room_count = 0
        for group_name, group_schedule in self.table.items():

            part = self._config.p.copy()

            for x, day in enumerate(group_schedule):
                for y, item in enumerate(day):
                    if item[0] == 'L':
                        teach_idxs = [2]  
                        room_idxs = [3]
                    else:
                        teach_idxs = [2, 4]                        
                        room_idxs = [3, 5]

                    for r_id in room_idxs:
                        if item[r_id] in room_use[x][y]:
                            room_score += 1
                        else:
                            room_use[x][y].append(item[r_id])

                    for t_id in teach_idxs:
                        if item[t_id] in teacher_use[x][y]:
                            teacher_score += 1
                        else:
                            teacher_use[x][y].append(item[t_id])

                    
                    part[item[0]+item[1]] -= 2

                    if item[0] == 'L':
                        if self._config.rooms[item[3]] < self._config.groups[group_name]:
                            room_count += 1
                    else:
                        if self._config.rooms[item[3]] < self._config.groups[group_name] // 2:
                            room_count += 1
                        if self._config.rooms[item[5]] < self._config.groups[group_name] // 2:
                            room_count += 1

            sc = 1 - sum([abs(v) for v in part.values()]) / self._config.total_hours            

            score += sc

        self.score = score / (len(self._config.groups_names)) - (room_score + room_count + teacher_score)
    
        return self.score

    def mutation(self, mutation_size=2):

        for _ in range(mutation_size):

            group = random.choice(self._config.groups_names)
            day_idx = random.randint(0, len(self._config.days)-1)
            lesson = random.choice(self._config.lessons)        
            current_day = self.table[group][day_idx]

            new_item = self.__get_item()

            if current_day[lesson-1][0] == "L":
                idx = random.randint(1, 2)
                if idx == 1:
                    if new_item[0] == "L":
                        current_day[lesson-1][1] = new_item[1]                    
                    else:                                       
                        current_day[lesson-1][0] = new_item[0]
                        current_day[lesson-1][1] = new_item[1]
                        current_day[lesson-1][2] = new_item[2]
                        current_day[lesson-1].append(new_item[4])
                        current_day[lesson-1].append(new_item[5])
                else:
                    current_day[lesson-1][3] = new_item[3]
            else:
                idx = random.randint(1, 3)
                if idx == 1:
                    if new_item[0] == "P":
                        current_day[lesson-1][1] = new_item[1]
                        current_day[lesson-1][2] = new_item[2]
                        current_day[lesson-1][4] = new_item[4]
                        current_day[lesson-1][5] = new_item[5]
                    else:
                        current_day[lesson-1][0] = new_item[0]
                        current_day[lesson-1][1] = new_item[1]                    
                        current_day[lesson-1][2] = new_item[2] 
                        current_day[lesson-1].pop()
                        current_day[lesson-1].pop()
                elif idx == 2:
                    current_day[lesson-1][3] = new_item[3]
                else:
                    current_day[lesson-1][5] = new_item[3]

    def copy(self):
        copy_schedule = Schedule(self._config)
        copy_schedule.table = copy.deepcopy(self.table)
        return copy_schedule

    def save_result(self, path):
        
        write_file_pickle(self.table, path)
    
    def load_table(self, path):

        self.table = read_file_pickle(path)
    
    def print_to_file(self, name):
        out_string = ""
        for group_name in self.table:
            current_table = self.table[group_name]

            out_string += "----------- {} -----------\n".format(group_name)
            
            row_line = "{:6}|"
            for _ in self._config.days:
                row_line += "{:20}|"
        
            day_line = row_line.format("", *self._config.days)
            max_len = len(day_line)
            out_string += "-" * max_len + '\n'
            out_string += day_line + "\n"
            out_string += "-" * max_len + '\n'

            for lesson_num in self._config.lessons:
                time = list(self._config.lessons_dict[lesson_num]) + [""] * 4
                                
                for i in range(6):
                    row_param = [time[i]]
                    for idx, _ in enumerate(self._config.days):
                        if len(current_table[idx][lesson_num-1]) <= i:
                            row_param.append("")
                            continue                  
                        
                        p = current_table[idx][lesson_num-1][i]                                                
                        if i == 3 or i == 5:
                            p = "room: {}".format(p)

                        row_param.append(p)
                    out_string += row_line.format(*row_param) + '\n'

                out_string += "-" * max_len + '\n'
        
        print(out_string)    
        with open(name, 'w+', encoding='utf-8') as f:
            f.write(out_string)