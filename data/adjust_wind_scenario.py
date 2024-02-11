import csv

def delete_rows_and_columns(input_file, output_file, rows_to_delete, columns_to_delete):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        data = list(reader)
        
        # Delete rows
        for row_index in sorted(rows_to_delete, reverse=True):
            del data[row_index]
        
        # Delete columns
        for row in data:
            for column_index in sorted(columns_to_delete, reverse=True):
                del row[column_index]
        
        writer.writerows(data)

# Example usage
input_file = 'wind_scenario_windgenerator1.csv'
output_file = 'wind_scenario_windgeneratorfinal.csv'
rows_to_delete = [26, 44]  # Example rows to delete
columns_to_delete = [8, 101]  # Example columns to delete

delete_rows_and_columns(input_file, output_file, rows_to_delete, columns_to_delete)