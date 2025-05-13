import src.download as download
import src.create_db as create_db
import src.graph as graph
from datetime import datetime


if input("Enter 'Y' to Get New Data from the site: ") == 'Y':
    download.download()

if input("Enter 'Y' to Update DB: ") == 'Y':
    create_db.create_db()

start = (input("Start Day (YYYY M D): "))
start = datetime.strptime(start, "%Y %m %d")

end = (input("End Day (YYYY M D): "))
end = datetime.strptime(end, "%Y %m %d")

graph.create_line_graph(start, end)