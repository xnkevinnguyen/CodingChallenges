const { PerformanceObserver, performance } = require('perf_hooks')

const REPEAT_COUNT = 10

function consoleAverageTime(func) {
  let totalTime = 0
  for (let i = 0; i < REPEAT_COUNT; i++) {
    var t0 = performance.now()
    func()
    var t1 = performance.now()
    totalTime += t1 - t0
  }
  console.log(`${(totalTime / REPEAT_COUNT).toFixed(3)}ms`)
}

module.exports = {
  consoleAverageTime
}
