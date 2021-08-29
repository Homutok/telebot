import datetime
timeSchedule=[[datetime.datetime.strptime('8:20','%H:%M'),datetime.datetime.strptime('9:40','%H:%M')],
[datetime.datetime.strptime('9:50','%H:%M'),datetime.datetime.strptime('11:10','%H:%M')],
[datetime.datetime.strptime('11:40','%H:%M'),datetime.datetime.strptime('13:00','%H:%M')],
[datetime.datetime.strptime('13:30','%H:%M'),datetime.datetime.strptime('14:50','%H:%M')],
[datetime.datetime.strptime('15:00','%H:%M'),datetime.datetime.strptime('16:20','%H:%M')],
[datetime.datetime.strptime('16:40','%H:%M'),datetime.datetime.strptime('18:00','%H:%M')],
[datetime.datetime.strptime('18:10','%H:%M'),datetime.datetime.strptime('19:30','%H:%M')],
[datetime.datetime.strptime('19:40','%H:%M'),datetime.datetime.strptime('23:00','%H:%M')]
]
weekDays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
evenNotEven = 1 - datetime.datetime.now().isocalendar()[1]%2
