from pathlib import Path
import time


class Screenshots:
    def __init__(self, driver, base_folder="reports/screenshots"):
        self.driver = driver
        self.base = Path(base_folder)
        self.base.mkdir(parents=True, exist_ok=True)

    def take(self, name_prefix="screenshot"):
        ts = int(time.time())
        path = self.base / f"{name_prefix}_{ts}.png"
        self.driver.save_screenshot(str(path))
        return str(path)
