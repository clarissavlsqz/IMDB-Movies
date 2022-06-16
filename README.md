# Proyecto Final - Diseño y Arquitectura de Software

### Flix - Endpoints

#### Login (/login)

El usuario necesita ingresar su usuario y correo electrónico, si son válidos y existentes en la base de datos entonces el proceso se realizará con éxito. De lo contrario saldrá un mensaje de error.

#### Register (/register_user)

El usuario necesita ingresar un usuario, correo electrónico y los tres números correspondientes a los génreos de su gusto. Si los campos ingresados son nuevos y válidos, entonces el proceso se realizará con éxito. De lo contrario saldrá un mensaje de error.

#### Get Movies Based on Preference Key (/getMoviesRecs) (/getMoviesRecs/False)

Como el proyecto no contiene un frontend, por el momento se requeríra que el usuario ingrese su correo electrónico para verifcar si está registrado. El resultado de este endpoint será una lista ordenada de las 10 películas con mayor rating o valoración, basadas en la llave de preferencia. Si se le agrega "False" a la ruta, entonces saldrán las 10 películas con menor rating o valoración, dependiedo de la llave de preferencia.

Ejemplo con una lista de 3 películas

    /getMoviesRecs
    preference_key = 3

    {
        "movie_title": "Batman: El Caballero de la Noche",
        "rating": 8.993127135124897,
        "year": 2008
    },
    {
        "movie_title": "El señor de los anillos: El retorno del rey",
        "rating": 8.92713309278143,
        "year": 2003
    },
    {
        "movie_title": "Forrest Gump",
        "rating": 8.776386232422228,
        "year": 1994
    }
    ...

    /getMoviesRecs/False
    preference_key = 3

    {
        "movie_title": "Jai Bhim",
        "rating": 8.01634138750673,
        "year": 2021
    },
    {
        "movie_title": "Sucedió una noche",
        "rating": 8.020466643288529,
        "year": 1934
    },
    {
        "movie_title": "La novicia rebelde",
        "rating": 8.023213477544674,
        "year": 1965
    }
    ...

#### Get Movies Based on Star Cast (/getMoviesByStar/name) (/getMoviesByStar/name/False)

Como el proyecto no contiene un frontend, por el momento se requeríra que el usuario ingrese su correo electrónico para verifcar si está registrado. Al final de la ruta se tiene que agregar el nombre del artista que se quiere buscar. El resultado serán todas las películas en las que aparezca el artista. Si se agrega "False" al final de la ruta, entonces las películas saldrán en orden de menor a mayor rating.

    /getMoviesByStar/Brad Pitt

    {
        "movie_title": "El club de la pelea",
        "rating": 8.760115474108114,
        "year": 1999
    },
    {
        "movie_title": "Seven, los siete pecados capitales",
        "rating": 8.611786867573802,
        "year": 1995
    },
    {
        "movie_title": "Bastardos sin gloria",
        "rating": 8.318201499478498,
        "year": 2009
    },
    {
        "movie_title": "Snatch: Cerdos y diamantes",
        "rating": 8.23042572326987,
        "year": 2000
    }

#### Get Movies Based on Rating Range (/getMoviesByRating/low_rating/high_rating) (/getMoviesByRating/low_rating/high_rating/False)

Como el proyecto no contiene un frontend, por el momento se requeríra que el usuario ingrese su correo electrónico para verifcar si está registrado. En la ruta se tienen que agregar dos numeros flotantes, el primero para indicar el minimo rating y el segundo para indicar el máximo rating. El resultado serán todas las películas que esté dentro de ese rango. Si se agrega "False" al final de la ruta, entonces las películas saldrán en orden de menor a mayor rating.

    /getMoviesByRating/8.5/9.0

    {
        "movie_title": "Batman: El Caballero de la Noche",
        "rating": 8.993127135124897,
        "year": 2008
    },
    {
        "movie_title": "El padrino II",
        "rating": 8.99012508760967,
        "year": 1974
    },
    {
        "movie_title": "12 hombres en pugna",
        "rating": 8.95049628688856,
        "year": 1957
    },
    ...

#### Get Movies Based on Year (/getMoviesByYear/year) (/getMoviesByYear/year/False)

Como el proyecto no contiene un frontend, por el momento se requeríra que el usuario ingrese su correo electrónico para verifcar si está registrado. En la ruta se tiene que agregar el año a buscar. El resultado serán todas las películas que hayan salido en ese año. Si se agrega "False" al final de la ruta, entonces las películas saldrán en orden de menor a mayor rating.

    /getMoviesByYear/2004/False

    {
        "movie_title": "Antes del atardecer",
        "rating": 8.032732152632061,
        "year": 2004
    },
    {
        "movie_title": "Los increíbles",
        "rating": 8.034842016087712,
        "year": 2004
    },
    {
        "movie_title": "Hotel Ruanda",
        "rating": 8.061086248052744,
        "year": 2004
    },
    ...

## Design Patterns

Los siguientes diagramas de clases representan algunos de los patrones que se pueden encontrar en el código.

### Command Pattern

El patrón de comando se utilizó para las solicitudes de registro de usuario y el ingreso de sesión.

![CommandPattern](https://www.dropbox.com/s/zenwddju5znssji/CommandPattern.jpg?dl=0&raw=1)

### Facade Pattern

En este caso el patrón de Facade se utilizó para agrupar las dependencias que se necesitan para obtener películas.

![FacadePattern](https://www.dropbox.com/s/93ad1acco70do6b/FacadePattern.jpg?dl=0&raw=1)

### Simple Factory Pattern

El patrón de fabrica simple se utilizó para conseguir el Data Frame con los datos requeridos dependiendo del endpoint a utilizar.

![SimpleFactory](https://www.dropbox.com/s/7pshehx3gw5q11o/SimpleFactory.jpg?dl=0&raw=1)

## Running the project

Project can be build using the following command:

    docker-compose build

Project can be run using the following command:

    docker-compose –-env-file config/dev.env up

You can connect to the running container using the following command:

    docker-compose exec app bash

You can connect to the database using the following command:

    docker-compose –-env-file config/dev.env exec postgres psql -h localhost -U movies movies

You can recreate the database with the following command:

    docker-compose -–env-file config/dev.env rm -v postgres

You can access the project using the following url:

http://localhost:5005/register_user
