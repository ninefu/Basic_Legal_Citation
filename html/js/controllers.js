var app = angular.module('LegalCitationApp',['ngRoute']);

// configure our routes
app.config(function($routeProvider) {
    $routeProvider

     // route for the home page
     .when('/', {
        templateUrl : '../pages/intro.html',
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
    .when('/1-300', {
        templateUrl : '../pages/1-300.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/1-400', {
        templateUrl : '../pages/1-400.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/1-500', {
        templateUrl : '../pages/1-500.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/1-600', {
        templateUrl : '../pages/1-600.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-100', {
        templateUrl : '../pages/2-100.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-200', {
        templateUrl : '../pages/2-200.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-300', {
        templateUrl : '../pages/2-300.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-400', {
        templateUrl : '../pages/2-400.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-500', {
        templateUrl : '../pages/2-500.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-600', {
        templateUrl : '../pages/2-600.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-700', {
        templateUrl : '../pages/2-700.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-800', {
        templateUrl : '../pages/2-800.html',
        controller  : 'dynamicExamplesCtrl'
    })
    .when('/2-900', {
        templateUrl : '../pages/2-900.html',
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

  //to enable popups
   $scope.showModal = false;
    $scope.buttonClicked = "";
    $scope.toggleModal = function(btnClicked){
        $scope.buttonClicked = btnClicked;
        $scope.showModal = !$scope.showModal;
    }
}]);

//Define a modal directive
app.directive('modal', function () {
    return {
      template: '<div class="modal fade">' + 
          '<div class="modal-dialog">' + 
            '<div class="modal-content">' + 
              '<div class="modal-header">' + 
                '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>' + 
              '</div>' + 
              '<div class="modal-body" ng-transclude></div>' + 
            '</div>' + 
          '</div>' + 
        '</div>',
      restrict: 'E',
      transclude: true,
      replace:true,
      scope:true,
      link: function postLink(scope, element, attrs) {
          scope.$watch(attrs.visible, function(value){
          if(value == true)
            $(element).modal('show');
          else
            $(element).modal('hide');
        });

        $(element).on('shown.bs.modal', function(){
          scope.$apply(function(){
            scope.$parent[attrs.visible] = true;
          });
        });

        $(element).on('hidden.bs.modal', function(){
          scope.$apply(function(){
            scope.$parent[attrs.visible] = false;
          });
        });
      }
    };
  });
