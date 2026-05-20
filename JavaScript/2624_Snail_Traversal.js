/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) return [];
    const result = Array.from({ length: rowsCount }, () => new Array(colsCount));
    for (let col = 0; col < colsCount; col++) {
        for (let row = 0; row < rowsCount; row++) {
            const idx = col * rowsCount + row;
            const r = col % 2 === 0 ? row : rowsCount - 1 - row;
            result[r][col] = this[idx];
        }
    }
    return result;
};
