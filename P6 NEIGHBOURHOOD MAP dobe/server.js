/* jshint esversion: 6 */

// Core Node dependencies
const path = require('path');

// Node Dependencies
const express = require('express');
const mongoose = require('mongoose');

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


// Start Server
app.listen(3000, function() {
    console.log('Server started on port 3000...');
});