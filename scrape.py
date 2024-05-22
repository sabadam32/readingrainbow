from selenium.webdriver import Firefox, FirefoxOptions
from bs4 import BeautifulSoup
import sqlite3


db = sqlite3.connect('instance/cat.sqlite3')
db.row_factory = sqlite3.Row

options = FirefoxOptions()
options.add_argument("--headless")
browser = Firefox(options=options)
base_url = ""

# Get the last complete row of categories (Parent)
for row in db.execute('select * from category where length(mds_number)=5;'):
    name = row['mds_name']

    # The next level (Child) with incomplete categories
    for digit in range(10):
        number = f'{row["mds_number"]}{digit}'
        
        # Check if the category already exists
        item = db.execute(f"select * from category where mds_number='{number}';").fetchone()
        if item:
            # Already in DB... move on
            continue

        # Check to see if the Parent Category is unset.
        if name == 'not_set':
            # Set Child to 'not_set' and move on
            db.execute(f'insert into Category (mds_number, mds_name) values ("{number}", "not_set");')
            continue

        # We now have a potential category to lookup
        # Get the page source.
        url = base_url.format(number)
        browser.get(url)
        text = browser.page_source

        # lookup the category in the page
        soup = BeautifulSoup(text, "html.parser")
        line = soup.find("a", attrs={"href": f"/mds/{number}"})
        if line:
            new_name = line.text.strip().replace('"', '')
            try:
                db.execute(f'insert into Category (mds_number, mds_name) values ("{number}", "{new_name}");')
            except Exception:
                print(f'ID: {row["id"]}, Number: {number}, Name: {new_name}')
                new_name = new_name.replace('!', '').replace('@', '').replace('#', '').replace('%', '')
                print(new_name)
                db.execute(f'insert into Category (mds_number, mds_name) values ("{number}", "{new_name}");')
                print('Inserted modified name')
    db.commit()
