class signalBus {
    constructor() {
        this.listeners = {};
    };

    on(e, callback) {
        if (!this.listeners[e]) this.listeners[e] = [];
        this.listeners[e].push(callback);
    };

    emit(e, d) {
        if (e === undefined) { 
            console.error('event cannot be undefined'); 
            return; 
        }
        (this.listeners[e] || []).forEach(cb => cb(d));
    };

    off(e, callback) {
        if (!this.listeners[e]) return;
        this.listeners[e] = this.listeners[e].filter(cb => cb !== callback);
    };
};