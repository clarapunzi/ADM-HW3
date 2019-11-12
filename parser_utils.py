# Define a function to get all the information available in the infobox

def parse_page(soup):
    infos_local = infos
    if bool(soup.findAll('table', {'class':'infobox vevent'})) == False:
        infos_local[:3] =[soup.title.text, soup.find_all('p')[0].text, soup.find_all('p')[1].text]
    else:
        infobox = soup.find_all('table', {'class':'infobox vevent'})[0].findAll('tr')
        infos_local[:4] =[soup.title.text, soup.find_all('p')[0].text, soup.find_all('p')[1].text, infobox[0].text]
        # complete the list 'infos' with the available information
        for j in range(len(head_wiki)):
            for i in range(1,len(infobox)):
                if bool(infobox[i].find('th')):
                    if head_wiki[j] == infobox[i].th.text:
                        infos_local[j+4] = infobox[i].td.text   # names in head_wiki correspond to those in head[4:]
                        break
    return infos_local