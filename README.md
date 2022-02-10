# Movie-Database
**Movie-Database is a website to filter out and find movies**

![alt text](https://i.postimg.cc/9WJ0TPGj/movie-site.png)

### Requirements
-  **Python3**
    - pip
	- virtualenv
- **NodeJs**
- **Npm**


### Installation

-  **Install Locally**

	Navigate to project folder
	
	```bash
	chmod +x install.sh
	./install.sh
	```
	
- **Docker Install**

	Navigate to project folder
	```bash
	docker-compose up
	```

### To Run

- Open 2 terminals
- Navigate to api/movie_database
- Run Django
```bash
python3 manage.py runserver
```

- In other terminal
- navigate to web/
- Run Vue
```bash
npm run serve
```
- Open your browser and navigate to http://localhost:8080

*Database has 100 movies and posters included*
