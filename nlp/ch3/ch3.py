#20240409
import pandas as pd
#read from file
print('result : f1 output:')
f1 = open('example.txt','r',encoding='utf-8')
print(f1)

print(f1.read())
print(f1.read())

f1.close()

print('result : f2 output:')
f2 = open('example.txt','r',encoding='utf-8')
f2.read()
f2.close()

print('result : f3 output:')
f3 = open('example.txt','r',encoding='utf-8')
f3.readline()
f3.readline()
f3.readline()
f3.close()

print('result : f4 output:')
file4 = open('example.txt','r',encoding='utf-8')
for line in file4:
	print(line,'')
file4.close()


with open('example.txt','r',encoding='utf-8') as f5:
	text = f5.read()
	
#write method
with open('contents.txt','w',encoding='utf-8') as f6:
	f6.write('Hello write method!\n')


#read from csv file
print('result : read data from example.csv')
example_csv_file = pd.read_csv('example.csv', encoding='utf-8')
print(example_csv_file)
print(example_csv_file['grade'])

print('result : read data from example1.csv')
example_csv1_file = pd.read_csv('example1.csv', encoding='utf-8')
print(example_csv1_file)

print('result :read data from example1.csv with keyword [header=None]')
example_csv1_file_withnone = pd.read_csv('example1.csv', header=None, encoding='utf-8')
print(example_csv1_file_withnone)

#read data from tsv file use read_csv
print('result : read data from example.tsv with method read_csv')
example_tsv_file = pd.read_csv('example.tsv', encoding='utf-8', sep='\t')
print(example_tsv_file)

#read data from tsv file use read_table
print('result : read data from example.tsv with method read_table')
example_tsv_file1 = pd.read_csv('example.tsv', encoding='utf-8', sep='\t')
print(example_tsv_file1)

#read data from json file
print('result : read data from example.json with method read_json')
example_json_file = pd.read_json('example.json', encoding='utf-8')
print(example_json_file)

#read data from json file
print('result : read data from example.json with keyword [lines=True]')
example_json_file1 = pd.read_json('example.json1',lines=True, encoding='utf-8')
print(example_json_file)

#ディレクトリの走査
print('result : ls dir1')
from pathlib import Path
p = Path('dir1')
dir_list = list(p.glob('*'))
print(dir_list)

print('result : ls *.txt')
all_txtfile = list(p.glob('*.txt'))
print(all_txtfile)

print('result : ls *.txt')
all_txtfilein_dir1 = list(p.glob('**/*.txt'))
print(all_txtfilein_dir1)

#20250410
#コーパスの作成
