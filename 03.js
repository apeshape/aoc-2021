const testinput = `00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010`;

const fs = require("fs");
const input = fs.readFileSync("./03.input", "utf-8");

const bytes = input.split("\n");

// const bits = bytes[0].split("");

const getBitCountForPos = (pos, list) => {
  // const count = {
  //   g: 0,
  //   e: 0,
  // };
  const bitCount = [0, 0];

  list.forEach((byte) => {
    bitCount[byte[pos]] += 1;
  });

  return bitCount;
  // list[0].split("").forEach((bit, idx) => {
  //   const bitCount = [0, 0];
  //   bytes.forEach((byte) => {
  //     bitCount[byte[idx]] += 1;
  //   });
  //   if (bitCount[0] > bitCount[1]) {
  //     gamma += "0";
  //     epsilon += "1";
  //   }
  //   if (bitCount[1] > bitCount[0]) {
  //     gamma += "1";
  //     epsilon += "0";
  //   }
  // });
};

const getSearchNumber = (type, bitCount) => {
  if (type === "oxygen") {
    if (bitCount[0] === bitCount[1]) return "1";
    return bitCount[0] > bitCount[1] ? "0" : "1";
  }
  if (bitCount[0] === bitCount[1]) return "0";
  return bitCount[0] > bitCount[1] ? "1" : "0";
};

const getNumber = (type = "oxygen", list, pos = 0) => {
  if (list.length === 1) return list[0];

  const length = list[0].length;
  if (pos < length) {
    const bitCount = getBitCountForPos(pos, list);

    let search = getSearchNumber(type, bitCount);
    const newList = list.filter((i) => i[pos] === search);
    return getNumber(type, newList, pos + 1);
  }
};

const oxygen = parseInt(getNumber("oxygen", bytes), 2);
const co2 = parseInt(getNumber("co2", bytes), 2);
console.log({ oxygen, co2 }, oxygen * co2);
