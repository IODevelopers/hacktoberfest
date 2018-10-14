let a = [5,10,15];
let b = ['A', 'B', 'C'];

var newList = function(a,b)
{
  let l = a.length+b.length;
  let r = [];
  let j=0,k=0;
  for(let i=0; i<l;i++) {
    if(i%2==0) {
      r[i]=a[j++];
    } else {
      r[i]=b[k++];
    }
  }
  return r;
}

console.log(newList(a,b));
