# Accessing the training_database.bin:
## To load the whole database:
full_data = get_data_from_bin('training_database.bin')
print(full_data.head())

## To access a specific row (for example, row index 5):
specific_row = get_data_from_bin('training_database.bin', row=5)
print(specific_row)