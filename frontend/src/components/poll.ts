
export function poll(fn, ms) {
    const interval = setInterval(fn, ms);
    fn();

    return () => clearInterval(interval);
}