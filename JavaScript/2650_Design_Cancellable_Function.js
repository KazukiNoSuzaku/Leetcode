function cancellable(generator) {
    let cancelled = false;
    let rejectFn;

    const promise = new Promise((resolve, reject) => {
        rejectFn = reject;

        function step(nextFn, arg) {
            if (cancelled) return;
            let result;
            try {
                result = nextFn(arg);
            } catch (e) {
                reject(e);
                return;
            }
            if (result.done) {
                resolve(result.value);
            } else {
                Promise.resolve(result.value).then(
                    val => step(generator.next.bind(generator), val),
                    err => step(generator.throw.bind(generator), err)
                );
            }
        }

        step(generator.next.bind(generator), undefined);
    });

    const cancel = () => {
        cancelled = true;
        generator.return(undefined);
        rejectFn("Cancelled");
    };

    return [cancel, promise];
}
