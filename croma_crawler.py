

"""

get the key entry such as smart phones, laptops so on

get all hyperlinks related to it using r_html.findAll("a", {"class": "product__list--thumb"}) and 
price using r_html.findAll("span", {"class": "pdpPrice"})

get the paginated hyperlinks related to it using condition check &page= add it inside hyperlinks list and make a cralwer


create the REST framework api and to access that and test it using API Gateway

"""

import requests
from bs4 import BeautifulSoup
import bs4,re,os
from autoscraper import AutoScraper

def get_pagination():

	link_url=[]

	pg_Cnt=41
	
	for i in range(pg_Cnt):
		url=f"https://www.reliancedigital.in/smartphones/c/S101711?searchQuery=:relevance&page={i}"
		print(url)
		link_url.append(url)
		
	return link_url


def scrape_website():

	url_list=get_pagination()

	for url in url_list:

		if url is not None:

			page = requests.get(url)

			soup=BeautifulSoup(page.content,'html.parser')

			all_hyperlinks=soup.findAll("div", {"class": "pl__container"})

			hyperlinks=[]

			image_links=[]

			for link in all_hyperlinks[0].findAll("a"):

				h_link=link.get("href")
				print(h_link)
				hyperlinks.append(h_link)

			for link in all_hyperlinks[0].findAll("img"):

				i_link=link.get("data-srcset")
				print(i_link)

				image_links.append(i_link)

	return hyperlinks,image_links


scrape_website()























# for urls in container:
# 	hyperlink=urls.get("href")

# 	if hyperlink!=None:
		
# 		if "#" not in hyperlink and "linkedin" not in hyperlink and "javascript" not in hyperlink and "instagram" not in hyperlink and "facebook" not in hyperlink and "twitter" not in hyperlink:
# 			list_of_links.append(hyperlink)
# 		else:
# 			continue


# print()

# def page_crawl(input_url):

# 	full_hyperlink=main_url+input_url

# 	r = requests.get(full_hyperlink, headers={"User-Agent": "XY"})
	
# 	if r.status_code==200:

# 		print("visiting  url: {}".format(full_hyperlink))
# 		r_html = BeautifulSoup(r.text, 'html.parser')

# 		container_price = r_html.findAll("span", {"class": "pdpPrice"})

# 		for single_price in container_price:
# 			price_1=re.findall(r"₹[0-9 , .]+", str(single_price))
# 			di.update({my_url:price_1[0]})

# 	return di




# for my_url in list_of_links:

# 	if "&page=" in my_url: # paginated_urls !=None and paginated_urls not in hyper_links and
# 		print("visiting paginated url {}".format(my_url))

# 		if my_url not in list_of_links:
# 			op_di=page_crawl(my_url)
# 			#print(op_di)

# 	else:

# 		container2 = r_html.findAll("a", {"class": "product__list--thumb"})

# 		for url1 in container2:
# 			full_url=url1.get("href")

# 			op_di1=page_crawl(full_url)


















