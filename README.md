# Git Graphs

We have need to have a look at who's working on what and at what time. These scripts
use the pylab setup of iPython to use matplotlib & numpy to take git log data and
draw charts of it.

For example, a chart of commit counts by day for devs:
    
![](https://github.com/jaymzcd/GitGraphs/raw/master/example.png) 
    
## Typical usage
    
    %run gitgraph.py
    raw_log = !git log --all --format="%ci %an"
    counts, names = user_list(raw_log)
    charts = draw_charts(counts, names)
    legend()

