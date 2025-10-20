import src.download as download
import src.create_db as create_db
import src.graph as graph
from datetime import datetime, timedelta


if input("Enter 'Y' to Get New Data from the site: ") == 'Y':
    download.download()

if input("Enter 'Y' to Update DB: ") == 'Y':
    create_db.create_db()

print("[Enter timeframe. Defaults to the last day in the DB]")
while(1):
    try:
        start = (input("Start Day (YYYY M D): "))
        start = datetime.strptime(start, "%Y %m %d")
        print("start")
    except:
        start = "2020 5 12"
        start = datetime.strptime(start, "%Y %m %d")



    try:
        end = (input("End Day (YYYY M D): "))
        print("\n")
        end = datetime.strptime(end, "%Y %m %d")
    except:
        end = "2020 5 13"
        end = datetime.strptime(end, "%Y %m %d")

    graph.create_line_graph(start, end)

    to_end = input("Press 'Enter' to Continue, Else to End: ")
    if(to_end != ''):
        break

    