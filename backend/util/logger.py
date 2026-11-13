from datetime import datetime
from pathlib import Path
LOG_PATH=Path(__file__).resolve().parents[2] / "activity_log.txt"
def log_activity(message, user_id=None):
    stamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"[{stamp}] user={user_id or 'system'} | {message}\n")
