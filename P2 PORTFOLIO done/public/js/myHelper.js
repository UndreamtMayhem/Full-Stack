/*
    This file contains all of the code running 
    in the background that makes 
    resumeBuilder.js possible. 
*/

//Portfolio
var HTMLportfolioRow = '<div class="row"><div class="col-xs-1 col-sm-1 col-md-2 col-lg-2"></div>';
var HTMLportfolioImageLeft = '<div class="col-xs-12 col-sm-5 col-md-4 col-lg-4"><img class="img-responsive img-portfolio" src="%data%" alt=""></div>';
var HTMLportfolioImageRight = '<div class="col-xs-12 col-sm-5 col-md-4 col-lg-4"><img class="img-responsive img-portfolio" src="%data%" alt=""></div><div class="col-xs-2 col-sm-1 col-md-2 col-lg-2"></div></div>';

// Project Template 
var HTMLprojectTemplateStart = '<div class="row"><div class="col-xs-12 col-sm-12 col-md-12 col-lg-12"><div class="row"><div class="col-xs-12 col-sm-12 col-md-12 col-lg-12"><div class="row"><div class="col-xs-5 col-sm-5 col-md-3 col-lg-3">';
var HTMLprojectTitle = '<h4 class="project-title text-uppercase">%data%</h4>';
var HTMLprojectYear = '<h4 class="year">%data%</h4></div><div class="col-xs-1 col-sm-1 col-md-6 col-lg-6"></div><div class="col-xs-5 col-sm-5 col-md-3 col-lg-3"><h4 class="languages text-uppercase text-center">languages</h4>';
var HTMLprojectLanguages = '<p class="text-center">%data%</p></div></div></div></div><div class="row project-description"><div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">'
var HTMLprojectDescription = '<p>%data%</p>';
var HTMLprojectAddtional = '<p>%data%</p>';
var HTMLprojectSource = '<a class="zocial icon github center-element text-uppercase" href="%data%">Source</a></div></div>'
var HTMLprojectImageContainer = '<div class="row img-gal">';
var HTMLprojectImage = '<div class="col-xs-12 col-sm-6 col-md-3 col-lg-3"><img class="img-responsive img-project" src="%data%" alt=""></div>';
var HTMLprojectTemplateEnd = '</div></div></div>';

// Education Template
var HTMLeducationStartTag = '<div class="row">';
var HTMLeducationTitle = '<div class="col-xs-6 col-sm-6 col-md-3 col-lg-3"><h4 class="course-title">%title%</h4>';
var HTMLeducationSourceLink = '<a class="btn-sm btn-primary source-link" href="%link%">Courselink</a></div><div class="col-xs-1 col-sm-1 col-md-6 col-lg-6"></div><div class="col-xs-5 col-sm-5 col-md-3 col-lg-3">'
var HTMLeducationYear = '<div class="row"><div class="col-xs-6 col-sm-6 col-md-6 col-lg-6"></div><div class="col-xs-6 col-sm-6 col-md-6 col-lg-6"><p class="course-year">Year: %year%</p>';
var HTMLeducationEndTag = '</div></div></div></div>';
var HTMLeducationGithub = '<a class="zocial icon github center-element" href="%github%"></a>';
var HTMLeducationDescription = '<p class="education-description text-center">%description%</p>';

// SOFTWARE DEVELOPMENT
var HTMLsoftwareDevStartTag = '<div class="row">';
var HTMLsoftwareDevTitle = '<div class="col-xs-4 col-sm-4 col-md-3 col-lg-3"><h4>%title%</h4></div><div class="col-xs-3 col-sm-3 col-md-6 col-lg-6"></div>';

var HTMLsoftwareDevDate = '<div class="col-xs-4 col-sm-4 col-md-3 col-lg-3"><p>Start: %date%</p></div></div>';
var HTMLsoftwareDevDescription = '<p class="education-description">%description%</p>';
var HTMLsoftwareDevGithub = '<p><a class="zocial icon github center-element" href="%github%"></a></p>'

// CURRENT COURSE
var HTMLcurrentDevTitle = '<div class="row"><div class="col-xs-3 col-sm-3 col-md-3 col-lg-3"><h4>%title%</h4></div></div>';
var HTMLcurrentDevDesc = '<p class="education-description">%description%</p>';

// FUTURE COURSES
var HTMLfutureDesc = '<p class="education-description">%description%</p>';

// CONTACT
var HTMLcontactButton = '<a class="btn btn-default btn-block btn-lg %name%" href="%link%">'
var HTMLcontactIcon = '<i class="fa fa-%class%" aria-hidden="true"></i>'
var HTMLcontactText = '<span class="social-text">%name%</span></a>'