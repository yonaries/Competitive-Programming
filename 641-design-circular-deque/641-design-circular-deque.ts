class MyCircularDeque {
    size: number = 0
    queue: number[] = []
    constructor(k: number) {
        this.size = k
    }

    insertFront(value: number): boolean {
        if (this.queue.length === this.size) return false
        const result = this.queue.unshift(value)
        return (result || result === 0) ? true : false
    }

    insertLast(value: number): boolean {
        if (this.queue.length === this.size) return false
        const result = this.queue.push(value)
        return (result || result === 0) ? true : false
    }

    deleteFront(): boolean {
        const result = this.queue.shift()
        return (result || result === 0) ? true : false
    }

    deleteLast(): boolean {
        const result = this.queue.pop()
        return (result || result === 0) ? true : false
    }

    getFront(): number {
        const result = this.queue[0]
        return (result || result === 0) ? result : -1
    }

    getRear(): number {
        const result = this.queue[this.queue.length - 1]
        return (result || result === 0) ? result : -1
    }   

    isEmpty(): boolean {
        return (!this.queue.length)
    }

    isFull(): boolean {
        if (this.queue.length >= this.size) return true
        return false
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */