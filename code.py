import math
import numpy as np
import matplotlib.pyplot as plt

def thresholds(m, s):
    return {
        "A+": math.ceil(min(90, max(75, m + 2.0*s))),
        "A" : math.ceil(min(82, max(67, m + 1.1*s))),
        "B" : math.ceil(min(74, max(59, m + 0.2*s))),
        "C" : math.ceil(min(66, max(51, m - 0.7*s))),
        "D" : math.ceil(min(58, max(43, m - 1.6*s))),
        "E" : math.ceil(min(50, max(35, m - 2.5*s))),
    }

def read_observations(filename):
    observations = []

    with open(filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()

            # Skip empty lines or comments
            if not line or line.startswith("#"):
                continue

            try:
                grade, score = line.split()
                score = int(score)
            except ValueError:
                raise ValueError(
                    f"Invalid format on line {line_num}: '{line}'\n"
                    "Expected: <GRADE> <SCORE>"
                )

            observations.append((score, grade))

    return observations

def is_consistent(m, s, observations):
    T = thresholds(m, s)

    for score, grade in observations:
        if score < T[grade]:
            return False
        if grade != 'A+':
            if score >= T[next_grade[grade]]:
                return False

    return True

grade_order = ["E", "D", "C", "B", "A", "A+"]
next_grade = {g : grade_order[i+1] for i, g in enumerate(grade_order[:-1])}

observations = read_observations("data.txt")

m_values = np.linspace(40, 80, 801)
s_values = np.linspace(1, 25, 501)

feasible = []

for m in m_values:
    for s in s_values:
        if is_consistent(m, s, observations):
            feasible.append((m, s))

if not feasible:
    raise RuntimeError("No feasible (m, s) found for given observations")

ms = [p[0] for p in feasible]
ss = [p[1] for p in feasible]

m_hat = sum(ms) / len(ms)
s_hat = sum(ss) / len(ss)

print("Expected mean: ", round(m_hat, 2), "\nExpected std dev: ", round(s_hat, 2), "\nExpected thresholds: ", thresholds(m_hat, s_hat))

plt.scatter(ms, ss, s=1)
plt.xlabel("Mean (m)")
plt.ylabel("Std Dev (s)")
plt.title("Feasible (m, s) region")
plt.show()