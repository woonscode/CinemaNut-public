const express = require('express');
const cors = require('cors');
const axios = require('axios');

// Create Express app instance
const app = express()
const PORT = 4004
const HOST = '0.0.0.0'

// Get environment variable API_KEY
const API_KEY = process.env.API_KEY

// Allow CORS with Express.js app
app.use(cors())

// Get list of movies by title
app.get('/movie_external/search/titles/:title', (req, res) => {
    let options = {
        method: 'GET',
        url: 'https://unogs-unogs-v1.p.rapidapi.com/search/titles',
        params: {
            type: 'movie', 
            order_by: 'date', 
            title: req.params.title.toLowerCase()
        },
        headers: {
          'X-RapidAPI-Host': 'unogs-unogs-v1.p.rapidapi.com',
          'X-RapidAPI-Key': API_KEY,
        }
      };
      
    axios.request(options).then(function (response) {
        let response_list = response.data.results
        let returned = []
        for (movie of response_list) {
            let movie_title = movie.title.toLowerCase()
            if (movie_title.includes(req.params.title.toLowerCase())) {
               returned.push(movie) 
            }
        }
        result = {"code": response.status, "data": returned}
        res.json(result)
    })
    .catch(function (error) {
        res.json(error)
    });
})

// Get list of genres available
app.get('/movie_external/genres', (req, res) => {
    let options = {
        method: 'GET',
        url: 'https://unogs-unogs-v1.p.rapidapi.com/static/genres',
        headers: {
          'X-RapidAPI-Host': 'unogs-unogs-v1.p.rapidapi.com',
          'X-RapidAPI-Key': API_KEY,
        }
      };
      
    axios.request(options).then(function (response) {
        result = {"code": response.status, "data": response.data.results}
        res.json(result)
    })
    .catch(function (error) {
        res.json(error)
    });
})

// Get details of a specific movie based on movie_id + genres + images
app.get('/movie_external/title/:movie_id/details', (req, res) => {
    let options_details = {
        method: 'GET',
        url: 'https://unogs-unogs-v1.p.rapidapi.com/title/details',
        params: {netflix_id: req.params.movie_id},
        headers: {
          'X-RapidAPI-Host': 'unogs-unogs-v1.p.rapidapi.com',
          'X-RapidAPI-Key': API_KEY,
        }
      };
    let options_genres = {
        method: 'GET',
        url: 'https://unogs-unogs-v1.p.rapidapi.com/title/genres',
        params: {netflix_id: req.params.movie_id},
        headers: {
            'X-RapidAPI-Host': 'unogs-unogs-v1.p.rapidapi.com',
            'X-RapidAPI-Key': API_KEY,
        }
    };
    let options_images = {
        method: 'GET',
        url: 'https://unogs-unogs-v1.p.rapidapi.com/title/images',
        params: {netflix_id: req.params.movie_id},
        headers: {
            'X-RapidAPI-Host': 'unogs-unogs-v1.p.rapidapi.com',
            'X-RapidAPI-Key': API_KEY,
        }
    };
    axios.request(options_details).then(function (response) {
        result = {"code": response.status, "data": response.data}
        axios.request(options_genres).then(function (response) {
            result.data.genres = response.data.results
            axios.request(options_images).then(function (response) {
                result.data.images = response.data.results
                res.json(result)
            })
            .catch(function (error) {
                res.json(error)
            });
        })
        .catch(function (error) {
            res.json(error)
        });
    })
    .catch(function (error) {
        res.json(error)
    });
})

app.listen(PORT, HOST, () => 
    console.log(`Server is running on port ${PORT}`)
);