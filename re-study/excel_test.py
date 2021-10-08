import openpyxl

workbook = openpyxl.load_workbook(r"D:\new-study\data\test_case.xlsx")
sheet = workbook["register"]
result = sheet.rows
data_result = list(result)

title = []
for i in data_result[0]:
    title.append(i.value)
print(title)

case_data = []

for i in data_result[1:]:
    data = []
    for j in i:
        data.append(j.value)
        print(data)
    case_data.append(dict(zip(title, data)))
print(case_data)
