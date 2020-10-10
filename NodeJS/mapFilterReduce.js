// The map() method creates a new array with the results of calling a function for every array element.
// The map() method calls the provided function once for each element in an array, in order.
// Note: map() does not execute the function for array elements without values.
// Note: map() does not change the original array.
//array.map(function(currentValue, index, arr), thisValue)
let arr = [1,2,3,4];

let plus5 = arr.map((val, i, arr) => {
    return val + 5;
  });

let newArr = arr.map((val, i, arr) => {
    return {
        value: val,
        index: i
    };
});
console.log(arr,plus5,newArr);

//Filter
arr = [1,2,3,4,5,6];
let even = arr.filter(val => {
    return val % 2 === 0;
  });

console.log(arr,even);

let data = [
    {
      country: 'China',
      population: 1409517397,
    },
    {
      country: 'India',
      population: 1339180127,
    },
    {
      country: 'USA',
      population: 324459463,
    },
    {
      country: 'Indonesia',
      population: 263991379,
    }
  ]
  let cities = data.filter(val => val.population > 500000000);
  console.log(data, cities);
// Reduce - The reduce() method is used to apply a function to each element in the array to reduce the array to a single value.
let sum = arr.reduce((acc, val) => acc + val, 100);
let data = [
    {
      country: 'China',
      pop: 1409517397,
    },
    {
      country: 'India',
      pop: 1339180127,
    },
    {
      country: 'USA',
      pop: 324459463,
    },
    {
      country: 'Indonesia',
      pop: 263991379,
    }
  ]
let sum = data.reduce((acc, val) => {
    return val.country == 'China' ? acc : acc + val.pop;
  }, 0);