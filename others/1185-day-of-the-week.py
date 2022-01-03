class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        days = 0
        # year
        days += 365 * (year - 1971) + (year - 1969) // 4
        # month
        days += sum(monthDays[:month-1])
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month >= 3:
            days += 1

        # day
        days += day

        return week[(days + 3) % 7]
