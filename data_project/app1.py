import csv

with open("events.csv","r") as fp:
    csv_data = csv.DictReader(fp)
    print(csv_data.fieldnames)
    # for row in csv_data.items():
    #     print(row.event_id,row.city)
    for row in csv_data:
        # print(csv_data['event_id'],csv_data['city'])
        print(row['event_id'],row['city'])
