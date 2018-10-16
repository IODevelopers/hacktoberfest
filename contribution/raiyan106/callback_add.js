const add = (a,b)=>{
	return a+b;
}

const call = (o1,o2,callback) =>{
	return callback(o1,o2);
}


const result = call(5,10, add);
console.log(result);