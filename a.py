from bs4 import BeautifulSoup
import requests

url_part='https://merolagani.com/CompanyDetail.aspx?symbol='
#sectors
c_bank=['kbl','cbl','mega','ccbl','ebl','lbl']
microfinance=['cbbl','mlbsl']
investment=[]
non_life=[]
life=[]
hydro=[]
finance=['jfl']
manu=[]
trading=[]
dev_bank=['lbbl','jbbl']
hotel=[]
others=[]



#looping through sectors(list), and merging with url_part and assging it with urls(list) which is used afterwards for scrapping.
urls=[]
for i in range(len(c_bank)):
	urls.append(url_part+c_bank[i])

for i in range(len(microfinance)):
	urls.append(url_part+microfinance[i])

for i in range(len(investment)):
	urls.append(url_part+investment[i])

for i in range(len(non_life)):
	urls.append(url_part+non_life[i])

for i in range(len(life)):
	urls.append(url_part+life[i])

for i in range(len(hydro)):
	urls.append(url_part+hydro[i])

for i in range(len(finance)):
	urls.append(url_part+finance[i])

for i in range(len(manu)):
	urls.append(url_part+manu[i])

for i in range(len(trading)):
	urls.append(url_part+trading[i])

for i in range(len(dev_bank)):
	urls.append(url_part+dev_bank[i])

for i in range(len(hotel)):
	urls.append(url_part+hotel[i])

for i in range(len(others)):
	urls.append(url_part+others[i])

#loop and getting request and making soup and getting company_name and table of the content
for url in urls:
	response=requests.get(url).content
	soup=BeautifulSoup(response,'lxml')

	cname=soup.find('span', id='ctl00_ContentPlaceHolder1_CompanyDetail1_companyName').text
	table=soup.find('table', class_='table table-striped table-hover table-zeromargin', id='accordion').text
	#this will remove spaces 
	rt=table.replace(' ','')
	# used for the removal of the unnecessary lines
	clean_rt = ""
	for line in rt.split("\n"):
	    if line.strip():
	        clean_rt += line + "\n"
	
	print(cname,'\n',clean_rt)