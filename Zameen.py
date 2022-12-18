from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time 

with open(r'path.csv','w+',newline="") as writefile:
# Path of CSV file in which the Scraped Data is Stored.
    
    f= open(r'path.txt','r')
    write.writerow(['Name','Description','PropertyType','Price','Area','City','Area Digit','Area Type','Purpose','Estate','Mobile No','Phone No','Agent'])
# We use Text file where we place the link of one Page that include many Properties.
    loop=f.readlines()

    for ab in loop:

        driver = webdriver.Chrome()
        driver.get(ab)

        aa = driver.find_element_by_class_name("bbfbe3d2") # entering in main div
        bb = aa.find_element_by_tag_name("ul") # entering into un ordered list of properties
        cc = bb.find_elements_by_class_name("ef447dde") # one property unit with article tag
     
    
        for i in cc:
            dd = i.find_element_by_tag_name("a") # getting link of proeprty
            
            title=dd.get_attribute("title")
            print("Tittle : ",title)
            property_link = dd.get_attribute("href")

            print("LINK:", property_link)
            driver3 = webdriver.Chrome()
            driver3.get(property_link)
            d1=driver3.find_element_by_class_name("_2015cd68")
            description=d1.text
            print(description) 

            d1 = driver3.find_element_by_class_name("_066bb126")
            ul = d1.find_element_by_class_name("_033281ab")
            lii = ul.find_elements_by_tag_name("li")
            a = []
            for ii in lii:
                a.append(ii.text)
            # print(a)
            zameen_type = a[0].split('\n')[1]
            print('zameen_type:', zameen_type)
            price = a[1].split('\n')[1].split('  ')[1]
            print("price:", price)
            lo = a[2].split('\n')[1]
            location_area = lo
            print("location_area:", location_area)
            location_city = lo.split(',')[1]
            print("location_city:", location_city)
            location_province = lo.split(',')[2]
            print("location_province:", location_province)
            Area = a[4].split('\n')[1].split(' ')
            Area_digit = Area[0]
            print("Area_digit :", Area_digit)
            Area_type = Area[1]
            print("Area_type:", Area_type)
            pur = a[5].split('\n')
            purpose = pur[1]
            print("purpose : ", purpose)
            ad = a[7].split('\n')
            added = ad[1]
            print("added:", added)
            print('-------------')
            try:
                estate=driver3.find_element_by_class_name('_5a588edf')
                e=estate.text
            except:
                e='Not Given'
            print(e)
            

            l=[]
            l.append(title)
            l.append(description)
            l.append(zameen_type)
            l.append(price)
            l.append(location_area)
            l.append(location_city)
            l.append(Area_digit)
            l.append(Area_type)
            l.append(purpose)
            l.append(e)   

            element = driver3.find_element_by_xpath("//button[@class='_5b77d672 da62f2ae ce26935f']")
            driver3.execute_script("arguments[0].click();", element)
   
        
            time.sleep(10)
            soup = BeautifulSoup(driver3.page_source, 'html5lib')
            pop_up = soup.findAll('div', {'aria-label': 'Dialog'})[1]
            table = pop_up.find('table', {'class': 'e5298ac6'})
            t_rows = table.findAll('tr',{'class': 'ae111ad6'})
            for t in t_rows:
                t1 = t.find('td',{'class': '_5f3a31f7'})
                try:
                    t11=t1.a.span.text.split('+')[1]
                    t12=t11.split('-')
                    t13=t12[0]+t12[1]
                    
                except:
                    t13='Not Given'
                print(t13)   
                l.append(t13)
            agen=table.find('tr',{'class':'_317da960'})
            agent=agen.text.split('Agent')[1]
            print(agent)
            l.append(agent)
            write.writerow(l)
            driver3.close()
            print('---------------------------')
        driver.close()
    writefile.close()
