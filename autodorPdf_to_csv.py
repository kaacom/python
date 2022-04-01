import tabula

dfs = tabula.read_pdf(r"C:\Users\akubarev\Documents\cars\Автодор\OL_0422_068.pdf", pages='all')
tabula.convert_into_by_batch(r"C:\Users\akubarev\Documents\cars\Автодор", output_format='csv', pages='all',stream=True)

#test