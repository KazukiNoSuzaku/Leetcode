/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    // Trie of Maps keyed by argument references; works for any arg type
    const root = { children: new Map(), hasResult: false, result: undefined };
    return function(...args) {
        let node = root;
        for (const arg of args) {
            if (!node.children.has(arg)) {
                node.children.set(arg, { children: new Map(), hasResult: false, result: undefined });
            }
            node = node.children.get(arg);
        }
        if (!node.hasResult) {
            node.result = fn(...args);
            node.hasResult = true;
        }
        return node.result;
    };
}
