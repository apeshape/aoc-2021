// const fishlist = [3, 4, 3, 1, 2];
const fishlist = [
  4, 5, 3, 2, 3, 3, 2, 4, 2, 1, 2, 4, 5, 2, 2, 2, 4, 1, 1, 1, 5, 1, 1, 2, 5, 2,
  1, 1, 4, 4, 5, 5, 1, 2, 1, 1, 5, 3, 5, 2, 4, 3, 2, 4, 5, 3, 2, 1, 4, 1, 3, 1,
  2, 4, 1, 1, 4, 1, 4, 2, 5, 1, 4, 3, 5, 2, 4, 5, 4, 2, 2, 5, 1, 1, 2, 4, 1, 4,
  4, 1, 1, 3, 1, 2, 3, 2, 5, 5, 1, 1, 5, 2, 4, 2, 2, 4, 1, 1, 1, 4, 2, 2, 3, 1,
  2, 4, 5, 4, 5, 4, 2, 3, 1, 4, 1, 3, 1, 2, 3, 3, 2, 4, 3, 3, 3, 1, 4, 2, 3, 4,
  2, 1, 5, 4, 2, 4, 4, 3, 2, 1, 5, 3, 1, 4, 1, 1, 5, 4, 2, 4, 2, 2, 4, 4, 4, 1,
  4, 2, 4, 1, 1, 3, 5, 1, 5, 5, 1, 3, 2, 2, 3, 5, 3, 1, 1, 4, 4, 1, 3, 3, 3, 5,
  1, 1, 2, 5, 5, 5, 2, 4, 1, 5, 1, 2, 1, 1, 1, 4, 3, 1, 5, 2, 3, 1, 3, 1, 4, 1,
  3, 5, 4, 5, 1, 3, 4, 2, 1, 5, 1, 3, 4, 5, 5, 2, 1, 2, 1, 1, 1, 4, 3, 1, 4, 2,
  3, 1, 3, 5, 1, 4, 5, 3, 1, 3, 3, 2, 2, 1, 5, 5, 4, 3, 2, 1, 5, 1, 3, 1, 3, 5,
  1, 1, 2, 1, 1, 1, 5, 2, 1, 1, 3, 2, 1, 5, 5, 5, 1, 1, 5, 1, 4, 1, 5, 4, 2, 4,
  5, 2, 4, 3, 2, 5, 4, 1, 1, 2, 4, 3, 2, 1,
];

const getFish = (seed, days, cache = {}) => {
  const cacheKey = `${seed}_${days}`;
  if (cache[cacheKey]) {
    return cache[cacheKey];
  }

  let fishdays = seed;
  let kids = 0;
  let passedDays = 0;
  let grandkids = 0;
  while (passedDays < days) {
    if (fishdays === 0) {
      if (fishdays + 1 < days) {
        kids++;
      }
      const canHaveGrandkids = passedDays + 8 < days;
      if (canHaveGrandkids) {
        grandkids += getFish(8, days - (passedDays + 1), cache);
      }
      fishdays = 7;
    }
    fishdays--;
    passedDays++;
  }
  cache[cacheKey] = kids + grandkids;
  return kids + grandkids;
};

console.time("start");
let part1 = 0;
fishlist.forEach((fish) => {
  fishkids = getFish(fish, 80);
  part1 += fishkids;
});

let part2 = 0;
fishlist.forEach((fish) => {
  fishkids = getFish(fish, 256);
  part2 += fishkids;
});
console.timeEnd("start");

console.log("part1: ", part1 + fishlist.length);
console.log("part2: ", part2 + fishlist.length);
