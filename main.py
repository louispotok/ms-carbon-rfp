import pandas as pd

def main():
    df = pd.read_csv('./2021_Microsoft_Carbon_RFP_Responses.csv', header=None)
    col_names = df.iloc[:2].T.fillna(method='ffill')
    col_names.columns = ['question', 'detail']
    data = df.iloc[2:].reset_index(drop=True)

    for i, row in data.iterrows():
            write_row(i, row, col_names)

def write_row(i, row, col_names):
	proj_name = str(row[3]).lower().replace(' ','-').replace('/','-')
	filename = f"./raw/{i:03d}-{proj_name}.md"
	assert len(row) == len(col_names)
	with open(filename,'w') as f:
		for i, val in row.iteritems():
			to_write = f"""
{i:02d}. **{col_names.iloc[i]['question']} : {col_names.iloc[i]['detail']}**

     {val}
<p>&nbsp;</p>
<p>&nbsp;</p>
"""
			f.write(to_write)

if __name__ == '__main__':
	main()
