from datetime import datetime, timezone, timedelta


class FormatTimeByUTC:
    def __init__(self, int):
        self.offset = int
        self.utc_offset = timedelta(hours=self.offset)
        self.time_zone = timezone(self.utc_offset)
        self.current_time = datetime.now(self.time_zone)
        self.date = self.get_current_date()
        self.time = self.current_time.strftime("%#I:%M%p")

    def get_current_date(self):
        day = int(self.current_time.strftime("%#d"))
        ordinal_suffix = self.get_ordinal_date_suffix(day)
        formatted_date = self.current_time.strftime("%A %B %#d" + ordinal_suffix)
        return formatted_date

    def get_ordinal_date_suffix(self, day):
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
            return suffix
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
            return suffix
