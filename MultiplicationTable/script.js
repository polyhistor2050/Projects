const table = [];
const size = 12;
for (let x = 0; x < size; x++){
    const temp = [];
    for (let y = 0; y < size; y++){
        temp.push(x * y);
    }
    table.push(temp);
}
console.table(table);