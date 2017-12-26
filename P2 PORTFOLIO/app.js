var express = require('express');
var app = express();

app.set('view engine', 'pug');
app.set('views', './views');
app.use(express.static('public'));
/* COMPLETED */

app.get('/', function (req, res) {
    var about = {
        image: 'profile.png',
        links: [
            {
                url: 'https://www.facebook.com/UndreamtMayhem',
                name: 'facebook'
            },
            {
                url: 'https://plus.google.com/101453351757242399591',
                name: 'googleplus'
            },
            {
                url: 'https://twitter.com/undreamtmayhem',
                name: 'linkedin'
            },
            {
                url: 'https://www.instagram.com/undreamtmayhem/',
                name: 'instagram'
            },
            {
                url: 'https://github.com/UndreamtMayhem',
                name: 'github'
            },

        ],
        description: 'Front-End Web Developer from the UK. I am currently working on various projects. I have recently ' +
        'finished Front-End development and have now moved onto FULL-STACK. I will post links and resources ' +
        'on topics I have learnt. As well as making notes on key areas',
        skills: ['HTML5', 'CSS/SASS/LESS', 'Javascript', 'C#', 'Python', 'Ruby', 'C']
    }
    // send down the first part at least
    res.render('index', { about: about });
});

app.get('/portfolio', function (req, res) {
    var portfolio = {
        images: [
            { imageleft: 'http://placehold.it/350x150', imageright: 'http://placehold.it/350x150' },
            { imageleft: 'http://placehold.it/350x150', imageright: 'http://placehold.it/350x150' },
        ],
    }

    res.json(portfolio);
});

app.get('/projects', function (req, res) {
    var projects = {
        completed: [{
            title: 'FRONT-END WEB DEVELOPER',
            year: 'Year 2017/02/18',
            languagesUsed: ['HTML', 'CSS', 'JS'],
            description: 'Learnt the fundamentals of how the web works. I used the three foundational languages that' +
            ' power each and every website.',
            addtionaInfo: 'I used frameworks JQUERY and Bootstrap',
            githubsource: '/',
            projectImages: [
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
            ]
        }],
        current: [{
            title: 'FULL STACK WEB DEVELOPER',
            year: 'Year 2017/03/09',
            languagesUsed: ['RUBY', 'PYTHON', 'JS', 'C#'],
            description: 'Building complex server-side web applications that use powerful relational databases to persistently store ' +
            'data. I plan on building a movie trailer website, a portfolio website, Multi User Blog, Tournment Gauntlet ' +
            '(wait and see), item catalog and a neighbourhood map.',
            addtionaInfo: 'Frameworks &ndash; DJANGO, RAILS, NODE, AS',
            githubsource: '/',
            projectImages: [
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
            ],
        }],
        future: [{
            title: 'Using Python for GUIS',
            year: 'Year 2017',
            languagesUsed: ['PYTHON'],
            description: 'Creating a series of Apps for python I will list them very soon &mldr;',
            addtionaInfo: 'Frameworks: TK, Kivvy',
            githubsource: '/',
            projectImages: [
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
                'http://placehold.it/350x150',
            ],
        }],
    }
    res.json(projects);

});

app.get('/contacts', function (req, res) {
    var contacts = [
        {
            name: 'facebook',
            class: 'facebook',
            link: 'https://www.facebook.com/UndreamtMayhem',
        }, {
            name: 'google',
            class: 'google-plus',
            link: 'https://plus.google.com/101453351757242399591',
        },
        {
            name: 'twitter',
            class: 'twitter',
            link: 'https://twitter.com/undreamtmayhem',
        }, {
            name: 'tumblr',
            class: 'tumblr',
            link: '#',
        }, {
            name: 'email',
            class: 'envelope-o',
            link: '#',
        },
        {
            name: 'instagram',
            class: 'instagram',
            link: 'https://www.instagram.com/undreamtmayhem/',
        }, {
            name: 'linkedin',
            class: 'linkedin',
            link: '#',
        }, {
            name: 'github',
            class: 'github',
            link: 'https://github.com/UndreamtMayhem',
        },

    ]


    res.json(contacts);


});

app.get('/education', function (req, res) {
    var education = {
        webcourses: [
            {
                title: 'Intro to HTML and CSS - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Converted a digital design mockup into a static page. I used – HTML-CSS and bootstrap to accomplish it.'],
            },
            {
                title: 'Javascript Basic - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['I learned Javascript syntax and coding conventions. I used what I learned to build an interactive and dynamic website.']
            },
            {
                title: 'HTML Canvas - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Learned about HTML5 Canvas and how to use it to modify Images. Also to add text, change text color, change text foreground color, and word wrapping. I built a meme generator website.']
            }, {
                title: 'Intro to JQUERY - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Learned how to access and modify the DOM via Jquery.']
            }, {
                title: 'Intro to AJAX - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Learned how to perform asynchronous request. From a variety of sources google street view, New York times and Wikipedia. Refer to Cornwall Coast project']
            }, {
                title: 'Responsive Images - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Learned how to make images responsive via grunt. Learned about image set.']
            }, {
                title: 'Website Performance Optimization - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Learned how to make images responsive via grunt. Learned about image set.']
            }, {
                title: 'Browser Rendering Optimization - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Learned how browsers convert HTML, CSS and javascript into websites. Fixed a project that suffered from jank. Learned about google console and debugging.']
            }, {
                title: 'Object-oriented Javascript - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Build a variety of javascript objects. How inheritance works in javascript, psudeoclassical and the prototype chain. Used it to build a frogger javascript game.']
            }, {
                title: 'Responsive Web Design - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['How to make a website look great on every device designs fluid layout, mostly fluid and stacked examples will be added soon.']
            }, {
                title: 'Browser Rendering Optimization - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Demystified the browsers rendering pipeline and making it easy to build high performance web apps.']
            }, {
                title: 'JavaScript Testing - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Used red-green-refactor workflow cycle and automated testing. Built a testing framework for a CSS feed reader.']
            },
        ],
        fullstackcourses: [
            {
                title: 'Programming Foundation - UDACITY',
                githubrepos: '/',
                collegeLink: '/',                
                year: '2017',
                description: ['Learned object-oriented programming, code reuse and sharing code easily. Learned how software engineers think about solving problems. Mastering object-oriented programming.']
            },
            {
                title: 'Intro to backend - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Learned about web backend topics such as handling user input, producing templating objects. How to store information in the database. How to build a secure system with a secure user accounts. Protecting passwords with encryption. Hashing cookies to prevent tampering. Using salt with hashes. Learned about scaling and memory caching to prevent unnecessary reads from the database.']
            },
            {
                title: 'Intro to relational database- UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Dealt with database system such as Postgre SQL and MySQL. Learned the fundamentals and essentials of databases. Able to interact with databases from application code. Learned about CRUD.']
            },
            {
                title: 'Authentication and authorization: OAuth - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Implemented OAuth 2.0 framework to allow users to securely login to a web app. Built a flask restaurant menu application that implements google+ signin and facebook login. And once the user was logged in allowed them to create restaurants menus.']
            },
            {
                title: 'Using Full Stack - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Learned how to interact with a database from a web app using ORM layer. Learned how to GET and POST request translate to CRUD operations. Deployed a web app from the ground using iterative development process.']
            },
            {
                title: 'Designing Restful APIs - UDACITY',
                githubrepos: '/',
                collegeLink: '/',
                year: '2017',
                description: ['Writing Secure developer friendly APIs that will make your backend application thrive and keep your user happy.']
            },
        ],
        softwarecourses: [
            {
                title: 'CS50 - Harvard EDX',
                startdate: '24/05/2016',
                enddate: '25/05/2016',
                description: ['Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, PHP, and JavaScript plus SQL, CSS, and HTML.'],
                languagesUsed: 'C, PHP, and JavaScript plus SQL, CSS, and HTML.',

            },
            {
                title: 'Program design - Level introduction - EDX',
                startdate: '10/10/2016',
                enddate: '/',
                description: ['Learn a programming method that will allow you to develop programs that are clear, well tested, and easy for others to improve. How to represent information as data.- How to focus each part of your program on a single task. - How to use examples to clarify what your program should do. - How to determine the proper tests for a program. - How to simplify the structure of your program using common patterns.'],
                languagesUsed: 'Racket',

            },
            {
                title: 'Programming Languages - Udacity',
                startdate: '10/11/2016',
                enddate: '',
                description: ['This class will give you an introduction to the fundamentals of programming languages. Key concepts include how to specify and process valid strings, sentences and program structures. String Patterns: Find and specify classes of strings using regular expressions. Learn how to escape problematic characters. Represent a Finite State Machine. Lexical Analysis: Breaking strings down into important words.Write your own lexer that can tokenize HTML strings.Use regular expressions to parse, lex, and tokenize HTML and JavaScript. Grammars: How to specify and deconstruct valid sentences. Parsing grammars and discovering errors using regular expressions. Use generators to parse strings.',
                    'Parsing', 'Turning sentences into trees. Discover malformed input. Set precedence to prioritize parsing of strings. Interpreting: Simulating programs. Write an HTML interpreter. Calling functions and interpreting function definitions.Building a Web Browser: Interpreting HTML and JavaScript. Build your own web browser. Optimize the performance of your web browser.'
                ],
                languagesUsed: 'Python and JS',
            }, {
                title: 'Software Debugging Udacity',
                startdate: '24/05/2016',
                enddate: '25/05/2016',
                description: [
                    'Automating the Boring Tasks',
                    'Scientific method and its application to debugging.',
                    'Assertions in testing and in debugging.',
                    'Strategy of simplifying failures. Binary search. Delta debugging principle.',
                    'Cause-effect chain. Deduction. Dependencies. Slices.',
                    'Types of bugs (Bohr bug, Heisenbug, Mandelbug, Schrodinbug). Systematic reproduction process.',
                    'Bug database management. Classifying bugs. Bug maps. Learning from mistakes.'
                ],
                languagesUsed: 'General',

            }
        ],
        currentcourses: [
            {
                title: 'Programming Languages, Part A',
                description: 'Introduction to the basic concepts of programming languages, with a strong emphasis on functional programming. The course uses the languages ML, Racket, and Ruby as vehicles for teaching the concepts, but the real intent is to teach enough about how any language “fits together” to make you more effective programming in any language -- and in learning new ones.'
            },
            {
                title: 'Programming Languages, Part B',
                description: ''
            },
            {
                title: 'Programming Languages, Part C',
                description: ''
            }
        ],
        futurecourses: [
            {
                description: [
                    'I plan to broaden and build on my existing knowledge on algorithms to help look for ways to improve my code.',
                    'I plan on learning using two paradigms both OOP with c# and functional with Scala and f#. I have previously used OOP languages with Python, Ruby and C# and functional with both Racket, some Haskell and JavaScript. But I want to start to focus on strongly typed languages.',
                    'Refresh myself with maths with the following topics of Calculus which is useful for function programming and discrete math which is heavily involved in SQL Joins and Unions.',
                    'Finish FullStack development'
                ]
            }
        ]
    }

    res.json(education);
});


app.listen(3000);