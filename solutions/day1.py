""" day1.py - solutions to day 1 puzzles of AoC19 """

input = [
126317,
64620,
139485,
77772,
104110,
103781,
62566,
76265,
122125,
54244,
113039,
142451,
118677,
54302,
143001,
81938,
110142,
115486,
128100,
81258,
126461,
81557,
147850,
138259,
73839,
96284,
149078,
59289,
125691,
102718,
142591,
110725,
56164,
76729,
133956,
140321,
57104,
125483,
115962,
52370,
74447,
121430,
96347,
116793,
76514,
60089,
113431,
66670,
120534,
117547,
113552,
131513,
118405,
85212,
57049,
118644,
54743,
95142,
58559,
85522,
73832,
141441,
97836,
98818,
104272,
100048,
99266,
97766,
115778,
51066,
132499,
129931,
119368,
91101,
139165,
106488,
105597,
66166,
117561,
94670,
123877,
63389,
70293,
79754,
105288,
128328,
130873,
54200,
120704,
57043,
71478,
133049,
102096,
82797,
62972,
121906,
77277,
97183,
112739,
135590,
]

def calculate_fuel_requirement(mass):
    return ((mass // 3) - 2)

def day_one_part_one():
    return sum(map(calculate_fuel_requirement, input))

def calculate_fuel_requirement_recursive(mass):
    if mass <= 8:
        return 0
    else:
        fuel_required = calculate_fuel_requirement(mass)
        return fuel_required + calculate_fuel_requirement_recursive(fuel_required)

def day_one_part_two():
    return sum(map(calculate_fuel_requirement_recursive, input))
