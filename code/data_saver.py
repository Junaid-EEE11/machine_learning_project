# data_saver.py
import csv

def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Product Name', 'Price', 'Description'])  # Add headers based on your data structure

        for product_data in data:
            if product_data:
                writer.writerow([product_data['name'], product_data['price'], product_data['description']])
