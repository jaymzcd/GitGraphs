
def draw_charts(counts, names, uid=None):
    from pylab import bar
    from numpy import array, zeros

    cols = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan']
    data = array(counts.values())

    if uid is not None:
        col_range = range(uid, uid+1)
    else:
        col_range = range(data.shape[1])
    
    charts = list()
    for i in col_range:
        bottom = zeros(data.shape[0])
        if uid is None:
            for col in range(i):
                bottom += data[:, col]
        charts.append(bar(counts.keys(), data[: ,i], color=cols[i], bottom=bottom, label=names[i]))
        
    return charts

def user_list(raw_log, name_trim=3):
    """ Use raw_log = !git log --format="%ci %an"  within iPython to 
    load the git data into a variable to parse out with this function.
    It can then be used to draw a stacked bar chart by commits for
    the date range of the repo. """

    from datetime import datetime
    from pylab import bar
    import sys
    
    DATE_LEN = len('2011-07-13')
    USER_OFFSET = len('2011-07-14 11:44:50 +0100 ')
    
    def dt_str(date):
        return datetime.strptime(date, '%Y-%m-%d')

    names = set([x[USER_OFFSET:][:name_trim].lower() for x in raw_log])
    names = list(names)
    date_range = set([dt_str(x[:DATE_LEN]) for x in raw_log])
    
    user_commits = dict()
    for name in names:
        user_commits.update({
            name: [dt_str(x[:DATE_LEN]) for x in raw_log if name in x[USER_OFFSET:].lower()],
        })

    counts = dict()
    for date in date_range:
        user_counts = list()
        for name in names:
            user_counts.append(user_commits[name].count(date))
        counts.update({date: user_counts})

    return counts, names

