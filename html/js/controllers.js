var app = angular.module('LegalCitationApp',['ngRoute']);

// configure our routes
app.config(function($routeProvider) {
    $routeProvider

     // route for the home page
     .when('/', {
        templateUrl : '../pages/1-100.html',
        controller  : 'dynamicExamplesCtrl'
    })   
     .when('/1-100', {
        templateUrl : '../pages/1-100.html',
        controller  : 'dynamicExamplesCtrl'
    }) 
    .when('/1-200', {
        templateUrl : '../pages/1-200.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .otherwise({
        redirectTo: '/'
    });

});


app.controller('mainCtrl', ['$scope', function($scope) {
  console.log("In mainCtrl");
}]);


app.controller('dynamicExamplesCtrl', ['$scope', function($scope) {
  console.log("In dynamicExamplesCtrl");
}]);

