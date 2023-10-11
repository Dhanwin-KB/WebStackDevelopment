const fs = require('fs');
const path = require('path')
fs.readFile(path.join(__dirname, 'posts','blogPost.txt'),'utf-8', (err,data) => {
    if (err) 
    {
        console.log('File Read Error');
    }
    console.log('data');
    const content = Buffer.from(data);
    console.log(cont.toString());
    console.log('data');
});