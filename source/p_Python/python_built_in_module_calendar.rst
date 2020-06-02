=============================
Python内置模块：calendar
=============================

日历模块calendar

.. code-block:: python

    >>> import calendar
    >>> type(calendar)
    <class 'module'>
    >>> calendar.__file__
    'C:\\Python38\\lib\\calendar.py'
    >>> dir(calendar)
    ['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
    >>>

.. code-block:: python

    import calendar

    for i in range(1, 13):
        print(calendar.month_name[i])

    import calendar

    d={}
    for i in range(1, 13):
        d[calendar.month_name[i]] = i

    print(d)

    import calendar
    from pprint import pprint
    s2 = "February January  May October August September April  November July March December"

    d = {}
    for i in range(1, 13):
        d[calendar.month_name[i]] = i
        
    def sorter(elem):
        return d[elem]

    pprint(sorted(s2.split(), key=sorter))

    import calendar
    month_names = [calendar.month_name[i] for i in range(1, 13)]
    print(month_names)
    print(sorted(s2.split(), key=month_names.index))
