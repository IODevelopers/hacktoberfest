cd ../../
rray of objects
var objArray = [
    {id: 1, name: 'User 1', address: '4 Redstone Road'},
  {id: 3, name: 'User 3', address: '18 Flinstone Parade'},
  {id: 7, name: 'User 7', address: 'Winston Lodge'},
  {id: 2, name: 'User 3', address: '28 Scrooble House'},
  {id: 4, name: 'User 4', address: '1 Redhut Crimble'},
];


// sort function params = objects to compare
function sortIdsDesc(a, b) {

    if(a.id < b.id) {
      // if b's ID is higher than a's ID then move down
    return -1;
  } else if(a.id > b.id) {
    // if a's ID is higher than b's id then move up
    return 1;
  }
  // keep same position
  return 0
}

console.log(objArray.sort(sortIdsDesc));
