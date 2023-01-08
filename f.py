from bs4 import BeautifulSoup
import requests
import pandas as pd
import html

url_part='https://merolagani.com/CompanyDetail.aspx?symbol='
#sectors
c_bank=['kbl','cbl',]
microfinance=['cbbl','mlbsl']

#looping through sectors(list), and merging with url_part and assging it with urls(list) which is used afterwards for scrapping.
urls=[]
for i in range(len(c_bank)):
	urls.append(url_part+c_bank[i])

for i in range(len(microfinance)):
	urls.append(url_part+microfinance[i])

#loop and getting request and making soup and getting company_name and table of the content
for url in urls:
	response=requests.get(url).content
	soup=BeautifulSoup(response,'lxml')

	cname=soup.find('span', id='ctl00_ContentPlaceHolder1_CompanyDetail1_companyName').text
	table=soup.find('table', class_='table table-striped table-hover table-zeromargin', id='accordion')
	#this will remove spaces 
	'''rt=table.replace(' ','')'''
	df=pd.read_html(str(table))[0]
	df.to_csv('table.csv', index=True)
	# used for the removal of the unnecessary lines
'''	clean_rt = ''
	for line in rt.split("\n"):
	    if line.strip():
	        clean_rt += line + "\n"'''
	
'''	print(cname,clean_rt)'''
	