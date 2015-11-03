var app = angular.module('LegalCitationApp',['ngRoute']);

 // configure our routes
    app.config(function($routeProvider) {
        $routeProvider

            // route for the home page
            .when('/', {
                templateUrl : '../pages/intro.html',
                controller  : 'dynamicExamplesCtrl'
            })            
    });


app.controller('mainCtrl', ['$scope', function($scope) {
  console.log("In mainCtrl");
}]);