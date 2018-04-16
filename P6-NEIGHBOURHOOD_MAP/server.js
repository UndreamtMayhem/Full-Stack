/* jshint esversion: 6 */

// Core Node dependencies
const path = require('path');

// Custom Database Dependency
const config = require('./config/database');

// Node Dependencies
const express = require('express');
const mongoose = require('mongoose');

var MongoClient = require('mongodb').MongoClient,
    assert = require('assert');

// Init App
const app = express();

// Load View Engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// Set Public Folder
app.use(express.static(path.join(__dirname, 'public')));

// Home Route
app.get('/', function(req, res) {
    const title = "Cornwall Coast";
    return res.render("index", { title: title });
});

app.get('/places', function(req, res) {
    MongoClient.connect(url, function(err, client) {

        if (err) throw err;

        var db = client.db('neighbourhood');

        db.collection('places').find({}, { _id: false }).toArray(function(findErr, result) {
            if (findErr) throw findErr;
            client.close();
            return res.json(result);
        });
    });
});


// Start Server
app.listen(3000, function() {
    console.log('Server started on port 3000...');
});