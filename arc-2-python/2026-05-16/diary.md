# 📅 Study Diary - May 16, 2026

### 🛠️ Technical Progress & Refactoring
* **Exercise 016 (Math.trunc):** Refactored the initial code from a broad `import math` to a precise **Named Import** (`from math import trunc`). This optimizes memory usage, keeps the global namespace tidy, and targets only the required behavior.
* **Exercise 017 (Hypotenuse):** Implemented two distinct approaches: the manual Pythagorean theorem ($a^2 + b^2 = c^2$) and the automated `math.hypot()` method. **Key milestone:** Independently engineered a geometric validation check (`if opS <= 0 or adjS <= 0`) to prevent unrealistic inputs and runtime logic flaws.
* **Exercise 018 (Trigonometry):** Mastered function nesting within f-strings. Successfully managed data conversion by transforming input degrees to radians (`radians(angle)`) dynamically before feeding them into the `sin()`, `cos()`, and `tan()` operations.
* **Exercises 019 & 020 (Random Pick & Shuffle):** Anticipated advanced control structures by implementing **`for` loops** and dynamic array population via `.append()` ahead of the standard curriculum. Handled list mutability (`in-place` modification) successfully with `shuffle()`.
* **Exercise 021 (Audio Player):** Developed a script to play an MP3 audio file (`music.mp3`) through Python, completing the core block of automation and external media challenges.

### 🛡️ Troubleshooting & System Engineering (The Core Challenge)
* **Environment Conflicts (Python 3.14):** Faced compilation blockages (`subprocess-exited-with-error`) while trying to install legacy external packages like `pygame` and `playsound`. Discovered that the cutting-edge Python 3.14 environment lacked obsolete dependencies required to build their wheels from scratch.
* **Environment Workaround:** Shifted from external packages to native modules (`import os`), avoiding third-party dependency resolution failures entirely.