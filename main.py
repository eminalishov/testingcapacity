from CalendarByDate import CalendarByDate
import pandas as pd

url = "https://testovani.uzis.cz/Detail?id=42c85d23-21e4-4fe9-baef-9ab06c0cbe6d&backURL=/"
obj = CalendarByDate(url)
info = obj.get_info()
print('Clinic information:')
tbl1 = pd.DataFrame(info.items(), columns=['Name', 'Value'])
print(tbl1)
calendar = obj.get_calendar()
print('Clinic calendar:')
tbl2 = pd.DataFrame(calendar.items(), columns=['Date', 'Capacity'])
print(tbl2)
