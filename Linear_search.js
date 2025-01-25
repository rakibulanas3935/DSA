const linearSearch=(arr,value)=>{
    for(let index of arr){
        if(arr[index]===value){
            return index
        }
    }
    return -1
}

const arr=[3,4,5,6,4,3,7]
let res=linearSearch(arr,10)
console.log(res)