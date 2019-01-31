import csv
import urllib.request

import os.path
def get_file(url,tp):
    head, filename = os.path.split(url)
    base, extension = os.path.splitext(filename)
    urllib.request.urlretrieve(url, "data/%s_%s%s" %(base,tp,extension))

with open('export.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print("File %s" % row["order"])
        get_file(row["media"],"mask")
        get_file(row["satellite_view_zoom"],"image")
