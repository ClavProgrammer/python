import pandas

table = pandas.read_csv("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/adopce-zvirat.csv?fbclid=IwAR06sHy5J07Os7NCiMLmma2G8q9I6m3Z18Z9nn9XjmXg0E0tre_BkCfNQEU", sep=";")

#Add how much rows, columns and their names

print(f"Rows: {len(table)}") 
print(f"{table.info()}")

table_names = table[["nazev_cz", "nazev_en"]]
print(table_names.iloc[[34]])

