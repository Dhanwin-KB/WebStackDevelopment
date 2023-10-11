const fs = require('fs');
const path = require('path')
fs.appendFile(path.join(__dirname, 'posts','blogPost.txt'),'\nMore data', (err) => {
    if (err) 
    {
        console.log('Error in Data Addition');
        return;
    }
    console.log('File contents updated');
});