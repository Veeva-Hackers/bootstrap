var helloApp = angular.module('helloApp', []);

helloApp.controller('resultListCtrl', function ($scope) {
  $scope.restaurants = [
    {'name': 'Round Table'},
      {'name': 'McDonalds'},
      {'name': 'Burger King'},
      {'name': 'Carls Jr'}
  ];
});