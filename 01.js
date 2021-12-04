const fs = require("fs");
const input = fs.readFileSync("./01.input", "utf-8");

let prev;
const aSum = input
  .trim()
  .split("\n")
  .map(Number)
  .reduce((acc, curr, idx, arr) => {
    const sum = arr[idx - 2] + arr[idx - 1] + curr;
    if (prev && sum > prev) {
      acc += 1;
    }
    prev = sum;
    return acc;
  }, 0);

console.log({ aSum });
