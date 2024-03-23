import json
#link download metadata_map: https://gadm.org/download_country.html
# Đọc file JSON
with open("metadata_map.json", "r", encoding="utf-8") as file:
    data = json.load(file)
# In dữ liệu đọc được từ file JSON
provices=["LaiChâu","ĐiệnBiên","SơnLa","HoàBình","LàoCai","YênBái"]
with open("coordinates.txt", "w", encoding="utf-8") as output_file:
    for i in range(len(data['features'])):
        for q in range(len(provices)):
            if data['features'][i]['properties']['NAME_1']==provices[q]:
                #output_file.write(";;"+data['features'][i]['properties']['NAME_1']+ "\n")
                #output_file.write(";;"+data['features'][i]['properties']['TYPE_2']+' '+data['features'][i]['properties']['NAME_2']+ "\n")
                coordinates = data['features'][i]['geometry']['coordinates'][0][0]
                for j in range(len(coordinates)):
                    coordinate_str = str(coordinates[j]).replace(",", "").replace("[", "").replace("]", "")
                    output_file.write('POINT '+coordinate_str + "\n")
                output_file.write("GAP"+ "\n")
