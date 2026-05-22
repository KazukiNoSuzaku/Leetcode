/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
var promisePool = async function(functions, n) {
    const executing = new Set();
    for (const fn of functions) {
        const p = fn().then(() => executing.delete(p));
        executing.add(p);
        if (executing.size >= n) {
            await Promise.race(executing);
        }
    }
    await Promise.all(executing);
};
