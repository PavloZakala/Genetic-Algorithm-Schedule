# Genetic-Algorithm-Schedule
Genetic Algorithm Schedule

Apdate config:
```
python make_config.py 
```

Train:
```
python train.py --out_path=saves\\best1.pkl --epoch=1000
```

Test and show:
```
python show_results.py --path=saves\\best.pkl
```
Output example:
```
Score:0.96
----------- K1 -----------
----------------------------------------------------------------------------------------------------------------
      |Monday              |Tuesday             |Wednesday           |Thursday            |Friday              |
----------------------------------------------------------------------------------------------------------------
8:40  |P                   |L                   |P                   |L                   |L                   |
10:15 |Matan               |NONE                |Сulture             |Matan               |Discrete            |
      |Molodtsov A.I.      |NONE0               |Kurembek M.L.       |Alexandrovich I.N.  |Shevchenko V.P.     |
      |room: 11            |room: 8             |room: 3             |room: 11            |room: 11            |
      |Rublev B.V.         |                    |Tetera P.K.         |                    |                    |
      |room: 7             |                    |room: 11            |                    |                    |
----------------------------------------------------------------------------------------------------------------
10:35 |L                   |L                   |L                   |L                   |L                   |
12:10 |NONE                |Programing          |NONE                |NONE                |Discrete            |
      |NONE1               |Vasulev B.V.        |NONE0               |Fedorus A.          |Shevchenko V.P.     |
      |room: 8             |room: 10            |room: 8             |room: 12            |room: 13            |
      |                    |                    |                    |                    |                    |
      |                    |                    |                    |                    |                    |
----------------------------------------------------------------------------------------------------------------
12:20 |P                   |L                   |P                   |L                   |L                   |
13:55 |Discrete            |NONE                |DO                  |NONE                |NONE                |
      |Linder Y.N.         |NONE0               |Polotsky S.V.       |Polotsky S.V.       |NONE1               |
      |room: 5             |room: 9             |room: 4             |room: 9             |room: 12            |
      |Shevchenko V.P.     |                    |Matsak I.K.         |                    |                    |
      |room: 11            |                    |room: 3             |                    |                    |
----------------------------------------------------------------------------------------------------------------
14:00 |P                   |L                   |L                   |L                   |P                   |
15:35 |Programing          |NONE                |DO                  |NONE                |English             |
      |Vasulev B.V.        |NONE1               |Polotsky S.V.       |NONE0               |Mrs Simson          |
      |room: 12            |room: 11            |room: 10            |room: 13            |room: 14            |
      |Dotanov A.P         |                    |                    |                    |Mrs Jonson          |
      |room: 10            |                    |                    |                    |room: 1             |
----------------------------------------------------------------------------------------------------------------
15:40 |L                   |L                   |L                   |L                   |L                   |
17:10 |NONE                |NONE                |Сulture             |Matan               |Programing          |
      |Fedorus A.          |NONE1               |Tetera P.K.         |Vasulev B.V.        |Dotanov A.P         |
      |room: 12            |room: 10            |room: 9             |room: 8             |room: 11            |
      |                    |                    |                    |                    |                    |
      |                    |                    |                    |                    |                    |
----------------------------------------------------------------------------------------------------------------
----------- K2 -----------
----------------------------------------------------------------------------------------------------------------
      |Monday              |Tuesday             |Wednesday           |Thursday            |Friday              |
----------------------------------------------------------------------------------------------------------------
8:40  |L                   |L                   |L                   |L                   |L                   |
10:15 |NONE                |Matan               |Programing          |DO                  |NONE                |
      |Kurembek M.L.       |Petrushenko A.M.    |Dotanov A.P         |Matsak I.K.         |NONE0               |
      |room: 8             |room: 11            |room: 12            |room: 12            |room: 12            |
      |                    |                    |                    |                    |                    |
      |                    |                    |                    |                    |                    |
----------------------------------------------------------------------------------------------------------------
10:35 |P                   |P                   |L                   |P                   |L                   |
12:10 |DO                  |Discrete            |NONE                |Matan               |NONE                |
      |Matsak I.K.         |Petrushenko A.M.    |NONE1               |Rublev B.V.         |NONE0               |
      |room: 6             |room: 11            |room: 11            |room: 13            |room: 9             |
      |Yakimov R.Y.        |Linder Y.N.         |                    |Molodtsov A.I.      |                    |
      |room: 4             |room: 8             |                    |room: 5             |                    |
----------------------------------------------------------------------------------------------------------------
12:20 |L                   |P                   |P                   |L                   |L                   |
13:55 |Сulture             |Сulture             |English             |NONE                |NONE                |
      |Kurembek M.L.       |Kurembek M.L.       |Mrs Simson          |NONE1               |Molodtsov A.I.      |
      |room: 9             |room: 13            |room: 7             |room: 11            |room: 10            |
      |                    |Tetera P.K.         |Mrs Rush            |                    |                    |
      |                    |room: 4             |room: 8             |                    |                    |
----------------------------------------------------------------------------------------------------------------
14:00 |L                   |L                   |L                   |P                   |L                   |
15:35 |NONE                |NONE                |Matan               |DO                  |NONE                |
      |NONE0               |NONE0               |Alexandrovich I.N.  |Matsak I.K.         |NONE1               |
      |room: 9             |room: 12            |room: 11            |room: 14            |room: 11            |
      |                    |                    |                    |Polotsky S.V.       |                    |
      |                    |                    |                    |room: 12            |                    |
----------------------------------------------------------------------------------------------------------------
      |Vasulev B.V.        |                    |                    |                    |                    |
      |room: 10            |                    |                    |                    |                    |
----------------------------------------------------------------------------------------------------------------
```
