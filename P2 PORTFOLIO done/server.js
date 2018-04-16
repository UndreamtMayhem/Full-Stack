// Node Dependencies
var express = require('express');
var app = express();

// Local Dependencies
var aboutme = require("./data/aboutme.js");

// Setting View Engine
app.set('view engine', 'pug');
app.set('views', './views');

// Setting public folder
app.use(express.static('public'));

/* Routes */

// Home Route
app.get('/', function(req, res) {

    res.render('index', {
        profile: aboutme.getProfile()
    });
});


/* JSON ROUTES */
app.get('/portfolio', function(req, res) {

    res.json(aboutme.getPortfolio());
});

app.get('/projects', function(req, res) {

    res.json(aboutme.getProjects());
});

app.get('/contacts', function(req, res) {

    res.json(aboutme.getContacts());
});

app.get('/education', function(req, res) {

    res.json(aboutme.getEducation());
});

app.listen(3000);