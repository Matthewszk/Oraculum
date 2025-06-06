from utils.gemini import query


def get_title():
    topic = input("Topic Name: ")
    while True:
        print("Titles Generating..")
        data = query(f"Give 5 titles for YouTube shorts related to topic '{topic}' seperated by commas.")
        if data:
            titles = data["candidates"][0]["content"]["parts"][0]["text"].split(',')
            titles.append(topic)
            for i in range(len(titles)):
                print(str(i) + " : " + titles[i])
            choice = int(input("Enter your choice of title: "))
            if choice == -1:
                continue
            print("Title Acquired!")
            with open("./outputs/title.txt", "w",encoding='utf-8') as f:
                f.write(titles[choice])
            return titles[choice]
        else:
            print("FATAL ERROR :(")
            exit()

def get_content(title):
    while True:
        data = query(f"Explain about this topic {title} in short for 1 min. Be creative.")
        if data:
            content = data["candidates"][0]["content"]["parts"][0]["text"]
            print(content)
            satisfied = input("Good to go? (y/n) : ")
            if satisfied != "n":
                return content
            else:
                continue 
        else:
            print("FATAL ERROR :(")
            exit()

def write_content(content):
    with open(f"./outputs/text.txt", "w",encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    write_content(get_content(get_title()))
