const fishlist = [3, 4, 3, 1, 2];

const maxdays = 80;

grandcache = {};

const getFish = (seed, days, cache = {}) => {
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
        grandkids += getFish(8, days - (passedDays + 1));
        // if (grandcache[cacheKey] !== undefined) {
        //   grandkids += grandcache[cacheKey];
        // } else {
        //   grandkids += getFish(8, days - (passedDays + 1));
        //   grandcache[cacheKey] = grandkids;
        // }
      }
      fishdays = 7;
    }
    // if (fishdays === 0) {
    //   fishdays = 6;
    //   // if (passedDays + 8 >= days) {
    //   //   grandkids = getFish(8, days - passedDays);
    //   //   console.log(`grandkids for ${seed}: ${grandkids}`);
    //   // }
    // } else {
    //   fishdays--;
    // }
    // console.log(`${passedDays}: ${fishdays}`);
    fishdays--;
    passedDays++;
  }
  // console.log(kids);

  // console.log(`grandkids ${seed} ${grandkids}`);
  return kids + grandkids;
};

let sum = 0;
fishlist.forEach((fish, idx) => {
  fishkids = getFish(fish, maxdays);
  console.log(fish, fishkids);
  sum += fishkids;
});

console.log("total", sum);
