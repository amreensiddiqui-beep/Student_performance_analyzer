# Student Performance Analyzer

## Project Overview
Student Performance Analyzer is a Python-based project that analyzes student marks across three subjects: Maths, Physics, and Chemistry. It calculates total marks, percentages, grades, and class statistics using Python libraries and presents the results through data visualizations.

## Features
- Reads student records from a CSV file using Pandas.
- Validates marks and skips invalid student records.
- Calculates total marks and percentages.
- Assigns grades based on percentage.
- Calculates mean, median, and standard deviation.
- Identifies the class topper.
- Calculates subject-wise average marks.
- Displays a bar chart and histogram using Matplotlib.
- Provides an interactive console-based menu.

## Technologies Used
- **Language:** Python 3
- **Pandas:** Data loading and data analysis.
- **NumPy:** Statistical calculations.
- **Matplotlib:** Data visualization.

## Grading Criteria

| Percentage | Grade |
|---|---|
| 90 and above | A |
| 75–89 | B |
| 60–74 | C |
| 40–59 | D |
| Below 40 | F |

## Project Structure
```text
Student-Performance-Analyzer/
│
├── student_analyzer.py
├── students.csv
└── README.md
```

## Installation

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib
```

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Make sure `students.csv` and `student_analyzer.py` are in the same folder.
4. Run the following command:

```bash
python student_analyzer.py
```

## Dataset Format

The CSV file contains student names and marks in three subjects.

Example:

```csv
Aman,80,70,90
Riya,60,65,70
Karan,40,35,50
```

**Maximum Marks:** 100 per subject  
**Total Maximum Marks:** 300

## Output

The project provides:

1. Student-wise results (Total, Percentage, Grade).
2. Class statistics (Mean, Median, Standard Deviation).
3. Topper details.
4. Subject-wise average marks.
5. Bar chart showing subject-wise average marks.
6. Histogram showing the distribution of student percentages.

## Concepts Covered
- Python Functions
- Conditional Statements
- Loops
- Exception Handling
- Pandas DataFrames
- NumPy Statistical Functions
- Data Visualization
- CSV File Handling

## Author
**Amreen Siddiqui**

BCA (Artificial Intelligence & Machine Learning)

## Conclusion
This project demonstrates
