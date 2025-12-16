# Grade Thresholds Estimator

This script estimates expected mean, standard deviation, and grade thresholds for a subject as defined by relative grading practices at MIT Manipal and MIT Bengaluru. Requires real score and grade data (more data generally results in tighter estimates).

# Dependencies

Python  
https://www.python.org/downloads/

Run `pip install -r requirements.txt`

# Usage
Clone the repo:  
`git clone https://github.com/aditya-mathpal/grade-thresholds-estimator.git`

In the same directory as `code.py`, create a text file `data.txt` and add \<grade\> \<score\> pairs per line like so:  
<img width="63" height="230" alt="Image" src="https://github.com/user-attachments/assets/2b599f8b-b53a-420a-89c9-ea6fe9662dc9" />  
(real data for HUM 3022 Essentials of Management, Dec 2025)

Run the code  
`python code.py`

# Sample output
Terminal:  
```
Expected mean:  64.66
Expected std dev:  10.62
Expected thresholds:  {'A+': 86, 'A': 77, 'B': 67, 'C': 58, 'D': 48, 'E': 39}
```
Plot:  
<img width="579" height="454" alt="Image" src="https://github.com/user-attachments/assets/fab8b6af-6f66-4ff8-a84a-279c349824d6" />  




