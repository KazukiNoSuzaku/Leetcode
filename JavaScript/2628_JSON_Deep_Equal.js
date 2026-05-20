/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    if (o1 === o2) return true;
    if (o1 === null || o2 === null) return false;
    if (typeof o1 !== typeof o2) return false;
    if (typeof o1 !== 'object') return false;
    if (Array.isArray(o1) !== Array.isArray(o2)) return false;
    if (Array.isArray(o1)) {
        if (o1.length !== o2.length) return false;
        return o1.every((v, i) => areDeeplyEqual(v, o2[i]));
    }
    const keys1 = Object.keys(o1);
    const keys2 = Object.keys(o2);
    if (keys1.length !== keys2.length) return false;
    return keys1.every(k => k in o2 && areDeeplyEqual(o1[k], o2[k]));
};
