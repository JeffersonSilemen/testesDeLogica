function reverseStr(str){
    var splitStr = str.split('')
    var newStr = [];
    k = splitStr.length - 1
    for (let i of splitStr){
        newStr.push(splitStr[k]);
        k = k - 1;
    }
    newStr = newStr.join('')

    console.log(`A string ${str} invertida é ${newStr}`);
}

reverseStr('programador')