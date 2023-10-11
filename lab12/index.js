import { mkdir } from 'fs';
import { join } from 'path';

mkdir(join(__dirname, '/posts'), (err) => {
    if (err)
    {
        console.log(err);
        console.log("folder with that name already exists");
        return;
    }
    console.log("Posts Folder Created!");
});