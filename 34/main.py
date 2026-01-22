# Build a news bot in python automate your daily news headlines

# pip install requests

import requests

def get_news_summary(category='technology'):
    api_key = "your api key"
    url = f"https://newsapi.org/v2/top-headlines"

    params={
        "category" : category,
        "Language" : "en",
        "apiKey" : api_key,
        "PageSize" : 5 # get top 5 news items
    }

    try:
        response = requests.get(url,params=params)

        data = response.json()

        if data["status"]=="ok":
            articles = data["articles"]
            print(f"\n Top 5 {category.upper()} HeadLines : ")
            print("-"*30)

            for i, articles in enumerate(articles):
                title = articles["title"]
                source = articles["source"]["name"]
                desc = articles["description"]

                print(f"{i}.{title}")
                print(f"Source : {source}")

                if desc:
                    print(f"Summary : {desc[:100]}...")
                    print("-"*30)

        else:
            print(f"Error : {data.get('message','unkown error')}")
    
    except Exception as e:
        print(f"An Error Occured : {e}")

get_news_summary("technology")