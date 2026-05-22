/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null) return 'null';
    if (typeof object === 'boolean' || typeof object === 'number') return String(object);
    if (typeof object === 'string') return `"${object}"`;
    if (Array.isArray(object)) {
        return '[' + object.map(jsonStringify).join(',') + ']';
    }
    const pairs = Object.keys(object).map(k => `"${k}":${jsonStringify(object[k])}`);
    return '{' + pairs.join(',') + '}';
};
