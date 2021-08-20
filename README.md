<p align="center">
  <h3 align="center">Platzigram</h3>

  <p align="center">
    Platzigram, web application
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
Platzigram is a web application created with the [ Curso de Django](https://platzi.com/clases/django/). 

This is a "clone" of instagram which allows you to have users, post photos, see photos of other users, etc.

#### Log In

![](https://raw.githubusercontent.com/murtagh95/platzigram/main/Image%20-%20Readme/login.png)

#### Profile

![](https://raw.githubusercontent.com/murtagh95/platzigram/main/Image%20-%20Readme/Perfil.PNG)

#### New Post

![](https://raw.githubusercontent.com/murtagh95/platzigram/main/Image%20-%20Readme/nueva_publicacion.PNG)


### Built With

*	Python 3
*	Django
*	Docker

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites for Local Development
* Python Programming Language

### Installation 

1. Clone the repo
   ```sh
   git clone https://github.com/murtagh95/platzigram
   ```
2. Change directory to platzigram
   ```sh
   cd platzigram
   ```
3. Install python module dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations and api server
   ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
   ```

### Using Docker Compose
1. Clone the repo
   ```sh
   git clone https://github.com/murtagh95/platzigram
   ```
2. Change directory to platzigram
   ```sh
   cd platzigram
   ```
3. Build containers with docker-compose
   ```sh
   docker-compose build
   ```
4. Start containers
   ```sh
   docker-compose up -d
   ```

<!-- USAGE EXAMPLES -->
## Usage

* Open http://127.0.0.1:8000/users/signup and register your user.

    ---------------------------------------------------o---------------------------------------------------


<!-- CONTACT -->
## Contact

Nicolas Catalano - nec.catalano@gmail.com