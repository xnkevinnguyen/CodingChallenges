const { consoleAverageTime } = require('../utils/timer')

/*
0.050ms
0.005ms
*/
var numJewelsInStones3 = function(J, S) {
  let stoneMap = new Map()
  let jewelCount = 0

  for (s of S) {
    if (!stoneMap.has(s)) {
      stoneMap.set(s, 1)
    } else {
      stoneMap.set(s, stoneMap.get(s) + 1)
    }
  }

  for (j of J) {
    if (stoneMap.has(j)) {
      jewelCount += stoneMap.get(j)
    }
  }
  return jewelCount
}

/*
0.024ms
0.006ms
*/
var numJewelsInStones2 = function(J, S) {
  const jewelCount = S.split('').filter(char => J.indexOf(char) !== -1).length
  return jewelCount
}

/*
0.022ms
0.004ms
*/
var numJewelsInStones = function(J, S) {
  let jewelCount = 0

  for (let i = 0; i < S.length; i++) {
    if (J.indexOf(S[i]) !== -1) {
      jewelCount++
    }
  }
  return jewelCount
}

// sample 1
const j1 = 'aA'
const s1 = 'aAAbbbb'

// sample 2
const j2 = 'z'
const s2 = 'ZZ'

consoleAverageTime(() => numJewelsInStones(j1, s1))
consoleAverageTime(() => numJewelsInStones(j2, s2))
