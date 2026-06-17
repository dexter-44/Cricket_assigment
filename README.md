# Cricket_assigment
# Fantasy Cricket Points Calculator

A modular Python application designed to evaluate and calculate performance match points for cricket players based on custom statistical rules. The system processes player data structures dynamically, splitting evaluation rules between batting and bowling performance criteria.

---

## 🚀 Features

- **Modular Design:** Points logic is completely decoupled from the main program block into its own explicit module (`player_points.py`).
- **Batting Evaluation Rules:** Calculates runs, milestone bonuses (50s/100s), boundary impacts (4s/6s), strike-rate metrics, and fielding contributions.
- **Bowling Evaluation Rules:** Processes wickets, milestone scaling (3+ or 5+ wickets), custom economy-rate categories, and fielding metrics.

---

## 📊 Rules Matrix

### Batting Points Breakdown
* **Base Runs:** `+1 point` per 2 runs scored.
* **Half-Century Bonus:** `+5 points` if runs $\ge$ 50.
* **Century Bonus:** `+10 points` if runs $\ge$ 100.
* **Boundaries:** `+1 point` per boundary (4), `+2 points` per six (6).
* **Strike Rate (SR) Multipliers:**
  * **SR 80 - 100:** `+2 points`
  * **SR > 100:** `+4 points`

### Bowling Points Breakdown
* **Base Wickets:** `+10 points` per wicket taken.
* **Haul Bonus:** `+5 points` for a 3-wicket haul; `+10 points` for a 5-wicket haul.
* **Economy Rate (ER) Impact:**
  * **ER 3.5 - 4.5:** `+4 points`
  * **ER 2.0 - 3.49:** `+7 points`
  * **ER < 2.0:** `+10 points`

> 💥 **Fielding Constants:** Any fielding action contributes a flat `+10 points` across both player roles.

---

## 💻 How to Run the Program

### Prerequisites
Make sure you have Python 3.x installed on your computer. You can check your version by running:
```bash
python --version

Execution Steps
1.Open your Terminal / Command Prompt
Windows: Press Win + R, type cmd, and press Enter.
Mac/Linux: Open your built-in Terminal application.

2.Navigate to the Directory
Move into your cloned project directory:
cd "Cricket_assigment"

3.Run the Script
Execute the driver file:
python main.py

⚙️ Sample Output Preview
When executing the sample roster configuration included inside main.py, the system outputs:

{'name': 'Virat Kohli', 'batscore': 83}
{'name': 'du Plessis', 'batscore': 94}
{'name': 'Bhuvneshwar Kumar', 'bowlscore': 20}
{'name': 'Yuzvendra Chahal', 'bowlscore': 24}
{'name': 'Kuldeep Yadav', 'bowlscore': 42}

Man of the Match: du Plessis
Points: 94
