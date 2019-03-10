const { consoleAverageTime } = require('../utils/timer')

var toLowerCase = function(str) {
  const lowUpMap = new Map([
    ['A', 'a'],
    ['B', 'b'],
    ['C', 'c'],
    ['D', 'd'],
    ['E', 'e'],
    ['F', 'f'],
    ['G', 'g'],
    ['H', 'h'],
    ['I', 'i'],
    ['J', 'j'],
    ['K', 'k'],
    ['L', 'l'],
    ['M', 'm'],
    ['N', 'n'],
    ['O', 'o'],
    ['P', 'p'],
    ['Q', 'q'],
    ['R', 'r'],
    ['S', 's'],
    ['T', 't'],
    ['U', 'u'],
    ['V', 'v'],
    ['W', 'w'],
    ['X', 'x'],
    ['Y', 'y'],
    ['Z', 'z']
  ])
  let newString = ''
  for (let i = 0; i < str.length; i++) {
    newString += lowUpMap.get(str[i]) || str[i]
  }
  return newString
}

const s1 = 'Hello'
const s2 = 'here'
const s3 = 'LOVELY'
const s4 = 'kasdhkjhqkdnASDWQEDkasjdkjahsdQWEQWDnbdsjhadhQWDQWASDAs'

console.log(toLowerCase(s1))
console.log(toLowerCase(s2))
console.log(toLowerCase(s3))
