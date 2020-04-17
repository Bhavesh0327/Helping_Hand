# Helping_Hand
A help site for people in Trichy at this moment when Covid-19 is making it difficult for people fulfill their basic needs and asking for help.

## Installation

### Prerequisites
* Install Python
* Install Python Package Manager (pip/pip3) :
    ```
    apt-get install python-pip
    ```
    ```
    apt-get install python3-pip
    ```
* Install [virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) :
    ```
    apt-get install virtualenv
    ```
* Install [`mysqlclient`](https://pypi.org/project/mysqlclient/) prerequisites :
    * You may need to install the Python and MySQL development headers and libraries like so:
        ```
        sudo apt-get install python-dev default-libmysqlclient-dev
        ```
    * If you are using python3 then you need to install python3-dev using the following command :
        ```
        sudo apt-get install python3-dev
        ```
    * Install from PyPI:
        ```
        pip3 install mysqlclient
        ```

### Project Installation

1. Clone the repository - `git clone <remote-url>`
2. Go to the project directory - `cd <cloned-repo>`
3. Set up the environment :
    * Create virtual environment files - `virtualenv -p python3 venv`
    * Activate virtual environment - `source venv/bin/activate`
4. Install dependencies - `pip3 install -r requirements.txt`
5. Create a database - `helping_hand`
6. Copy contents of `.env.example` to a new file `.env` - `cp .env.example .env`
    * Set DB_USERNAME and DB_PASSWORD to your localhost mysql credentials
7. Make migrations - `python3 manage.py makemigrations`
8. Run migrations - `python3 manage.py migrate`
9. Start server - `python3 manage.py runserver`
