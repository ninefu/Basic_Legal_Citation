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


app.controller('mainController', function($scope) {
  console.log("Init'd statePracticesCtrl")
  $scope.sortType     = 'state'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  $scope.searchFish   = '';     // set the default search/filter term
  
  // create the list of sushi rolls 
  $scope.countries = [
{state: 'Alabama', Cases: '3-200.html#3-210_Alabama', Statutes:'3-300.html#3-320_Alabama', Regulations:'3-400.html#3-410_Alabama', Examples_and_Rules:'state_samples/sample_alabama.html'},
{state: 'Alaska', Cases: '3-200.html#3-210_Alaska', Statutes:'3-300.html#3-320_Alaska', Regulations:'3-400.html#3-410_Alaska', Examples_and_Rules:'state_samples/sample_alaska.html'},
{state: 'Arizona', Cases: '3-200.html#3-210_Arizona', Statutes:'3-300.html#3-320_Arizona', Regulations:'3-400.html#3-410_Arizona', Examples_and_Rules:'state_samples/sample_arizona.html'},
{state: 'Arkansas', Cases: '3-200.html#3-210_Arkansas', Statutes:'3-300.html#3-320_Arkansas', Regulations:'3-400.html#3-410_Arkansas', Examples_and_Rules:'state_samples/sample_arkansas.html'},
{state: 'California', Cases: '3-200.html#3-210_California', Statutes:'3-300.html#3-320_California', Regulations:'3-400.html#3-410_California', Examples_and_Rules:'state_samples/sample_california.html'},
{state: 'Colorado', Cases: '3-200.html#3-210_Colorado', Statutes:'3-300.html#3-320_Colorado', Regulations:'3-400.html#3-410_Colorado', Examples_and_Rules:'state_samples/sample_colorado.html'},
{state: 'Connecticut', Cases: '3-200.html#3-210_Connecticut', Statutes:'3-300.html#3-320_Connecticut', Regulations:'3-400.html#3-410_Connecticut', Examples_and_Rules:'state_samples/sample_connecticut.html'},
{state: 'Delaware', Cases: '3-200.html#3-210_Delaware', Statutes:'3-300.html#3-320_Delaware', Regulations:'3-400.html#3-410_Delaware', Examples_and_Rules:'state_samples/sample_delaware.html'},
{state: 'District of Columbia', Cases: '3-200.html#3-210_District_of_Columbia', Statutes:'3-300.html#3-320_District_of_Columbia', Regulations:'3-400.html#3-410_District_of_Columbia', Examples_and_Rules:'state_samples/sample_district_of_columbia.html'},
{state: 'Florida', Cases: '3-200.html#3-210_Florida', Statutes:'3-300.html#3-320_Florida', Regulations:'3-400.html#3-410_Florida', Examples_and_Rules:'state_samples/sample_florida.html'},
{state: 'Georgia', Cases: '3-200.html#3-210_Georgia', Statutes:'3-300.html#3-320_Georgia', Regulations:'3-400.html#3-410_Georgia', Examples_and_Rules:'state_samples/sample_georgia.html'},
{state: 'Hawaii', Cases: '3-200.html#3-210_Hawaii', Statutes:'3-300.html#3-320_Hawaii', Regulations:'3-400.html#3-410_Hawaii', Examples_and_Rules:'state_samples/sample_hawaii.html'},
{state: 'Idaho', Cases: '3-200.html#3-210_Idaho', Statutes:'3-300.html#3-320_Idaho', Regulations:'3-400.html#3-410_Idaho', Examples_and_Rules:'state_samples/sample_idaho.html'},
{state: 'Illinois', Cases: '3-200.html#3-210_Illinois', Statutes:'3-300.html#3-320_Illinois', Regulations:'3-400.html#3-410_Illinois', Examples_and_Rules:'state_samples/sample_illinois.html'},
{state: 'Indiana', Cases: '3-200.html#3-210_Indiana', Statutes:'3-300.html#3-320_Indiana', Regulations:'3-400.html#3-410_Indiana', Examples_and_Rules:'state_samples/sample_indiana.html'},
{state: 'Iowa', Cases: '3-200.html#3-210_Iowa', Statutes:'3-300.html#3-320_Iowa', Regulations:'3-400.html#3-410_Iowa', Examples_and_Rules:'state_samples/sample_iowa.html'},
{state: 'Kansas', Cases: '3-200.html#3-210_Kansas', Statutes:'3-300.html#3-320_Kansas', Regulations:'3-400.html#3-410_Kansas', Examples_and_Rules:'state_samples/sample_kansas.html'},
{state: 'Kentucky', Cases: '3-200.html#3-210_Kentucky', Statutes:'3-300.html#3-320_Kentucky', Regulations:'3-400.html#3-410_Kentucky', Examples_and_Rules:'state_samples/sample_kentucky.html'},
{state: 'Louisiana', Cases: '3-200.html#3-210_Louisiana', Statutes:'3-300.html#3-320_Louisiana', Regulations:'3-400.html#3-410_Louisiana', Examples_and_Rules:'state_samples/sample_louisiana.html'},
{state: 'Maine', Cases: '3-200.html#3-210_Maine', Statutes:'3-300.html#3-320_Maine', Regulations:'3-400.html#3-410_Maine', Examples_and_Rules:'state_samples/sample_maine.html'},
{state: 'Maryland', Cases: '3-200.html#3-210_Maryland', Statutes:'3-300.html#3-320_Maryland', Regulations:'3-400.html#3-410_Maryland', Examples_and_Rules:'state_samples/sample_maryland.html'},
{state: 'Massachusetts', Cases: '3-200.html#3-210_Massachusetts', Statutes:'3-300.html#3-320_Massachusetts', Regulations:'3-400.html#3-410_Massachusetts', Examples_and_Rules:'state_samples/sample_massachusetts.html'},
{state: 'Michigan', Cases: '3-200.html#3-210_Michigan', Statutes:'3-300.html#3-320_Michigan', Regulations:'3-400.html#3-410_Michigan', Examples_and_Rules:'state_samples/sample_michigan.html'},
{state: 'Minnesota', Cases: '3-200.html#3-210_Minnesota', Statutes:'3-300.html#3-320_Minnesota', Regulations:'3-400.html#3-410_Minnesota', Examples_and_Rules:'state_samples/sample_minnesota.html'},
{state: 'Mississippi', Cases: '3-200.html#3-210_Mississippi', Statutes:'3-300.html#3-320_Mississippi', Regulations:'3-400.html#3-410_Mississippi', Examples_and_Rules:'state_samples/sample_mississippi.html'},
{state: 'Missouri', Cases: '3-200.html#3-210_Missouri', Statutes:'3-300.html#3-320_Missouri', Regulations:'3-400.html#3-410_Missouri', Examples_and_Rules:'state_samples/sample_missouri.html'},
{state: 'Montana', Cases: '3-200.html#3-210_Montana', Statutes:'3-300.html#3-320_Montana', Regulations:'3-400.html#3-410_Montana', Examples_and_Rules:'state_samples/sample_montana.html'},
{state: 'Nebraska', Cases: '3-200.html#3-210_Nebraska', Statutes:'3-300.html#3-320_Nebraska', Regulations:'3-400.html#3-410_Nebraska', Examples_and_Rules:'state_samples/sample_nebraska.html'},
{state: 'Nevada', Cases: '3-200.html#3-210_Nevada', Statutes:'3-300.html#3-320_Nevada', Regulations:'3-400.html#3-410_Nevada', Examples_and_Rules:'state_samples/sample_nevada.html'},
{state: 'New Hampshire', Cases: '3-200.html#3-210_New_Hampshire', Statutes:'3-300.html#3-320_New_Hampshire', Regulations:'3-400.html#3-410_New_Hampshire', Examples_and_Rules:'state_samples/sample_new_hampshire.html'},
{state: 'New Jersey', Cases: '3-200.html#3-210_New_Jersey', Statutes:'3-300.html#3-320_New_Jersey', Regulations:'3-400.html#3-410_New_Jersey', Examples_and_Rules:'state_samples/sample_new_jersey.html'},
{state: 'New Mexico', Cases: '3-200.html#3-210_New_Mexico', Statutes:'3-300.html#3-320_New_Mexico', Regulations:'3-400.html#3-410_New_Mexico', Examples_and_Rules:'state_samples/sample_new_mexico.html'},
{state: 'New York', Cases: '3-200.html#3-210_New_York', Statutes:'3-300.html#3-320_New_York', Regulations:'3-400.html#3-410_New_York', Examples_and_Rules:'state_samples/sample_new_york.html'},
{state: 'North Carolina', Cases: '3-200.html#3-210_North_Carolina', Statutes:'3-300.html#3-320_North_Carolina', Regulations:'3-400.html#3-410_North_Carolina', Examples_and_Rules:'state_samples/sample_north_carolina.html'},
{state: 'North Dakota', Cases: '3-200.html#3-210_North_Dakota', Statutes:'3-300.html#3-320_North_Dakota', Regulations:'3-400.html#3-410_North_Dakota', Examples_and_Rules:'state_samples/sample_north_dakota.html'},
{state: 'Ohio', Cases: '3-200.html#3-210_Ohio', Statutes:'3-300.html#3-320_Ohio', Regulations:'3-400.html#3-410_Ohio', Examples_and_Rules:'state_samples/sample_ohio.html'},
{state: 'Oklahoma', Cases: '3-200.html#3-210_Oklahoma', Statutes:'3-300.html#3-320_Oklahoma', Regulations:'3-400.html#3-410_Oklahoma', Examples_and_Rules:'state_samples/sample_oklahoma.html'},
{state: 'Oregon', Cases: '3-200.html#3-210_Oregon', Statutes:'3-300.html#3-320_Oregon', Regulations:'3-400.html#3-410_Oregon', Examples_and_Rules:'state_samples/sample_oregon.html'},
{state: 'Pennsylvania', Cases: '3-200.html#3-210_Pennsylvania', Statutes:'3-300.html#3-320_Pennsylvania', Regulations:'3-400.html#3-410_Pennsylvania', Examples_and_Rules:'state_samples/sample_pennsylvania.html'},
{state: 'Rhode Island', Cases: '3-200.html#3-210_Rhode_Island', Statutes:'3-300.html#3-320_Rhode_Island', Regulations:'3-400.html#3-410_Rhode_Island', Examples_and_Rules:'state_samples/sample_rhode_island.html'},
{state: 'South Carolina', Cases: '3-200.html#3-210_South_Carolina', Statutes:'3-300.html#3-320_South_Carolina', Regulations:'3-400.html#3-410_South_Carolina', Examples_and_Rules:'state_samples/sample_south_carolina.html'},
{state: 'South Dakota', Cases: '3-200.html#3-210_South_Dakota', Statutes:'3-300.html#3-320_South_Dakota', Regulations:'3-400.html#3-410_South_Dakota', Examples_and_Rules:'state_samples/sample_south_dakota.html'},
{state: 'Tennessee', Cases: '3-200.html#3-210_Tennessee', Statutes:'3-300.html#3-320_Tennessee', Regulations:'3-400.html#3-410_Tennessee', Examples_and_Rules:'state_samples/sample_tennessee.html'},
{state: 'Texas', Cases: '3-200.html#3-210_Texas', Statutes:'3-300.html#3-320_Texas', Regulations:'3-400.html#3-410_Texas', Examples_and_Rules:'state_samples/sample_texas.html'},
{state: 'Utah', Cases: '3-200.html#3-210_Utah', Statutes:'3-300.html#3-320_Utah', Regulations:'3-400.html#3-410_Utah', Examples_and_Rules:'state_samples/sample_utah.html'},
{state: 'Vermont', Cases: '3-200.html#3-210_Vermont', Statutes:'3-300.html#3-320_Vermont', Regulations:'3-400.html#3-410_Vermont', Examples_and_Rules:'state_samples/sample_vermont.html'},
{state: 'Virginia', Cases: '3-200.html#3-210_Virginia', Statutes:'3-300.html#3-320_Virginia', Regulations:'3-400.html#3-410_Virginia', Examples_and_Rules:'state_samples/sample_virginia.html'},
{state: 'Washington', Cases: '3-200.html#3-210_Washington', Statutes:'3-300.html#3-320_Washington', Regulations:'3-400.html#3-410_Washington', Examples_and_Rules:'state_samples/sample_washington.html'},
{state: 'West Virginia', Cases: '3-200.html#3-210_West_Virginia', Statutes:'3-300.html#3-320_West_Virginia', Regulations:'3-400.html#3-410_West_Virginia', Examples_and_Rules:'state_samples/sample_west_virginia.html'},
{state: 'Wisconsin', Cases: '3-200.html#3-210_Wisconsin', Statutes:'3-300.html#3-320_Wisconsin', Regulations:'3-400.html#3-410_Wisconsin', Examples_and_Rules:'state_samples/sample_wisconsin.html'},
{state: 'Wyoming', Cases: '3-200.html#3-210_Wyoming', Statutes:'3-300.html#3-320_Wyoming', Regulations:'3-400.html#3-410_Wyoming', Examples_and_Rules:'state_samples/sample_wyoming.html'}
  ];
  
});


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
          if(value == true){
            
            $(element).modal('show');
            $('.modal-content').draggable();
          }
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
