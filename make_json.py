import pickle

if __name__ == "__main__":
    d = {
        "Subjects":{
            "Lecture": [
                ("Matan", 4),
                ("Programing", 4),
                ("Discrete", 4),
                ("DO", 2),
                ("Сulture", 2),
                ("NONE", 22)
                ], 
            "Practice": [
                ("Matan", 2),
                ("Programing", 2),
                ("Discrete", 2),
                ("DO", 2),
                ("Сulture", 2),
                ("English", 2),
            ],
        },
        "Rooms":[
            (1, 15), 
            (2, 20),
            (3, 20),
            (4, 18),
            (5, 16),
            (6, 17),
            (7, 18),
            (8, 40),
            (9, 40),
            (10, 40),
            (11, 40),
            (12, 40),
            (13, 40),
            (14, 18),
            ],
        "Teachers":{
            "Matan": ["Molodtsov A.I.", "Rublev B.V.", "Alexandrovich I.N."],
            "Programing": ["Vasulev B.V.", "Dotanov A.P", "Fedorus A."],
            "Discrete": ["Shevchenko V.P.", "Petrushenko A.M.", "Linder Y.N."],
            "DO": ["Matsak I.K.", "Yakimov R.Y.", "Polotsky S.V."],
            "English": ["Mrs Simson", "Mrs Jonson", "Mrs Rush"],
            "Сulture": ["Kurembek M.L.", "Tetera P.K."],
            "NONE": ["NONE{}".format(i) for i in range(2)]

        },
        "Groups":[
            ("K1", 30),
            ("K2", 29),
            # ("K3", 28),
            # ("K4", 31),
        ],
        "Days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "Lessons": {
            1: ("8:40", "10:15"),
            2: ("10:35", "12:10"),
            3: ("12:20", "13:55"),
            4: ("14:00", "15:35"),
            5: ("15:40", "17:10"),
        }
    }

    with open("schedule_info.pkl", "wb") as f:
        pickle.dump(d, f)
    
