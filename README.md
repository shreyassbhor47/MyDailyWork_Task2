# MydailyWork
MyDailyWork python programming internship. 
# MyDailyWork — Python Programming Internship Tasks

This folder contains working solutions for all 5 tasks from the internship
task sheet. Complete **at least 3 of the 5** to qualify for the certificate.

## One-time setup (do this first)

1. Install Python 3.8+ if you don't have it: https://www.python.org/downloads/
2. Verify it's installed by opening a terminal (Command Prompt / PowerShell on
   Windows, Terminal on Mac/Linux) and running:
   ```
   python3 --version
   ```
   (On Windows it may just be `python --version`.)
3. Put all the `.py` files in one folder.
4. Open a terminal, `cd` into that folder.

## Task 1 — To-Do List (`task1_todo_list.py`)
**Run it:**
```
python3 task1_todo_list.py
```
**How it works:** A menu-driven CLI app. Choose 1–6 to add, view, update,
complete, or delete tasks. Tasks are saved automatically to `tasks.json` in
the same folder, so your list survives closing/reopening the program.
No extra libraries needed — uses only Python's built-in `json` and `os`.

## Task 2 — Calculator (`task2_calculator.py`)
**Run it:**
```
python3 task2_calculator.py
```
**How it works:** Pick an operation (add/subtract/multiply/divide), enter two
numbers, get the result. Handles invalid input (non-numbers) and division by
zero gracefully. No extra libraries needed.

## Task 3 — Password Generator (`task3_password_generator.py`)
**Run it:**
```
python3 task3_password_generator.py
```
**How it works:** Enter a desired length, then choose (y/n) whether to
include uppercase letters, digits, and symbols. It builds a random password
from Python's `random` and `string` modules — no extra libraries needed.

## Task 4 — Weather Forecast (`task4_weather_forecast.py`)
**Extra setup required** (this one calls a real weather API):
1. Install the `requests` library:
   ```
   pip install requests
   ```
2. Sign up for a free API key at https://openweathermap.org/api
   (free tier is enough — takes a couple minutes, key may take ~10 min to activate)
3. Open `task4_weather_forecast.py` and replace `"YOUR_API_KEY_HERE"` with
   your real key — OR set it as an environment variable so you don't hardcode it:
   ```
   export OPENWEATHER_API_KEY=your_real_key_here      # Mac/Linux
   set OPENWEATHER_API_KEY=your_real_key_here          # Windows CMD
   ```
**Run it:**
```
python3 task4_weather_forecast.py
```
**How it works:** Enter a city name, it calls the OpenWeatherMap API, parses
the JSON response, and prints temperature, humidity, wind speed, and a
description in a clean format.

## Task 5 — Quiz Game (`task5_quiz_game.py`)
**Run it:**
```
python3 task5_quiz_game.py
```
**How it works:** Presents 5 multiple-choice questions in random order,
tracks your score, gives immediate feedback (correct answer shown if you
miss), shows a final score + performance message, and asks if you want to
play again. Add your own questions by editing the `QUESTIONS` list at the
top of the file — just follow the same dictionary format.

## Recording your demo video (required for submission)
For each task, use a screen recorder (e.g. OBS Studio, or the built-in
recorder on Windows/Mac) to:
1. Show the code briefly in your editor
2. Run the script in the terminal
3. Demonstrate all the main features working
4. Upload the video to LinkedIn, tag **@mydailywork**, and add hashtags
   `#mydailywork #pythonprogramming`

## Submitting to GitHub
1. Create a GitHub repo named **MYDAILYWORK**
2. Create a folder per task (e.g. `Task1_ToDoList`, `Task2_Calculator`, etc.)
3. Push each `.py` file into its folder along with a short `README.md`
   describing what it does
4. Copy your repo URL — you'll paste it into the task submission form once
   MyDailyWork emails it to you
