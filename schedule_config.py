class ScheduleConfig:

    def __init__(self, config):

        self.subjects_dict = config["Subjects"]
        
        self.rooms = {idx:size for idx, size in config["Rooms"]}
        self.rooms_idxs = list(self.rooms.keys())

        self.teachers_dict = config["Teachers"]
        self.lessons_dict = config["Lessons"]

        self.groups = {name:size for name, size in config["Groups"]}
        self.groups_names = [name for name, size in config["Groups"]]
        

        self.days = config["Days"]
        self.lessons = list(config["Lessons"].keys())

        self.subject_types = list(config["Subjects"].keys())
        
        self.teachers = []
        for list_t in config["Teachers"].values():
            self.teachers += list_t        

        self.p = {}        
        for t in self.subject_types:
            for name, h in config["Subjects"][t]:
                self.p[t[0]+name] = h

        self.total_hours = sum(self.p.values())