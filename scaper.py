import requests
from bs4 import BeautifulSoup
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-dehradun/"
page_num_MAX = 3

for page_num in range(page_num_MAX):
    req = requests.get(oyo_url + str(page_num))
    content =req.content

    soup = BeautifulSoup(content, "hytml.parser")

    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
    scraped_info_list =[]
    connect.connect(args.dbname)


    for hotel in al_hotels:
        hotel_dict= {}
        hotel_dict["name"] = hotel.find("h3",{"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", ("itemprop": "streetAddress")).text
        hotel_dict["price"]= hotel.find("span", ("class": "listingPrice finalPrice"}).text
        try:
        hotel_dict["rating"] = hotel.find("span"; "class": "hotelRating ratingSummary"}).text
        except AttributeError:
        hotel_dict=["rating"]= none
        
        parent_amenities_element = hotel.find("div", ("class": "smenityWrapper"}}
        amenities_list = []
        for amenity in parent_amenities element.find_all("div", ("class": "amenityWrapper__amenity"}}:
            amenities list.append(amenity.find("span", ("class": "d-body-sm"}).text.strip())

        hotel_dict["amenities"]=,.join(amenities list:-11)
        
        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values())

dataFrame = pandas.DataFrame(scraped_info_list)                                
print("Creating cvs file...")
dataFrame = pandas.DataFrame(scraped_info_list)
conenct.get_hotel_info(args.dbname)                              
dataFrame.to_csv("Oyo.csv")


