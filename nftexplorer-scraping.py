from selenium import webdriver
import time

url = "https://www.nftexplorer.app/asset/{ID_ASSET}"
driver = webdriver.Chrome(executable_path="/Users/salvatorecorvaglia/Downloads/scraping-algo-main/chromedriver")

#create file o reset if exist
file = open('addresses.txt', 'w')
file.close()

#open file in append mode
file = open('addresses.txt', 'a')

#get page
driver.get(url)
time.sleep(5)

#extract table
x = driver.find_element_by_tag_name("tbody")
text = x.get_attribute("innerHTML")

#table to list
list = text.split("<tr>")
list.reverse()


# extract escrow account address
popped_row = list.pop(0)

columns = popped_row.split("<th")
receiver_column = columns[4]

start = receiver_column.find("title=\"") + len("title=\"")
end = receiver_column.find("\"><a")
escrow_account = receiver_column[start:end]
print(escrow_account)

#get row addresses
i = 1
for row in list:
    print("Fetching row num " + str(i))
    sender = ""
    receiver = ""

    columns = row.split("<th")

    #extract sender address
    sender_column = columns[3]
    start = sender_column.find("title=\"") + len("title=\"")
    end = sender_column.find("\"><a")
    sender = sender_column[start:end]

    if sender == escrow_account:
        #extract receiver address
        receiver_column = columns[4]
        start = receiver_column.find("title=\"") + len("title=\"")
        end = receiver_column.find("\"><a")
        receiver = receiver_column[start:end]
        file.write(receiver)
        file.write("\n")

    i = i + 1

file.close()
