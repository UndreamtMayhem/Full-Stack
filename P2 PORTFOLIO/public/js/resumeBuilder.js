$(document).ready(function() {
    portofolio = {};
    projects = {};
    contacts = {};
    education = {};

    portofolio.display = function() {
        $.getJSON("/portfolio", function(data) {
            $.each(data.images, function(key, image) {
                var elem = HTMLportfolioRow + HTMLportfolioImageLeft.replace("%data%", image.imageleft) +
                    HTMLportfolioImageRight.replace("%data%", image.imageright);
                $('#portfolio').append(elem);
            });
        });
    }

    projects.display = function() {
        $.getJSON("/projects", function(data) {
            var helperFunc = function(data, elementToAttachTo) {
                $.each(data, function(key, val) {

                    // fetch all languages
                    var languages = '';
                    for (var i = 0; i < val.languagesUsed.length; i++) {
                        languages += val.languagesUsed[i] + ", ";
                    }

                    // fetch all images
                    var imgs = '';
                    for (var i = 0; i < val.projectImages.length; i++) {
                        imgs += HTMLprojectImage.replace('%data%', val.projectImages[i]);
                    }

                    // add all data
                    var elem = HTMLprojectTemplateStart +
                        HTMLprojectTitle.replace('%data%', val.title) +
                        HTMLprojectYear.replace('%data%', val.year) +
                        HTMLprojectLanguages.replace('%data%', languages) +
                        HTMLprojectDescription.replace('%data%', val.description) +
                        HTMLprojectAddtional.replace('%data%', val.addtionaInfo) +
                        HTMLprojectSource.replace('%data%', val.githubsource) +
                        imgs + HTMLprojectTemplateEnd;

                    $(elementToAttachTo).after(elem);
                });
            }
            helperFunc(data.completed, '#project-completed h3');
            helperFunc(data.current, '#project-current h3');
            helperFunc(data.future, '#project-future h3');
        });
    }

    education.display = function() {
        $.getJSON("/education", function(data) {

            var helperFunc = function(data, elementToAttachTo) {
                $.each(data, function(key, val) {
                    var HTMLallDescriptions = '';
                    for (var i = 0; i < val.description.length; i++) {
                        HTMLallDescriptions += HTMLeducationDescription.replace('%description%', val.description[i]);
                    }


                    var webcoursesElement = HTMLeducationStartTag +
                        HTMLeducationTitle.replace('%title%', val.title) +
                        HTMLeducationSourceLink.replace('%link%', val.githubrepos) +
                        HTMLeducationYear.replace('%year%', val.year) +
                        HTMLeducationEndTag +
                        HTMLallDescriptions +
                        HTMLeducationGithub.replace('%github%', val.githubrepos);
                    $(elementToAttachTo).append(webcoursesElement);

                });
            }
            helperFunc(data.webcourses, '#front-end');
            helperFunc(data.fullstackcourses, '#full-stack');

            // SOFTWARE DEVELOPMENT
            function softwareDevelopment() {
                $.each(data.softwarecourses, function(key, val) {
                    var HTMLallDescriptions = '';

                    for (var i = 0; i < val.description.length; i++) {
                        HTMLallDescriptions += HTMLsoftwareDevDescription.replace('%description%', val.description[i]);
                    }

                    var webcoursesElement = HTMLsoftwareDevStartTag +
                        HTMLsoftwareDevTitle.replace('%title%', val.title) +
                        HTMLsoftwareDevDate.replace('%date%', val.startdate) +
                        HTMLallDescriptions +
                        HTMLsoftwareDevGithub.replace('%github%', val.githubrepos);
                    $('#software-development').append(webcoursesElement);
                });
            }

            // CURRENTCOURSES
            function currentCourses() {
                $.each(data.currentcourses, function(key, val) {
                    var webcoursesElement = HTMLcurrentDevTitle.replace('%title%', val.title) +
                        HTMLcurrentDevDesc.replace('%description%', val.description);
                    $('#education-current').append(webcoursesElement);
                });
            }

            // FUTURECOURSES
            function futureCourses() {
                $.each(data.futurecourses, function(key, val) {
                    var HTMLallDescriptions = '';

                    for (var i = 0; i < val.description.length; i++) {
                        HTMLallDescriptions += HTMLfutureDesc.replace('%description%', val.description[i]);
                    }

                    $('#education-future').append(HTMLallDescriptions);
                });
            }


            softwareDevelopment();
            currentCourses();
            futureCourses();
        });
    }

    contacts.display = function() {
        $.getJSON("/contacts", function(data) {

            $.each(data, function(key, val) {

                var HTMLcontactCompleteTag = HTMLcontactButton.replace('%name%', val.name).replace('%link%', val.link) + HTMLcontactIcon.replace('%class%', val.class) + HTMLcontactText.replace('%name%', val.name);

                if (key <= 3) {
                    $('.social-button-left').append(HTMLcontactCompleteTag);
                } else {
                    $('.social-button-right').append(HTMLcontactCompleteTag);
                }
            });
        });
    }

    portofolio.display();
    projects.display();
    education.display();
    contacts.display();
});