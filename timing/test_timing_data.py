import csv


timing_data = []
with open('TestTimingData.csv') as csv_file:
  file_reader = csv.reader(csv_file)
  for row in file_reader:
    timing_data.append(row)

column_chart_data = [["Test name", "Diff from Avg"]]
table_data = [["Test name", "Run time (seconds)"]]

for row in timing_data[1:]:
  test_name = row[0]
  
  if not row[1] or not row[2]:
    continue
  current_run_time = float(row[1])
  avg_run_time = float(row[2])
  diff_from_avg = avg_run_time - current_run_time
  column_chart_data.append([test_name, diff_from_avg])
  table_data.append([test_name, current_run_time])

print(column_chart_data)
print(table_data)
