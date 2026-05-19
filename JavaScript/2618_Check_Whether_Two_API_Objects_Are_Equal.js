/**
 * @param {object} o1
 * @param {object} o2
 * @return {boolean}
 */
var areSame = function(o1, o2) {
    if (typeof o1 !== typeof o2) return false;
    if (typeof o1 !== 'object' || o1 === null) return o1 === o2;
    if (Array.isArray(o1) !== Array.isArray(o2)) return false;
    const keys1 = Object.keys(o1).sort();
    const keys2 = Object.keys(o2).sort();
    if (keys1.length !== keys2.length) return false;
    return keys1.every((k, i) => k === keys2[i] && areSame(o1[k], o2[k]));
};
