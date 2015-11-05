var app = angular.module('LegalCitationApp',['ngRoute']);

// configure our routes
app.config(function($routeProvider) {
    $routeProvider

     // route for the home page
     .when('/', {
        templateUrl : '../pages/intro.html'
    })   
     .when('/1-100', {
        templateUrl : '../pages/1-100.html'
    }) 
    .when('/1-200', {
        templateUrl : '../pages/1-200.html'
    })
    .when('/1-300', {
        templateUrl : '../pages/1-300.html'
    })
    .when('/1-400', {
        templateUrl : '../pages/1-400.html'
    })
    .when('/1-500', {
        templateUrl : '../pages/1-500.html'
    })
    .when('/1-600', {
        templateUrl : '../pages/1-600.html'
    })
    .when('/2-100', {
        templateUrl : '../pages/2-100.html'
    })
    .when('/2-200', {
        templateUrl : '../pages/2-200.html'
    })
    .when('/2-300', {
        templateUrl : '../pages/2-300.html'
    })
    .when('/2-400', {
        templateUrl : '../pages/2-400.html'
    })
    .when('/2-500', {
        templateUrl : '../pages/2-500.html'
    })
    .when('/2-600', {
        templateUrl : '../pages/2-600.html'
    })
    .when('/2-700', {
        templateUrl : '../pages/2-700.html'
    })
    .when('/2-800', {
        templateUrl : '../pages/2-800.html'
    })
    .when('/2-900', {
        templateUrl : '../pages/2-900.html'
    })
    .when('/3-100', {
        templateUrl : '../pages/3-100.html'
    })
    .when('/3-200', {
        templateUrl : '../pages/3-200.html'
    })
    .when('/3-300', {
        templateUrl : '../pages/3-300.html'
    })
    .when('/3-400', {
        templateUrl : '../pages/3-400.html'
    })
    .when('/3-500', {
        templateUrl : '../pages/3-500.html'
    })
    .when('/3-600', {
        templateUrl : '../pages/3-600.html'
    })
    .when('/3-700', {
        templateUrl : '../pages/3-700.html'
    })
    .when('/3-800', {
        templateUrl : '../pages/3-800.html'
    })
    .when('/4-100', {
        templateUrl : '../pages/4-100.html'
    })
    .when('/4-200', {
        templateUrl : '../pages/4-200.html'
    })
    .when('/4-300', {
        templateUrl : '../pages/4-300.html'
    })
    .when('/4-400', {
        templateUrl : '../pages/4-400.html'
    })
    .when('/4-500', {
        templateUrl : '../pages/4-500.html'
    })
    .when('/4-600', {
        templateUrl : '../pages/4-600.html'
    })
    .when('/4-700', {
        templateUrl : '../pages/4-700.html'
    })
    .when('/4-800', {
        templateUrl : '../pages/4-800.html'
    })
    .when('/5-000', {
        templateUrl : '../pages/5-000.html'
    })
    .when('/5-100', {
        templateUrl : '../pages/5-100.html'
    })
    .when('/5-200', {
        templateUrl : '../pages/5-200.html'
    })
    .when('/5-300', {
        templateUrl : '../pages/5-300.html'
    })
     .when('/6-100', {
        templateUrl : '../pages/6-100.html'
    })
    .when('/6-200', {
        templateUrl : '../pages/6-200.html'
    })
    .when('/6-300', {
        templateUrl : '../pages/6-300.html'
    })
    .when('/6-400', {
        templateUrl : '../pages/6-400.html'
    })
    .when('/6-500', {
        templateUrl : '../pages/6-500.html'
    })
     .when('/7-100', {
        templateUrl : '../pages/7-100.html'
    })
    .when('/7-200', {
        templateUrl : '../pages/7-200.html'
    })
    .when('/7-300', {
        templateUrl : '../pages/7-300.html'
    })
    .when('/7-400', {
        templateUrl : '../pages/7-400.html'
    })
    .when('/7-500', {
        templateUrl : '../pages/7-500.html'
    })
    .when('/toc', {
        templateUrl : '../pages/toc.html'
    })
    .when('/index', {
        templateUrl : '../pages/content_index.html'
    })
    .when('/help', {
        templateUrl : '../pages/help.html'
    })
    .when('/about', {
        templateUrl : '../pages/about.html'
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
