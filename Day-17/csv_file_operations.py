# READING CSV FILES IN PYTHON

import csv

with open("./modal_logs1.csv", "r") as file:
    csv_content = csv.reader(file)
    print(type(csv_content))

    header = next(csv_content)
    print(f'Header: {header}')

    # for row in csv_content:
    #     print(row[0], row[2])

    # find the day where the tokens are used max

    day_wise_tokens = {row[0]: row[2] for row in csv_content }
    print(day_wise_tokens)

    max_tokens = max(day_wise_tokens, key=day_wise_tokens.get)
    print(max_tokens)
    print(day_wise_tokens[max_tokens])

with open("./modal_logs_summary.csv", "w", newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(['Day', 'Tokens Used'])

    for day, tokens in day_wise_tokens.items():
        csv_writer.writerow([day, tokens])









