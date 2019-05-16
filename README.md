![simplinnovation](https://4.bp.blogspot.com/-f7YxPyqHAzY/WJ6VnkvE0SI/AAAAAAAADTQ/0tDQPTrVrtMAFT-q-1-3ktUQT5Il9FGdQCLcB/s350/simpLINnovation1a.png)

# 🐍 Digimon Beautifulsoup Web Scraping

### A simple Python project to scraping thousands of Digimon data (only its name & picture's url) from [Wikimon.net](https://wikimon.net/Visual_List_of_Digimon), then store all data into a csv file & MySQL database.

1. #### Activate MySQL server, create a database with a table inside:

    ```bash
    $ mysql -u yourUserName -p
    $ Enter password: *******
    $ create database digimon;
    $ use digimon;
    $ create table digimon(
        id int auto_increment,
        nama varchar(255),
        gambar varchar(255),
        primary key (id)
        ); 
    ```

2. #### Install Beautifulsoup & MySQL connector package via pip:

    ```bash
    $ pip install beautifulsoup4 MySQL-connector-python
    ```

3. #### Clone this repo & run _digimon.py_ file:

    ```bash
    $ git clone https://github.com/LintangWisesa/Digimon_BeautifulSoup_WebScraping
    $ run digimon.py
    ```

4. #### Enjoy~ 😎

#### Lintang Wisesa :love_letter: _lintangwisesa@ymail.com_

[Facebook](https://www.facebook.com/lintangbagus) | 
[Twitter](https://twitter.com/Lintang_Wisesa) |
[Google+](https://plus.google.com/u/0/+LintangWisesa1) |
[Youtube](https://www.youtube.com/user/lintangbagus) | 
:octocat: [GitHub](https://github.com/LintangWisesa) |
[Hackster](https://www.hackster.io/lintangwisesa)