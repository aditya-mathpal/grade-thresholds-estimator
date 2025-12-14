# Grade Thresholds Estimator

This script estimates expected mean, standard deviation, and grade thresholds for a subject as defined by relative grading practices at MIT Manipal and MIT Bangalore. Requires real score and grade data (more data generally results in tighter estimates).

# Dependencies

Python  
https://www.python.org/downloads/

Run `pip install -r requirements.txt`

# Usage
Clone the repo:  
`git clone https://github.com/aditya-mathpal/grade-thresholds-estimator.git`

In the same directory as `code.py`, create a text file `data.txt` and add \<grade\> \<score\> pairs per line like so:  
<img width="69" height="164" alt="Image" src="https://github.com/user-attachments/assets/cd55831f-40c6-4be3-99c7-d516803be423" />  
(real data for HUM 3022 Essentials of Management, Dec 2025)

Run the code  
`python code.py`

# Sample output
Terminal:  
```
Expected mean:  65.01 
Expected std dev:  7.77 
Expected thresholds:  {'A+': 81, 'A': 74, 'B': 67, 'C': 60, 'D': 53, 'E': 46}
```
Plot:  
<img width="646" height="552" alt="Image" src="https://github.com/user-attachments/assets/1d45fa42-42d2-4ee8-b4ed-9fc24d7402cc" />

