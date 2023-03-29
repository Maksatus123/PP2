import json

# temp_file = json.dumps(sample-data.json)
with open('sample_data.json') as file:
    data = json.load(file)

temp_file = json.dumps('sample_data.json')

print("Interface status")
print("=" * 80)
print("DN", " " * 40, "Description ", "speed", " " * 10, "MTU")
print("-" * 41, "-" * 12, "-" * 13, "\t", "-" * 4)
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t", "\t"  , imdata[i][j]["speed"] ,"\t" , imdata[i][j]["mtu"])