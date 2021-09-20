from ClinicList import ClinicList
from CalendarByDate import CalendarByDate
import pandas as pd
from time import sleep
clinic = ClinicList()
for cl in clinic.data():
    url = cl['url']
    obj = CalendarByDate(url)
    info = obj.get_info()
    print("=====================================================")
    print(cl['name'])
    print("-----------------------")
    print('Clinic information:')
    tbl1 = pd.DataFrame(info.items(), columns=['Name', 'Value'])
    print(tbl1)
    calendar = obj.get_calendar()
    print('Clinic calendar:')
    tbl2 = pd.DataFrame(calendar.items(), columns=['Date', 'Capacity'])
    print(tbl2)
    sleep(1)

