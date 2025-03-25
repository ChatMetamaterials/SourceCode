from source_server_interface import *

file_name = "irrational_architectural_data.txt"
metadata_extended = extract_data_txt("Example_universal_metamaterial.txt")
Type = "irrational"
architectures = extended_architecture_data_algorithms(metadata_extended, Type)
write_json_to_txt(architectures, file_name)