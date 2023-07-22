import requests
import json
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

def task1():
    """
        Use the specific url to convert the .json format to the .csv format
        Don't use any third party tools
    """
    print("Running task1...")
    url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
    data_json = json.loads(urlopen(url).read())
    # ====================================
    # For checking the json file content
    # ====================================
    # stitle => attraction name
    # address => use address to extract the district of Taiwan
    # longitude, latitude
    # file => get the first img html
    # with open("test.txt", "w", encoding="UTF-8") as f:
    #     for list in data_json["result"]["results"]:
    #         for key,val in list.items():
    #             f.write(str(key) + "\n")
    #             f.write("    " + str(val) + "\n")
    #         f.write("=="*20 + "\n")

    # For the district
    dist_set = ["中正區","萬華區","中山區","大同區","大安區","松山區","信義區","士林區","文山區","北投區","內湖區","南港區"]
    # For the MRT
    mrt_stop_dict = {}
    with open("attraction.csv", "w", encoding="utf-8-sig", newline='') as atrc_file, open("mrt.csv", "w", encoding="utf-8-sig", newline='') as mrt_file:
        atrc_writer = csv.writer(atrc_file)
        mrt_writer = csv.writer(mrt_file)
        for list in data_json["result"]["results"]:
            # ============
            # Attraction
            # ============
            atrc_row = []
            # Attraction name
            atrc_row.append(list["stitle"])
            # District name
            for dist in dist_set:
                word = list["address"].encode('utf8')[3:].decode('utf8')
                if word.find(dist) != -1:
                    atrc_row.append(dist)
            # Longitude
            atrc_row.append(list["longitude"])
            # Latitude
            atrc_row.append(list["latitude"])
            # First jpg html
            atrc_row.append(list["file"].lower().split(".jpg")[0]+".jpg")
            # Write to CSV
            atrc_writer.writerow(atrc_row)

            # ===========
            # MRT parse
            # ===========
            if list["MRT"] == None: continue
            if list["MRT"] not in mrt_stop_dict:
                mrt_stop_dict[list["MRT"]] = [list["stitle"]]
            else:
                mrt_stop_dict[list["MRT"]].append(list["stitle"])
        # ============
        # MRT write
        # ============
        for key,val in mrt_stop_dict.items():
            mrt_writer.writerow([key] + val)

def task2():
    """
        Use BeautifulSounp4 to parse html content
        => 3 pages
        title, # of tweets, release time
    """
    print("Running task2...")
    url_prefix = "https://www.ptt.cc"
    url = "https://www.ptt.cc/bbs/movie/index.html"
    num_pages_catched = 3

    with open("movie.txt", "w", encoding="utf-8-sig", newline='') as movie_file:
        for i in range(0,num_pages_catched):
            # Get the current page soup
            soup = BeautifulSoup(requests.get(url).text, "html.parser")

            # Parse title and # of tweets
            title = soup.select("div.title")
            tweets = soup.select("div.nrec")
            # Change to the page and get the time
            sub_pages = soup.select("div.title > a")
            for iter,sub_page in enumerate(sub_pages):
                if "本文已被刪除" in title[iter].text : continue
                tweet_page_href = sub_page["href"]
                tweet_url = url_prefix + tweet_page_href
                soup = BeautifulSoup(requests.get(tweet_url).text, "html.parser")
                meta_value = soup.select("div.article-metaline>span.article-meta-value")
                movie_file.write("".join(title[iter].text.split("\n")) + ",")
                movie_file.write("".join(tweets[iter].text.split("\n")) + ",")
                movie_file.write("".join(meta_value[-1].text.split("\n")) + "\n")


            # Change to the previous page
            soup = BeautifulSoup(requests.get(url).text, "html.parser")
            btn = soup.select("div.btn-group > a")
            up_page_href = btn[3]["href"]
            url = url_prefix + up_page_href



if __name__=="__main__":
    task1()
    task2()