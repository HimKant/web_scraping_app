
import streamlit as st
import pandas as pd



#google api modules
from googleapiclient.discovery import build

#credentials
api_key = "AIzaSyBh9_pQA2Vyh2YMgNUBYMWppFaJlR-Qyxs"
search_engine_id = "403255ea2525b46b4"


resource = build("customsearch", "v1" , developerKey = api_key).cse()

#request creation

request = resource.list(q = input("Enter search term :") , cx = search_engine_id)

#request execution
result = request.execute()

print("\n------------Search--------------\n\n")

print(f"search results (", result["searchInformation"]["searchTime"], ")")

print ("total" , len (result['items']), "results fetched")

for item in result['items']:
    print("___________________________________________")
    print("Title:", item["title"]) #title
    print("Link:", item["link"])
    print("Description:", item["snippet"])
    print("___________________________________________\n")

