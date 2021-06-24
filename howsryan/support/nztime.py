from datetime import datetime, timezone, timedelta
import platform


class FormatTimeByUTC:
    def __init__(self, int):
        self.offset = int
        self.utc_offset = timedelta(hours=self.offset)
        self.time_zone = timezone(self.utc_offset)
        self.current_time = datetime.now(self.time_zone)
        self.date = self.get_current_date()
        self.time = self.current_time.strftime("%#I:%M%p")

    def get_current_date(self):
        current_platform = platform.system()
        string_format_char = ""
        if current_platform == "Linux":
            string_format_char = "-"
        else:
            string_format_char = "#"
        day = int(self.current_time.strftime(f"%{string_format_char}d"))
        ordinal_suffix = self.get_ordinal_date_suffix(day)
        formatted_date = self.current_time.strftime(f"%A %B %{string_format_char}d" + ordinal_suffix)
        return formatted_date

    def get_ordinal_date_suffix(self, day):
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
            return suffix
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
            return suffix
