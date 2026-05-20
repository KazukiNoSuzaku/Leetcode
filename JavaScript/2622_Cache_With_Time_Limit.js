var TimeLimitedCache = function() {
    this.cache = new Map();
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const existing = this.cache.get(key);
    const exists = existing !== undefined && existing.expiry > Date.now();
    if (existing) clearTimeout(existing.timer);
    const timer = setTimeout(() => this.cache.delete(key), duration);
    this.cache.set(key, { value, expiry: Date.now() + duration, timer });
    return exists;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const entry = this.cache.get(key);
    return entry && entry.expiry > Date.now() ? entry.value : -1;
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.cache.size;
};
