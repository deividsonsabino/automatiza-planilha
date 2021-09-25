import openpyxl

book = openpyxl.load_workbook('Planilha de Compras.xlsx')

frutas_page = book['Frutas']

for rows in frutas_page.iter_rows(min_row=2,max_row=3):
	for cell in rows:
		print(cell.value)

