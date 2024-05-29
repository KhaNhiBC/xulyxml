from bs4 import BeautifulSoup
#doc du lieu
with open('items.xml','r') as f:
    data = f.read()
#truyen du lieu
bs_data = BeautifulSoup(data,"xml")
#tim tat ca cac the
item = bs_data.find_all('items')
print(item)
name = bs_data.find('item',{'name':'item1'})
print(name)
text = name.get_text()
print(text)
value = name.get('price')
print(value)